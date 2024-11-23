"""
Test script for the currency converter
"""

from currency_converter import CurrencyConverter
import os

def test_currency_converter():
    """Test basic functionality of the currency converter"""
    print("🧪 Testing Currency Converter...")
    
    converter = CurrencyConverter()
    
    try:
        # Test 1: Basic conversion
        print("\n1. Testing basic conversion...")
        result = converter.convert_currency(100, 'USD', 'EUR')
        if result:
            print(f"✅ 100 USD = {result:.2f} EUR")
        else:
            print("❌ Basic conversion failed")
        
        # Test 2: Get real-time rate
        print("\n2. Testing real-time rate...")
        rate = converter.get_real_time_rate('USD', 'EUR')
        if rate:
            print(f"✅ Current USD/EUR rate: {rate:.4f}")
        else:
            print("❌ Real-time rate failed")
        
        # Test 3: Historical data
        print("\n3. Testing historical data (last 7 days)...")
        historical = converter.get_historical_rates('USD', 'EUR', 7)
        if historical:
            print(f"✅ Retrieved {len(historical)} days of historical data")
            for data in historical[:3]:  # Show first 3
                print(f"   {data['date']}: {data['rate']:.4f}")
        else:
            print("❌ Historical data failed")
        
        # Test 4: Conversion history
        print("\n4. Testing conversion history...")
        history = converter.get_conversion_history(5)
        print(f"✅ Conversion history entries: {len(history)}")
        
        print("\n🎉 All tests completed!")
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
    finally:
        converter.close()
        
        # Clean up test database
        if os.path.exists('currency_data.db'):
            os.remove('currency_data.db')

if __name__ == "__main__":
    test_currency_converter()