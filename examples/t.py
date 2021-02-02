import pandas as pd
from time import sleep

from ledgerx import Trades
from ledgerx import Contracts


# # trades
# #
# # list, w/ default params
data = Trades.list_all({"limit": 50})
df = pd.DataFrame.from_dict(data)
df.to_csv("all_trades.csv")


# print(data)
# sleep(1.0)
# #
# # list, w/ custom params
# params = dict(min_size=2)
# data = Trades.list(params)
# print(data)
# sleep(1.0)
# #
# # next
# data = Trades.next(data["meta"]["next"])
# print(data)
# sleep(1.0)

# contracts
# data = Contracts.list()
# xs = Contracts.list_all_expiration_dates()

# for x in xs:
#     print(x)
