# Bjarkan Local

A local implementation of the Bjarkan Smart Order Router (SOR) system for personal trading.

## Features

- Real-time market data aggregation from multiple exchanges
- Fee-aware orderbook processing
- VWAP calculations
- Smart order routing and execution
- Trade monitoring and filtering

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file with your BetterStack token:
```
BETTERSTACK_TOKEN=your_token_here
```

2. Use the sample configurations in `instructions.py` as templates for your setup.

## Usage

```python
import asyncio
from bjarkan_local import OrderbookData, TradesData, OrderExecutor
from bjarkan_local.models import OrderbookConfig, TradesConfig, OrderConfig, APIConfig

# See instructions.py for configuration examples
async def main():
    # Initialize your configurations
    orderbook_config = OrderbookConfig(...)
    trades_config = TradesConfig(...)
    api_configs = [APIConfig(...)]

    # Initialize components
    orderbook_data = OrderbookData(orderbook_config)
    trades_data = TradesData(trades_config)
    executor = OrderExecutor(orderbook_config, api_configs)

    # Start data collection
    await orderbook_data.start()
    await trades_data.start()

    # Execute orders
    result = await executor.execute_order(order_config)

if __name__ == "__main__":
    asyncio.run(main())
```

## License

Private use only.