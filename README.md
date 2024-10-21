.md

# Real-time Currency Converter with Historical Data

A Python-based currency conversion tool that provides real-time exchange rates and historical data capabilities.

## Features

- **Real-time Conversion**: Get current exchange rates for 24+ major currencies
- **Historical Data**: Access historical exchange rates (simulated for free tier)
- **Command-line Interface**: Easy-to-use CLI for quick conversions
- **Interactive Mode**: User-friendly interactive session
- **Conversion History**: Track your recent conversions
- **Multiple Output Formats**: Full details or exchange rate only

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

**Basic Conversion:**
```bash
python cli_interface.py 100 USD EUR
```

**Historical Conversion:**
```bash
python cli_interface.py 100 USD EUR --date 2024-01-15
```

**Exchange Rate Only:**
```bash
python cli_interface.py 1 USD EUR --rate
```

**List Supported Currencies:**
```bash
python cli_interface.py --list-currencies
```

**Show Conversion History:**
```bash
python cli_interface.py --history
```

**Interactive Mode:**
```bash
python cli_interface.py
```

### Python API

```python
from currency_converter import CurrencyConverter

# Initialize converter
converter = CurrencyConverter()

# Real-time conversion
result = converter.convert(100, 'USD', 'EUR')
print(f"${result['original_amount']} USD = {result['converted_amount']} EUR")

# Historical conversion
historical_result = converter.convert(100, 'USD', 'EUR', '2024-01-15')

# Get exchange rate only
rate = converter.get_exchange_rate('USD', 'GBP')
```

### Demo

Run the demo to see all features:
```bash
python demo.py
```

## Supported Currencies

The tool supports 24 major currencies including:
USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, SGD, NZD, MXN, BRL, RUB, ZAR, KRW, TRY, AED, SAR, HKD, SEK, NOK, DKK, PLN

## API Limitations

- **Free Tier**: Uses ExchangeRate-API free tier with rate limitations
- **Historical Data**: Simulated for free tier (real historical data requires premium API)
- **Real-time Updates**: Rates are cached for 5 minutes to respect API limits

## File Structure

- `currency_api.py` - API client for fetching exchange rates
- `currency_converter.py` - Main conversion logic and history tracking
- `cli_interface.py` - Command-line interface
- `demo.py` - Demonstration script
- `requirements.txt` - Python dependencies

## Error Handling

- Network errors are caught and reported
- Invalid currency codes are handled gracefully
- Invalid dates are validated
- API rate limits are respected with caching

## Extending the Tool

To add premium features:
1. Get an API key from ExchangeRate-API or similar service
2. Pass the API key when initializing `CurrencyConverter`
3. Modify `currency_api.py` to use premium endpoints for historical data

## License

This is a demo project for educational purposes.