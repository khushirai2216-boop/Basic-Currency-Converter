"""
Task 5: Currency Converter
Saiket Systems - Python Development Internship
Description: Converts one currency to another currency by taking amount as an input from the user and keeping the base currency as 'USD'.
"""

import requests
from config import APP_ID, BASE_URL

def get_rates():
    url = f"{BASE_URL}?app_id={APP_ID}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data['rates']


def display_currency_list(rates):
    print("="*60)
    print("AVAILABLE CURRENCIES")
    print("="*60)

    currencies = sorted(rates.keys())

    for index, currency in enumerate(currencies, start = 1):
        print(f"{index:3}. {currency}")

    print("="*60)


def currency_converter(amount, from_currency, to_currency, rates):
    
    usd_amount = amount / rates[from_currency]
    
    converted_amount = usd_amount * rates[to_currency]
    
    return converted_amount


def main():
    print("="*60)
    print("REAL-TIME CURRENCY CONVERTER")
    print("="*60)

    try:
        rates = get_rates()

    except Exception as e:
        print(f"Error: {e}")
        return
    
    display_currency_list(rates)

    while True:

        try:
            amount = float(input("Enter the amount: "))

        except ValueError:
            print("Please enter valid numeric amount.")
            continue

        from_currency = input("From Currency: ").upper().strip()

        to_currency = input("To Currency: ").upper().strip()

        if from_currency not in rates:
            print("Invalid Source Currency!")
            continue

        if to_currency not in rates:
            print("Invalid Target Currency!")
            continue

        result = currency_converter(
            amount,
            from_currency,
            to_currency,
            rates
        )    

        print("="*60)
        print(f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
        print("="*60)

        choice = input("Do another conversion? (Y/N) ").upper().strip()

        if choice != 'Y':
            print("\nThank you for using Currency Converter. ")
            break

if __name__ == "__main__":
    main()