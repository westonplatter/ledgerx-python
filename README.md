# LedgerX Python Client

FYI - I don't have access to the trading API at the moment (it's only available to institutional accounts). LedgerX will be allowing retail in the future, at which point I plan to build out all API endpoints. In the meantime, if you're an institution and want to use this, get in touch with me and I'd be happy to build the trading portion of the client.

## example
One of the many examples in the [examples](https://github.com/westonplatter/ledgerx-python/tree/main/examples) directory.

```
from ledgerx import Trades

data = Trades.list()

print(f"Number of trades = {len(data['data'])}")
print(f"Example trade = {data['data'][0]}")
```


## dev env
Currently managed via miniconda. To create the env and install deps, 
1. `make env.create`
2. `make env.update`
3. conda activate ledgerx

## testing
Run tests via `make test`

## license
See LICENSE file
