import ledgerx
from examples.example_util import get_env_api_key

ledgerx.api_key = get_env_api_key()

# id=22202077 -> BTC Mini 2021-12-31 Call $25,000
contract_id = 22202077

contract = ledgerx.Contracts.retrieve(contract_id)

print(contract)
