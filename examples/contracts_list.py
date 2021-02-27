import ledgerx

from examples.example_util import get_env_api_key

ledgerx.api_key = get_env_api_key()


# default
data = ledgerx.Contracts.list_all()
print(f"default params returns = {len(data)}")


### see list of query parameters here, https://docs.ledgerx.com/reference#listcontracts


# list only calls
query_params = {"contract_type": "call"}
data = ledgerx.Contracts.list_all(query_params)
print(f"params({query_params}) returns = {len(data)}")


# list derivative types
query_params = {"derivative_type": "future_contract"}
data = ledgerx.Contracts.list_all(query_params)
print(f"params({query_params}) returns = {len(data)}")
