import ledgerx
from examples.example_util import get_env_api_key


ledgerx.api_key = get_env_api_key()


# default
res = ledgerx.Contracts.list_traded()
print(f"total number of trades = {res['meta']['total_count']}")

### see list of query parameters here, https://docs.ledgerx.com/reference#tradedcontracts
