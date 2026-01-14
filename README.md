# Portfolio Management

A Python project for managing and rebalancing stock portfolios using pandas, yfinance, and Pydantic for data validation.

## Features
- Define target allocations and current shares for your portfolio
- Fetch real-time stock prices using yfinance
- Calculate portfolio value and suggest rebalancing actions
- Input validation with Pydantic

## Requirements
- Python 3.8+
- pandas
- yfinance
- pydantic

Install dependencies:
```
pip install -r requirements.txt
```

## Usage

Example usage in `portfolio.py`:

```python
from portfolio import Portfolio

allocations = {"AAPL": 0.6, "META": 0.4}
current_shares = {"AAPL": 10, "META": 40}
portfolio = Portfolio(allocations, current_shares)
print(portfolio.rebalance())
```

## Project Structure
- `portfolio.py` - Main logic for portfolio management
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules
## Referencia GEMINI
https://gemini.google.com/share/923ae6f68f9f
## License
MIT
