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
Caso de uso tipico donde se tiene dos stock que se reparten el 100%

```python
from portfolio import Portfolio

allocations = {"AAPL": 0.6, "META": 0.4}
current_shares = {"AAPL": 10, "META": 40}
portfolio = Portfolio(allocations, current_shares)
print(portfolio.rebalance())
```
## OUTPUT
```python
Se deben comprar 54.0201493966673 acciones de AAPL
Se deben vender 22.34540239902391 acciones de META
AAPL    54.020149
META   -22.345402
```
## Usage

Example usage in `portfolio.py`:
Typical use case in which the target allocations are divided between two shares that we already own

```python
from portfolio import Portfolio

allocations = {"AAPL": 0.6, "META": 0.4}
current_shares = {"AAPL": 10, "META": 40}
portfolio = Portfolio(allocations, current_shares)
print(portfolio.rebalance())
```
## OUTPUT
```python
Se deben comprar 54.0201493966673 acciones de AAPL
Se deben vender 22.34540239902391 acciones de META
AAPL    54.020149
META   -22.345402
```
## Alternativa Usage

Example usage in `portfolio.py`:
This alternative use case considers the scenario in which we already have some stock shares and we want to add a new one along with new target allocations. In order to use this we must declare the new stock id and how the new target allocations are composed.

```python
from portfolio import Portfolio

allocations = {"AAPL":0.6,"META":0.2,"DLO":0.2}
current_shares = {"AAPL":10,"META":40}
portfolio = Portfolio(allocations, current_shares)
print(portfolio.rebalance())
```
## OUTPUT
```python
Se deben comprar 54.0201493966673 acciones de AAPL
Se deben vender 31.17270119951196 acciones de META
Se deben comprar 388.2104529616725 acciones de DLO
AAPL     54.020149
META    -31.172701
DLO     388.210453
```

## Project Structure
- `portfolio.py` - Main logic for portfolio management
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore rules
## Referencia GEMINI
https://gemini.google.com/share/923ae6f68f9f
## License
MIT
