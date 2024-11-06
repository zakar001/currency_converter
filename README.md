## Real-time Currency Conversion Tool

A Python-based tool for real-time currency conversion with historical data visualization.

### Features
- ✅ Real-time currency conversion
- ✅ Live exchange rates display
- ✅ Historical exchange rate data (up to 1 year)
- ✅ Interactive charts for historical trends
- ✅ Support for 150+ currencies
- ✅ Simple command-line interface

### Installation

1. **Clone or download the files** to your local directory

2. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Run the main application**:
   ```bash
   python main.py
   ```

2. **Or run the converter directly**:
   ```bash
   python currency_converter.py
   ```

3. **Test the functionality**:
   ```bash
   python test_converter.py
   ```

### How to Use

1. **Convert Currency**:
   - Select option 1 from the menu
   - Enter amount, source currency, and target currency
   - Get instant conversion with current exchange rate

2. **View Real-time Rates**:
   - Select option 2
   - Choose a base currency
   - See current exchange rates for major currencies

3. **View Historical Rates**:
   - Select option 3
   - Enter base and target currencies
   - Specify number of days for historical data
   - View data table and interactive chart

### Supported Currencies
The tool supports all major currencies including:
- USD (US Dollar)
- EUR (Euro)
- GBP (British Pound)
- JPY (Japanese Yen)
- CAD (Canadian Dollar)
- AUD (Australian Dollar)
- CHF (Swiss Franc)
- CNY (Chinese Yuan)
- INR (Indian Rupee)
- And 150+ more...

### API Information
- Uses free APIs from exchangerate-api.com and exchangerate.host
- No API key required for basic usage
- Real-time data updates every 24 hours
- Historical data available for up to 1 year

### File Structure
- `currency_api.py` - Core API functions for fetching data
- `currency_converter.py` - Main application with user interface
- `main.py` - Application entry point
- `test_converter.py` - Testing script
- `requirements.txt` - Python dependencies

### Requirements
- Python 3.6+
- requests library
- matplotlib (for charts)
- pandas (for data handling)

### Notes
- Internet connection required for real-time data
- Historical charts require matplotlib
- Free API has rate limits - be respectful with requests
- For production use, consider using paid API services

Enjoy converting currencies! 💱