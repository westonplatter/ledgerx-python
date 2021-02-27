# WARNING
This codebase is still in an `alpha state` and could have bugs that result in financial losses. Use at your own risk.

# LedgerX Python Client
## example
One of the many examples in the [examples](https://github.com/westonplatter/ledgerx-python/tree/main/examples) directory.

```
from ledgerx import Trades

data = Trades.list()

print(f"Number of trades = {len(data['data'])}")
print(f"Example trade = {data['data'][0]}")
```
## dev env
Currently managed via miniconda. To create the env and install dependencies,
1. `make env.create`
2. `make env.update`
3. conda activate ledgerx

## testing
Run tests via `make test`

## license
See LICENSE file
