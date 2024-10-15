"""
Demo script showing various features of the currency converter.
"""

from currency_converter import CurrencyConverter
from datetime import datetime, timedelta

def demo():
    """Demonstrate the currency converter features."""
    print("Currency Converter Demo")
    print("=" * 50)
    
    converter = CurrencyConverter()
    
    # 1. Real-time conversion
    print("\n1. Real-time Conversion:")
    result = converter.convert(100, 'USD', 'EUR')
    if result:
        print(f"${result['original_amount']} USD = €{result['converted_amount']} EUR")
        print(f"Current exchange rate: {result['exchange_rate']}")
    
    # 2. Multiple conversions
    print("\n2. Multiple Currency Conversions:")
    test_conversions = [
        (50, 'EUR', 'GBP'),
        (1000, 'USD', 'JPY'),
        (75, 'CAD', 'AUD')
    ]
    
    for amount, from_curr, to_curr in test_conversions:
        result = converter.convert(amount, from_curr, to_curr)
        if result:
            print(f"{amount} {from_curr} = {result['converted_amount']} {to_curr}")
    
    # 3. Historical conversion (simulated)
    print("\n3. Historical Conversion (Yesterday):")
    yesterday = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
    result = converter.convert(100, 'USD', 'EUR', yesterday)
    if result:
        print(f"Historical rate on {yesterday}: {result['exchange_rate']}")
        print(f"${result['original_amount']} USD = €{result['converted_amount']} EUR")
    
    # 4. Exchange rate only
    print("\n4. Exchange Rate Lookup:")
    rate = converter.get_exchange_rate('USD', 'GBP')
    print(f"Current USD to GBP rate: {rate}")
    
    # 5. Supported currencies
    print("\n5. Supported Currencies:")
    currencies = converter.get_currency_list()
    print(f"Total: {len(currencies)} currencies")
    print(", ".join(currencies[:10]) + "...")
    
    # 6. Conversion history
    print("\n6. Conversion History:")
    history = converter.get_conversion_history()
    print(f"Recent conversions: {len(history)}")
    for i, record in enumerate(history[-3:], 1):
        print(f"  {i}. {record['original_amount']} {record['from_currency']} -> "
              f"{record['converted_amount']} {record['to_currency']}")

if __name__ == "__main__":
    demo()