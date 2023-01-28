"""
Imported libraries and constant variables were written as in the Love Sandwiches project of Code Institute
"""

import gspread
from google.oauth2.service_account import Credentials
from tabulate import tabulate


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('online_shop_for_storehouse')

orders = SHEET.worksheet('orders')

prices = SHEET.worksheet('prices')

item_name = ""
column_product = []


def menu():

    """
    Provides the customer with a list of products 
    with prices and a specific order index
    """
    global column_product
    print('Welcome to automatic order system!')
    print('What would you like to order?')

    column_prices = prices.col_values(2)
    column_product = prices.col_values(1)

    list_for_customer = list(zip(column_product, column_prices))
    table_for_customer = tabulate((list_for_customer), headers=['Product', 'Price'])
    print("")
    print(table_for_customer)
    print("")
    
    return table_for_customer


def get_order():
    global item_name

    print("Please, select from the list above")
    print ("and type the name of the product and it's price separated by coma")
    print('For example: earrings,12')
    data_str = input("Enter your data here: \n")
    
    
    sales_data = data_str.split(",")
    item_name = sales_data[0]
    item_price = float(sales_data[1])
    print("Your choise is: " + item_name + " for €" + str(item_price))
    if validate_data(sales_data):
        print('Data is valid!')

    print('Thank you!')

    return sales_data

def validate_data(sales_data):
    """
    Inside the try, we check if the name of the product that user
    put to console match products in the list.
    Raises ValueError if there is no match.
    """
    global item_name
    global column_product



    try:
        if item_name not in column_product:
             raise ValueError(
                "Sorry, this product is not in the list."
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")

        return False

    return True




def main():
    """
    Run all program functions
    """
    menu()
    validate_data(get_order())
    validate_data(menu())


main()