.md

# Real-time Currency Converter with Historical Data

A Python-based currency conversion tool that provides real-time exchange rates and historical data analysis.

## Features

- 💱 **Real-time currency conversion** using live exchange rates
- 📊 **Historical data** for up to 30 days
- 💾 **Local caching** of exchange rates using SQLite
- 📝 **Conversion history** tracking
- 🖥️ **Multiple interfaces**: CLI and interactive mode
- 🌐 **Free API** using exchangerate.host (no API key required)

## Installation

1. **Clone or download the files** to your local directory
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Method 1: Command Line Interface (CLI)

**Basic Conversion:**
```bash
python cli_interface.py --amount 100 --from USD --to EUR
```

**With Historical Data:**
```bash
python cli_interface.py --amount 100 --from USD --to EUR --historical
```

**View Conversion History:**
```bash
python cli_interface.py --history
```

### Method 2: Interactive Mode

Run the interactive interface:
```bash
python interactive_mode.py
```

In interactive mode, you can:
- Convert currencies: `100 USD to EUR`
- View history: `history`
- Check historical rates: `historical`
- Get help: `help`
- Exit: `quit` or `exit`

### Method 3: Programmatic Usage

Use the converter in your own Python scripts:

```python
from currency_converter import CurrencyConverter

converter = CurrencyConverter()

# Convert currency
result = converter.convert_currency(100, 'USD', 'EUR')
print(f"100 USD = {result:.2f} EUR")

# Get historical data
historical_rates = converter.get_historical_rates('USD',