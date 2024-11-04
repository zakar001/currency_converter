"""
Simple test script for the currency converter
"""

from currency_api import CurrencyAPI

def test_basic_functionality():
    """Test basic functionality of the currency converter"""
    api = CurrencyAPI()
    
    print("Testing Currency Converter...")
    print("-" * 30)
    
    # Test real-time rates
    print("1. Testing real-time rates...")
    rates = api.get_real_time_rates("USD")
    if rates['success']:
        print("   ✓ Real-time rates fetched successfully")
        print(f"   Base currency: {rates['base_currency']}")
        print(f"   Number of currencies: {len(rates['rates'])}")
    else:
        print(f"   ✗ Failed: {rates['error']}")
    
    # Test currency conversion
    print("\n2. Testing currency conversion...")
    conversion = api.convert_currency(100, "USD", "EUR")
    if conversion['success']:
        print("   ✓ Currency conversion successful")
        print(f"   100 USD = {conversion['converted_amount']:.2f} EUR")
        print(f"   Exchange rate: {conversion['exchange_rate']:.4f}")
    else:
        print(f"   ✗ Failed: {conversion['error']}")
    
    # Test historical data
    print("\n3. Testing historical data...")
    historical = api.get_historical_rates("USD", "EUR", 7)
    if historical:
        print("   ✓ Historical data fetched successfully")
        print(f"   Retrieved {len(historical)} days of data")
        for data in historical[:3]:  # Show first 3 days
            print(f"     {data['date']}: {data['rate']:.4f}")
    else:
        print("   ✗ No historical data available")
    
    print("\n" + "="*30)
    print("Testing completed!")

if __name__ == "__main__":
    test_basic_functionality()