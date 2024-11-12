"""
Main currency converter module with real-time conversion and historical data
"""

import requests
import json
from datetime import datetime, timedelta
import sqlite3
from typing import Optional, Dict, List
import time

class CurrencyConverter:
    def __init__(self, api_key: str = None):
        """
        Initialize currency converter with API key for real-time rates
        """
        self.api_key = api_key
        self.base_url = "https://api.exchangerate.host"
        self.db_connection = self._init_database()
        
    def _init_database(self) -> sqlite3.Connection:
        """Initialize SQLite database for caching rates"""
        conn = sqlite3.connect('currency_data.db')
        cursor = conn.cursor()
        
        # Create table for historical rates
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS exchange_rates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                base_currency TEXT NOT NULL,
                target_currency TEXT NOT NULL,
                rate REAL NOT NULL,
                date TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Create table for conversion history
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversion_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                from_currency TEXT NOT NULL,
                to_currency TEXT NOT NULL,
                converted_amount REAL NOT NULL,
                rate REAL NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()
        return conn
    
    def get_real_time_rate(self, from_currency: str, to_currency: str) -> Optional[float]:
        """
        Get real-time exchange rate using exchangerate.host API
        """
        try:
            url = f"{self.base_url}/latest"
            params = {
                'base': from_currency.upper(),
                'symbols': to_currency.upper()
            }
            
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('success', False):
                rate = data['rates'].get(to_currency.upper())
                if rate:
                    self._cache_rate(from_currency, to_currency, rate)
                    return rate
            
            return None
            
        except requests.RequestException as e:
            print(f"Error fetching real-time rate: {e}")
            return self._get_cached_rate(from_currency, to_currency)
    
    def _cache_rate(self, base_currency: str, target_currency: str, rate: float):
        """Cache the exchange rate in database"""
        cursor = self.db_connection.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
            INSERT OR REPLACE INTO exchange_rates 
            (base_currency, target_currency, rate, date)
            VALUES (?, ?, ?, ?)
        ''', (base_currency.upper(), target_currency.upper(), rate, today))
        
        self.db_connection.commit()
    
    def _get_cached_rate(self, base_currency: str, target_currency: str) -> Optional[float]:
        """Get cached exchange rate from database"""
        cursor = self.db_connection.cursor()
        today = datetime.now().strftime('%Y-%m-%d')
        
        cursor.execute('''
            SELECT rate FROM exchange_rates 
            WHERE base_currency = ? AND target_currency = ? AND date = ?
            ORDER BY timestamp DESC LIMIT 1
        ''', (base_currency.upper(), target_currency.upper(), today))
        
        result = cursor.fetchone()
        return result[0] if result else None
    
    def convert_currency(self, amount: float, from_currency: str, to_currency: str) -> Optional[float]:
        """
        Convert currency amount from one currency to another
        """
        rate = self.get_real_time_rate(from_currency, to_currency)
        
        if rate is None:
            print(f"Could not get exchange rate for {from_currency} to {to_currency}")
            return None
        
        converted_amount = amount * rate
        
        # Save conversion to history
        self._save_conversion_history(amount, from_currency, to_currency, converted_amount, rate)
        
        return converted_amount
    
    def _save_conversion_history(self, amount: float, from_currency: str, to_currency: str, 
                               converted_amount: float, rate: float):
        """Save conversion to history table"""
        cursor = self.db_connection.cursor()
        
        cursor.execute('''
            INSERT INTO conversion_history 
            (amount, from_currency, to_currency, converted_amount, rate)
            VALUES (?, ?, ?, ?, ?)
        ''', (amount, from_currency.upper(), to_currency.upper(), converted_amount, rate))
        
        self.db_connection.commit()
    
    def get_historical_rates(self, base_currency: str, target_currency: str, 
                           days: int = 30) -> List[Dict]:
        """
        Get historical exchange rates for the specified period
        """
        historical_data = []
        
        for i in range(days):
            date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
            
            try:
                url = f"{self.base_url}/{date}"
                params = {
                    'base': base_currency.upper(),
                    'symbols': target_currency.upper()
                }
                
                response = requests.get(url, params=params, timeout=10)
                response.raise_for_status()
                
                data = response.json()
                
                if data.get('success', False):
                    rate = data['rates'].get(target_currency.upper())
                    if rate:
                        historical_data.append({
                            'date': date,
                            'rate': rate
                        })
                        
                time.sleep(0.1)  # Rate limiting
                
            except requests.RequestException as e:
                print(f"Error fetching historical data for {date}: {e}")
                continue
        
        return historical_data
    
    def get_conversion_history(self, limit: int = 10) -> List[Dict]:
        """Get recent conversion history"""
        cursor = self.db_connection.cursor()
        
        cursor.execute('''
            SELECT amount, from_currency, to_currency, converted_amount, rate, timestamp
            FROM conversion_history 
            ORDER BY timestamp DESC 
            LIMIT ?
        ''', (limit,))
        
        history = []
        for row in cursor.fetchall():
            history.append({
                'amount': row[0],
                'from_currency': row[1],
                'to_currency': row[2],
                'converted_amount': row[3],
                'rate': row[4],
                'timestamp': row[5]
            })
        
        return history
    
    def close(self):
        """Close database connection"""
        if self.db_connection:
            self.db_connection.close()