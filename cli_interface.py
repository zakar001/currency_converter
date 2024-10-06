"""
Command-line interface for the currency converter tool.
"""

from currency_converter import CurrencyConverter
import argparse
import sys
from datetime import datetime, timedelta

def print_conversion_result(result):
    """Print conversion result in a formatted way."""
    if not result:
        print("Conversion failed. Please check your inputs.")
        return
    
    print("\n" + "="*50)
    print(f"CONVERSION RESULT")
    print("="*50)
    print(f"Amount: {result['original_amount']} {result['from_currency']}")
    print(f"Converted: {result['converted_amount']} {result['to_currency']}")
    print(f"Exchange Rate: 1 {result['from_currency']} = {result['exchange_rate']} {result['to_currency']}")
    print(f"Type: {result['conversion_type'].upper()}")
    print(f"Date: {result['rate_date']}")
    print("="*50)

def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(description='Real-time Currency Converter with Historical Data')
    
    # Main conversion arguments
    parser.add_argument('amount', type=float, nargs='?', help='Amount to convert')
    parser.add_argument('from_currency', type=str.upper, nargs='?', help='Source currency code')
    parser.add_argument('to_currency', type=str.upper, nargs='?', help='Target currency code')
    
    # Optional arguments
    parser.add_argument('--date', '-d', type=str, help='Historical date (YYYY-MM-DD)')
    parser.add_argument('--list-currencies', '-l', action='store_true', help='List supported currencies')
    parser.add_argument('--history', '-H', action='store_true', help='Show conversion history')
    parser.add_argument('--rate', '-r', action='store_true', help='Show exchange rate only')
    parser.add_argument('--clear-history', '-c', action='store_true', help='Clear conversion history')
    
    args = parser.parse_args()
    
    converter = CurrencyConverter()
    
    # List currencies
    if args.list_currencies:
        currencies = converter.get_currency_list()
        print("\nSupported Currencies:")
        print(", ".join(currencies))
        return
    
    # Show history
    if args.history:
        history = converter.get_conversion_history()
        if not history:
            print("No conversion history available.")
            return
        
        print("\nConversion History:")
        print("-" * 60)
        for i, record in enumerate(reversed(history), 1):
            print(f"{i}. {record['original_amount']} {record['from_currency']} -> "
                  f"{record['converted_amount']} {record['to_currency']} "
                  f"(Rate: {record['exchange_rate']}, {record['rate_date']})")
        return
    
    # Clear history
    if args.clear_history:
        converter.clear_history()
        print("Conversion history cleared.")
        return
    
    # Interactive mode if no arguments provided
    if not args.amount or not args.from_currency or not args.to_currency:
        print("Currency Converter - Interactive Mode")
        print("Enter 'quit' to exit\n")
        
        while True:
            try:
                amount = input("Enter amount to convert: ").strip()
                if amount.lower() == 'quit':
                    break
                
                from_curr = input("From currency (e.g., USD): ").strip().upper()
                if from_curr.lower() == 'quit':
                    break
                
                to_curr = input("To currency (e.g., EUR): ").strip().upper()
                if to_curr.lower() == 'quit':
                    break
                
                date_input = input("Historical date (YYYY-MM-DD) or Enter for real-time: ").strip()
                date = date_input if date_input else None
                
                result = converter.convert(float(amount), from_curr, to_curr, date)
                print_conversion_result(result)
                print()
                
            except ValueError:
                print("Invalid input. Please enter numeric amount.")
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
    else:
        # Command-line mode
        result = converter.convert(args.amount, args.from_currency, args.to_currency, args.date)
        
        if args.rate:
            if result:
                print(result['exchange_rate'])
            else:
                print("Failed to get exchange rate")
        else:
            print_conversion_result(result)

if __name__ == "__main__":
    main()