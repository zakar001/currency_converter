"""
Currency API module for fetching real-time and historical exchange rates
Uses free API from exchangerate-api.com
"""

import requests
import json
from datetime import datetime, timedelta
import time

class CurrencyAPI:
    def __init__(self):
        self.base_url = "https://api.exchangerate-api.com/v4/latest/"
        self.historical_base_url = "https://api.exchangerate.host/"
        
    def get_real_time_rates(self, base_currency="USD"):
        """
        Get real-time exchange rates for a base currency
        """
        try:
            response = requests.get(f"{self.base_url}{base_currency}")
            if response.status_code == 200:
                data = response.json()
                return {
                    'success': True,
                    'base_currency': data['base'],
                    'rates': data['rates'],
                    'timestamp': data['time_last_updated']
                }
            else:
                return {'success': False, 'error': 'API request failed'}
        except Exception as e:
            return {'success': False, 'error': str(e)}
    
    def get_historical_rates(self, base_currency, target_currency, days_back=30):
        """
        Get historical exchange rates for the last N days
        """
        historical_data = []
        
        for i in range(days_back):
            date = datetime.now() - timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            
            try:
                url = f"{self.historical_base_url}{date_str}"
                params = {
                    'base': base_currency,
                    'symbols': target_currency
                }
                
                response = requests.get(url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    if data['success']:
                        rate = data['rates'].get(target_currency)
                        if rate:
                            historical_data.append({
                                'date': date_str,
                                'rate': rate
                            })
                
                # Be nice to the API
                time.sleep(0.1)
                
            except Exception as e:
                print(f"Error fetching data for {date_str}: {e}")
                continue
        
        return historical_data
    
    def convert_currency(self, amount, from_currency, to_currency):
        """
        Convert currency amount from one currency to another
        """
        rates_data = self.get_real_time_rates(from_currency)
        
        if rates_data['success']:
            rate = rates_data['rates'].get(to_currency)
            if rate:
                converted_amount = amount * rate
                return {
                    'success': True,
                    'original_amount': amount,
                    'from_currency': from_currency,
                    'to_currency': to_currency,
                    'converted_amount': converted_amount,
                    'exchange_rate': rate,
                    'timestamp': rates_data['timestamp']
                }
            else:
                return {'success': False, 'error': f"Currency {to_currency} not found"}
        else:
            return {'success': False, 'error': rates_data['error']}