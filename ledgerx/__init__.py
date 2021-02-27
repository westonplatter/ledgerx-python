import os

# settings
API_BASE = "https://api.ledgerx.com"
DELAY_SECONDS = 0.0

# configurations
api_key = None
verify_ssl_certs = True

# endpoints as classes
from ledgerx.trades import Trades
from ledgerx.contracts import Contracts
