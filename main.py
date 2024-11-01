"""
Main entry point for the Currency Converter application
"""

from currency_converter import CurrencyConverter

def main():
    """Main function to start the application"""
    try:
        converter = CurrencyConverter()
        converter.run()
    except KeyboardInterrupt:
        print("\n\nApplication interrupted by user. Goodbye!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()