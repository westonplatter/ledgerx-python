import glob
import os
import pandas as pd
from time import sleep, time


from ledgerx import Trades
from ledgerx import Contracts


CONSOLIDATED_TRADES_FILE = "examples/data/consolidated_trades.csv"


class StopRequestsException(Exception):
    pass


def consolidate_and_save_file() -> pd.DataFrame:
    file_names = glob.glob("examples/data/trades_*.csv")
    dfs = [pd.read_csv(f, index_col=[0]) for f in file_names]
    df = pd.DataFrame()

    # carry forward any trades in "examples/data/consolidated_trades.csv"
    if os.path.exists(CONSOLIDATED_TRADES_FILE):
        dfs.append(pd.read_csv(CONSOLIDATED_TRADES_FILE))

    if len(dfs) > 0:
        df = pd.concat(dfs)
        df.drop_duplicates(subset=["id", "timestamp"], inplace=True)
        df.sort_values("timestamp", ascending=True, inplace=True)
        df.reset_index(drop=True, inplace=True)
        df.to_csv(CONSOLIDATED_TRADES_FILE)
        # remove old files
        [os.remove(fn) for fn in file_names]

    return df


df = consolidate_and_save_file()

# initial values
last_timestamp = df.timestamp.values[-1] if df.index.size > 0 else None
count = 0

# callback that's inserted into the HTTP request circle
def callback_func(data):
    global count, last_timestamp
    count += 1
    ddf = pd.DataFrame.from_dict(data)
    epoch_time = int(time())
    ddf.to_csv(f"examples/data/trades_{epoch_time}.csv")
    print(".", end="", flush=True)
    if count % 10 == 0:
        print(f"count = {count}")
    if str(last_timestamp) in df["timestamp"].values:
        raise StopRequestsException()


# exit if there's a timestamp value we've already seen
try:
    data = Trades.list_all_incremental_return({"limit": 200}, callback_func)
except StopRequestsException:
    print("\nDownloaded all trades")

df = consolidate_and_save_file()
