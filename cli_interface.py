"""
Command-line interface for the currency converter
"""

import argparse
from currency_converter import CurrencyConverter
from datetime import datetime
import sys

def main():
    parser = argparse.ArgumentParser(description='Real-time Currency Converter')
    parser.add_argument('--amount', type=float, required=True, help='Amount to convert')
    parser.add_argument('--from', dest='from_currency', required=True, help='Source currency code (e.g., USD)')
    parser.add_argument('--to', dest='to_currency', required=True, help='Target currency code (e.g., EUR)')
    parser.add_argument('--historical', action='store_true', help='Show historical data (last 30 days)')
    parser.add_argument('--history', action='store_true', help='Show conversion history')
    
    args = parser.parse_args()
    
    converter = CurrencyConverter()
    
    try:
        if args.history:
            # Show conversion history
            history = converter.get_conversion_history(10)
            print("\n=== Conversion History ===")
            for entry in history:
                print(f"{entry['timestamp']}: {entry['amount']} {entry['from_currency']} -> "
                      f"{entry['converted_amount']:.2f} {entry['to_currency']} (Rate: {entry['rate']:.4f})")
            return
        
        # Perform conversion
        result = converter.convert_currency(args.amount, args.from_currency, args.to_currency)
        
        if result is not None:
            print(f"\n💰 Conversion Result:")
            print(f"{args.amount} {args.from_currency.upper()} = {result:.2f} {args.to_currency.upper()}")
            
            # Get current rate for display
            current_rate = converter.get_real_time_rate(args.from_currency, args.to_currency)
            if current_rate:
                print(f"Current Exchange Rate: 1 {args.from_currency.upper()} = {current_rate:.4f} {args.to_currency.upper()}")
        else:
            print("Error: Could not perform conversion. Please check currency codes.")
            sys.exit(1)
        
        if args.historical:
            # Show historical data
            print(f"\n📊 Historical Rates (Last 30 days) for {args.from_currency.upper()} to {args.to_currency.upper()}:")
            historical_data = converter.get_historical_rates(args.from_currency, args.to_currency)
            
            for data in historical_data[:10]:  # Show first 10 entries
                print(f"  {data['date']}: {data['rate']:.4f}")
            
            if len(historical_data) > 10:
                print(f"  ... and {len(historical_data) - 10} more days")
    
    except KeyboardInterrupt:
        print("\nOperation cancelled by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        converter.close()

if __name__ == "__main__":
    main()