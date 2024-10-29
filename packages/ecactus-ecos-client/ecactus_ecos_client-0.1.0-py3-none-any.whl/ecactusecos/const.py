"""EcactusEcos constants"""

API_HOST = "api-ecos-eu.weiheng-tech.com"

AUTH_ACCESS_TOKEN = "accessToken"

AUTHENTICATION_PATH = "/api/client/guide/login"
"""Path to perform authentication. Result is a user id and an auth token"""

"""Default source types to fetch if none are specified."""

CUSTOMER_OVERVIEW_PATH = "/api/client/settings/user/info"
"""Path to request details of the customer."""

DEVICE_LIST_PATH = "/api/client/home/device/list"

ACTUALS_PATH = "/api/client/home/now/device/runData"
"""Path to request actual values."""

AUTH_TOKEN_HEADER = "Authorization"
"""Header which should contain (in request) the authentication token"""
