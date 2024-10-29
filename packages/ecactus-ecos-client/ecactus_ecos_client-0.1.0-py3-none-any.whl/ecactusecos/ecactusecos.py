# type: ignore
import asyncio
import aiohttp
import async_timeout
import time
from yarl import URL

from .const import (
    API_HOST,
    AUTHENTICATION_PATH,
    ACTUALS_PATH,
    AUTH_ACCESS_TOKEN,
    CUSTOMER_OVERVIEW_PATH,
    DEVICE_LIST_PATH,
    AUTH_TOKEN_HEADER,
)
from .exceptions import (
    EcactusEcosConnectionException,
    EcactusEcosException,
    EcactusEcosUnauthenticatedException,
)


class EcactusEcos:
    """Client to connect with EcactusEcos"""

    def __init__(
        self,
        username: str,
        password: str,
        api_scheme: str = "https",
        api_host: str = API_HOST,
        api_port: int = 443,
        request_timeout: int = 10,
    ):
        self.api_scheme = api_scheme
        self.api_host = api_host
        self.api_port = api_port
        self.request_timeout = request_timeout

        self._username = username
        self._password = password
        self._customer_info = None
        self._auth_token = None
        self._devices = None

    async def authenticate(self) -> None:
        """Log in using username and password.

        If succesfull, the authentication is saved and is_authenticated() returns true
        """
        # Make sure all data is cleared
        self.invalidate_authentication()

        url = URL.build(
            scheme=self.api_scheme,
            host=self.api_host,
            port=self.api_port,
            path=AUTHENTICATION_PATH,
        )

        # auth request, password grant type
        data = {
            "email": self._username,
            "password": self._password,
        }

        return await self.request(
            "POST",
            url,
            data=data,
            callback=self._handle_authenticate_response,
        )

    async def _handle_authenticate_response(self, response, params):
        json = await response.json()
        self._auth_token = json["data"][AUTH_ACCESS_TOKEN]

    async def customer_overview(self):
        """Request the customer overview."""
        if not self.is_authenticated():
            raise EcactusEcosUnauthenticatedException("Authentication required")

        url = URL.build(
            scheme=self.api_scheme,
            host=self.api_host,
            port=self.api_port,
            path=CUSTOMER_OVERVIEW_PATH,
        )

        return await self.request(
            "GET", url, callback=self._handle_customer_overview_response
        )

    async def _handle_customer_overview_response(self, response, params):
        json = await response.json()
        self._customer_info = json["data"]

    async def device_overview(self):
        if not self.is_authenticated():
            raise EcactusEcosUnauthenticatedException("Authentication required")

        url = URL.build(
            scheme=self.api_scheme,
            host=self.api_host,
            port=self.api_port,
            path=DEVICE_LIST_PATH,
        )
        return await self.request(
            "GET", url, callback=self._handle_device_list_repsonse
        )

    async def _handle_device_list_repsonse(self, response, params):
        json = await response.json()
        self._devices = dict()
        for device in json["data"]:
            self._devices[device["deviceId"]] = device

    async def actuals(self):
        """Request the actual values of the sources of the types configured in this instance (source_types)."""
        if not self.is_authenticated():
            raise EcactusEcosUnauthenticatedException("Authentication required")

        # If there is no device list load it
        if not self._devices:
            await self.device_overview()

        actuals = dict()
        for device_id in self.get_device_ids():
            url = URL.build(
                scheme=self.api_scheme,
                host=self.api_host,
                port=self.api_port,
                path=ACTUALS_PATH,
            )
            actuals[device_id] = await self.request(
                "POST",
                url,
                data={"deviceId": device_id},
                callback=self._handle_actuals_response,
            )
        return actuals

    async def _handle_actuals_response(self, response, params):
        json = await response.json()
        return json["data"]

    async def request(
        self,
        method: str,
        url: URL,
        data: dict = None,
        callback=None,
        params: dict = None,
    ):
        headers = {}
        json: dict = {
            **{
                "_t": int(time.time()),
                "clientType": "BROWSER",
                "clientVersion": "1.0",
            },
            **(data if data else {}),
        }

        # Insert authentication
        if self._auth_token is not None:
            headers[AUTH_TOKEN_HEADER] = "Bearer %s" % self._auth_token
        try:
            async with async_timeout.timeout(self.request_timeout):
                async with aiohttp.ClientSession() as session:
                    req = session.request(
                        method,
                        url,
                        json=json,
                        headers=headers,
                    )
                    async with req as response:
                        status = response.status
                        is_json = "application/json" in response.headers.get(
                            "Content-Type", ""
                        )

                        if (status == 401) | (status == 403):
                            raise EcactusEcosUnauthenticatedException(
                                await response.text()
                            )

                        if not is_json:
                            raise EcactusEcosException(
                                "Response is not json", await response.text()
                            )

                        if not is_json or (status // 100) in [4, 5]:
                            raise EcactusEcosException(
                                "Response is not success",
                                response.status,
                                await response.text(),
                            )

                        if callback is not None:
                            return await callback(response, params)

        except asyncio.TimeoutError as exception:
            raise EcactusEcosConnectionException(
                "Timeout occurred while communicating with EcactusEcos"
            ) from exception
        except aiohttp.ClientError as exception:
            raise EcactusEcosConnectionException(
                "Error occurred while communicating with EcactusEcos"
            ) from exception

    def is_authenticated(self):
        """Returns whether this instance is authenticated

        Note: despite this method returning true, requests could still fail to an authentication error."""
        return self._auth_token is not None

    def get_customer_info(self):
        """Returns the unique id of the currently authenticated user"""
        return self._customer_info

    def invalidate_authentication(self):
        """Invalidate the current authentication tokens and account details."""
        self._customer_info = None
        self._devices = None
        self._auth_token = None

    def get_device(self, device_id):
        """Gets the id of the device which belongs to the given source type, if present."""
        return (
            self._devices[device_id]
            if self._devices is not None and device_id in self._devices
            else None
        )

    def get_device_ids(self):
        """Gets the ids of the devices, if present."""
        return list(self._devices.keys()) if self._devices is not None else None
