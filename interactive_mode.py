"""
Interactive mode for the currency converter
"""

from currency_converter import CurrencyConverter
import sys

def interactive_mode():
    """Run currency converter in interactive mode"""
    converter = CurrencyConverter()
    
    print("🎯 Real-time Currency Converter - Interactive Mode")
    print("Type 'quit' to exit, 'history' to see conversion history")
    print("Type 'help' for available commands\n")
    
    while True:
        try:
            user_input = input("💱 Enter conversion (e.g., '100 USD to EUR') or command: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                break
            elif user_input.lower() == 'history':
                show_conversion_history(converter)
                continue
            elif user_input.lower() == 'help':
                show_help()
                continue
            elif user_input.lower() == 'historical':
                show_historical_menu(converter)
                continue
            
            # Parse conversion input
            parts = user_input.split()
            if len(parts) >= 4 and parts[2].lower() == 'to':
                try:
                    amount = float(parts[0])
                    from_currency = parts[1].upper()
                    to_currency = parts[3].upper()
                    
                    result = converter.convert_currency(amount, from_currency, to_currency)
                    
                    if result is not None:
                        rate = converter.get_real_time_rate(from_currency, to_currency)
                        print(f"✅ {amount} {from_currency} = {result:.2f} {to_currency}")
                        print(f"   Exchange Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
                    else:
                        print("❌ Error: Could not perform conversion. Please check currency codes.")
                        
                except ValueError:
                    print("❌ Error: Invalid amount. Please enter a valid number.")
            else:
                print("❌ Invalid format. Use: '100 USD to EUR' or type 'help' for commands")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
    
    converter.close()

def show_conversion_history(converter: CurrencyConverter):
    """Display conversion history"""
    history = converter.get_conversion_history(10)
    if not history:
        print("No conversion history found.")
        return
    
    print("\n📋 Recent Conversion History:")
    print("-" * 60)
    for entry in history:
        print(f"🕒 {entry['timestamp']}")
        print(f"   {entry['amount']} {entry['from_currency']} → "
              f"{entry['converted_amount']:.2f} {entry['to_currency']}")
        print(f"   Rate: {entry['rate']:.4f}")
        print()

def show_historical_menu(converter: CurrencyConverter):
    """Show historical data menu"""
    print("\n📊 Historical Data")
    from_currency = input("Enter base currency (e.g., USD): ").strip().upper()
    to_currency = input("Enter target currency (e.g., EUR): ").strip().upper()
    days = input("Enter number of days (default 30): ").strip()
    
    try:
        days = int(days) if days else 30
        historical_data = converter.get_historical_rates(from_currency, to_currency, days)
        
        if historical_data:
            print(f"\nHistorical Rates for {from_currency} to {to_currency} (Last {days} days):")
            print("-" * 40)
            for data in historical_data:
                print(f"📅 {data['date']}: {data['rate']:.4f}")
        else:
            print("❌ No historical data available for the specified currencies.")
            
    except ValueError:
        print("❌ Invalid number of days.")

def show_help():
    """Display help information"""
    print("""
🆘 Available Commands:
  • '100 USD to EUR'    - Convert 100 US Dollars to Euros
  • 'history'           - Show conversion history
  • 'historical'        - View historical exchange rates
  • 'help'              - Show this help message
  • 'quit' or 'exit'    - Exit the program

💡 Popular Currency Codes:
  USD - US Dollar      EUR - Euro
  GBP - British Pound  JPY - Japanese Yen
  CAD - Canadian Dollar AUD - Australian Dollar
  CHF - Swiss Franc    CNY - Chinese Yuan
  INR - Indian Rupee   BRL - Brazilian Real
    """)

if __name__ == "__main__":
    interactive_mode()