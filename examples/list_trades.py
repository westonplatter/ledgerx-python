from ledgerx import Trades


data = Trades.list()
print(f"Number of trades = {len(data['data'])}")
print(f"Example trade = {data['data'][0]}")
