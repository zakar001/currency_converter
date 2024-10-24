"""
Main currency converter application with user interface
"""

from currency_api import CurrencyAPI
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

class CurrencyConverter:
    def __init__(self):
        self.api = CurrencyAPI()
        self.common_currencies = ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD', 'CHF', 'CNY', 'INR']
    
    def display_main_menu(self):
        """Display the main menu options"""
        print("\n" + "="*50)
        print("      REAL-TIME CURRENCY CONVERTER")
        print("="*50)
        print("1. Convert Currency")
        print("2. View Real-time Exchange Rates")
        print("3. View Historical Exchange Rates")
        print("4. Exit")
        print("="*50)
    
    def convert_currency_interactive(self):
        """Interactive currency conversion"""
        try:
            amount = float(input("Enter amount to convert: "))
            from_curr = input("Enter source currency (e.g., USD): ").upper()
            to_curr = input("Enter target currency (e.g., EUR): ").upper()
            
            print(f"\nConverting {amount} {from_curr} to {to_curr}...")
            result = self.api.convert_currency(amount, from_curr, to_curr)
            
            if result['success']:
                print(f"\n✓ Conversion Successful!")
                print(f"  {amount} {from_curr} = {result['converted_amount']:.2f} {to_curr}")
                print(f"  Exchange Rate: 1 {from_curr} = {result['exchange_rate']:.4f} {to_curr}")
                print(f"  Last updated: {datetime.fromtimestamp(result['timestamp'])}")
            else:
                print(f"✗ Error: {result['error']}")
                
        except ValueError:
            print("✗ Error: Please enter a valid number for amount")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def view_real_time_rates(self):
        """Display real-time exchange rates"""
        base_currency = input("Enter base currency (default: USD): ").upper() or "USD"
        
        print(f"\nFetching real-time rates for {base_currency}...")
        result = self.api.get_real_time_rates(base_currency)
        
        if result['success']:
            print(f"\n📊 Real-time Exchange Rates (Base: {base_currency})")
            print("-" * 40)
            
            # Display common currencies first
            for currency in self.common_currencies:
                if currency != base_currency and currency in result['rates']:
                    rate = result['rates'][currency]
                    print(f"  {currency}: {rate:.4f}")
            
            print(f"\nLast updated: {datetime.fromtimestamp(result['timestamp'])}")
        else:
            print(f"✗ Error: {result['error']}")
    
    def view_historical_rates(self):
        """Display and plot historical exchange rates"""
        try:
            base_currency = input("Enter base currency (e.g., USD): ").upper()
            target_currency = input("Enter target currency (e.g., EUR): ").upper()
            days = int(input("Enter number of days for history (max 365): ") or "30")
            days = min(days, 365)  # Limit to 1 year
            
            print(f"\nFetching historical data for {days} days...")
            historical_data = self.api.get_historical_rates(base_currency, target_currency, days)
            
            if historical_data:
                # Display recent rates
                print(f"\n📈 Historical Exchange Rates ({base_currency} to {target_currency})")
                print("-" * 50)
                
                # Show last 10 days
                for i, data in enumerate(historical_data[:10]):
                    print(f"  {data['date']}: 1 {base_currency} = {data['rate']:.4f} {target_currency}")
                
                if len(historical_data) > 10:
                    print(f"  ... and {len(historical_data) - 10} more days")
                
                # Plot the data
                self.plot_historical_data(historical_data, base_currency, target_currency)
                
            else:
                print("✗ No historical data available")
                
        except ValueError:
            print("✗ Error: Please enter valid numbers")
        except Exception as e:
            print(f"✗ Error: {e}")
    
    def plot_historical_data(self, historical_data, base_currency, target_currency):
        """Plot historical exchange rate data"""
        try:
            # Prepare data for plotting
            dates = [data['date'] for data in historical_data]
            rates = [data['rate'] for data in historical_data]
            
            # Reverse to show chronological order
            dates.reverse()
            rates.reverse()
            
            plt.figure(figsize=(12, 6))
            plt.plot(dates, rates, marker='o', linewidth=2, markersize=4)
            plt.title(f'Historical Exchange Rate: {base_currency} to {target_currency}')
            plt.xlabel('Date')
            plt.ylabel(f'Exchange Rate ({target_currency})')
            plt.xticks(rotation=45)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()
            
        except ImportError:
            print("Note: matplotlib not available. Install with: pip install matplotlib")
        except Exception as e:
            print(f"Could not display chart: {e}")
    
    def run(self):
        """Main application loop"""
        print("Welcome to Real-time Currency Converter!")
        
        while True:
            self.display_main_menu()
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == '1':
                self.convert_currency_interactive()
            elif choice == '2':
                self.view_real_time_rates()
            elif choice == '3':
                self.view_historical_rates()
            elif choice == '4':
                print("Thank you for using Currency Converter. Goodbye!")
                break
            else:
                print("✗ Invalid choice. Please enter 1-4.")
            
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()