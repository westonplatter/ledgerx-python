import pandas as pd
from time import time

from ledgerx import Trades


def callback_func(data):
    df = pd.DataFrame.from_dict(data)
    epoch_time = int(time())
    df.to_csv(f"trades_{epoch_time}.csv")


data = Trades.list_all_incremental_return({"limit": 200}, callback_func)
