"""
Main currency converter class with real-time and historical conversion capabilities.
"""

from currency_api import CurrencyAPI
from datetime import datetime, timedelta
import json

class CurrencyConverter:
    def __init__(self, api_key=None):
        """
        Initialize the currency converter.
        
        Args:
            api_key (str): Optional API key for enhanced features
        """
        self.api = CurrencyAPI(api_key)
        self.conversion_history = []
        self.max_history_size = 100
    
    def convert(self, amount, from_currency, to_currency, date=None):
        """
        Convert amount from one currency to another.
        
        Args:
            amount (float): Amount to convert
            from_currency (str): Source currency code
            to_currency (str): Target currency code
            date (str): Historical date in YYYY-MM-DD format (None for real-time)
            
        Returns:
            dict: Conversion result with details
        """
        try:
            if date:
                rates_data = self.api.get_historical_rates(from_currency, date)
                conversion_type = "historical"
            else:
                rates_data = self.api.get_real_time_rates(from_currency)
                conversion_type = "real-time"
            
            if not rates_data or to_currency not in rates_data['rates']:
                return None
            
            exchange_rate = rates_data['rates'][to_currency]
            converted_amount = amount * exchange_rate
            
            result = {
                'original_amount': amount,
                'from_currency': from_currency,
                'to_currency': to_currency,
                'exchange_rate': exchange_rate,
                'converted_amount': round(converted_amount, 2),
                'conversion_type': conversion_type,
                'timestamp': datetime.now().isoformat(),
                'rate_date': rates_data.get('date', datetime.now().strftime('%Y-%m-%d'))
            }
            
            # Add to history
            self.conversion_history.append(result)
            if len(self.conversion_history) > self.max_history_size:
                self.conversion_history.pop(0)
            
            return result
            
        except Exception as e:
            print(f"Conversion error: {e}")
            return None
    
    def get_conversion_history(self, limit=10):
        """
        Get recent conversion history.
        
        Args:
            limit (int): Number of recent conversions to return
            
        Returns:
            list: Recent conversion records
        """
        return self.conversion_history[-limit:]
    
    def get_currency_list(self):
        """
        Get list of supported currencies.
        
        Returns:
            list: Supported currency codes
        """
        return self.api.get_supported_currencies()
    
    def get_exchange_rate(self, from_currency, to_currency, date=None):
        """
        Get exchange rate between two currencies.
        
        Args:
            from_currency (str): Source currency
            to_currency (str): Target currency
            date (str): Historical date
            
        Returns:
            float: Exchange rate
        """
        result = self.convert(1, from_currency, to_currency, date)
        return result['exchange_rate'] if result else None
    
    def clear_history(self):
        """Clear conversion history."""
        self.conversion_history.clear()

# Example usage
if __name__ == "__main__":
    converter = CurrencyConverter()
    
    # Real-time conversion
    result = converter.convert(100, 'USD', 'EUR')
    if result:
        print(f"${result['original_amount']} {result['from_currency']} = {result['converted_amount']} {result['to_currency']}")
        print(f"Exchange rate: {result['exchange_rate']}")