import ledgerx
from examples.example_util import get_env_api_key

ledgerx.api_key = get_env_api_key()


resolutions = ["1H", "1D", "1W", "1M", "3M", "1Y"]

for res in resolutions:
    params = {"resolution": res}
    data = ledgerx.Bitvol.list_eth(params)
    print("-------------------")
    print(f"params={params} returns {len(data['data'])} data points")
    print(f"First vol object={data['data'][-1]}")
    print(f"First vol object={data['data'][-2]}")
    print(f"First vol object={data['data'][-3]}")
