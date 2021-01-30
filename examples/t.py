from time import sleep
from ledgerx.trade_blotter import TraderBlotter

data = TraderBlotter.list({})

sleep(1.0)

data = TraderBlotter.next(data["meta"]["next"])


print(data)
