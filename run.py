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


def menu():

    """
    Provides the customer with a list of products 
    with prices and a specific order index
    """
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

    """
    Get input from the user with product name and price
    Run a wile loop to collect a valid string of data from the user
    The loop repeatedly request data untill it is valid
    """
    
    while True:

        print("Please, select from the list above and type")
        print ("the name of the product and it's price separated by coma")
        print('For example: earrings,12')

        data_str = input("Enter your data here: \n")
        sales_data = data_str.split(",")
        item_name = sales_data[0]
        item_price = sales_data[1]
        print("Your choice is: " + item_name + " for €" + item_price)
        if validate_data(sales_data):
            print('Input is valid!\n')
            break
        
    return sales_data

def validate_data(values):
    """
    Inside the try, we check if number of values provided by user
    match conditions
    Raises ValueError if input didn't meet requirements
    """
    
    try:
        if len(values) > 2:
            raise ValueError(
                f"Exactly 2 values required, you provided {len(values)}"
            )
    except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
            return False

    return True

def update_orders(data):
    """
    Receives a data to be inserted into a worksheet
    Updates a relevant worksheet with data provided
    """
    print('Working on your order...\n')
    orders_to_update = SHEET.worksheet('orders')
    orders_to_update.append_row(data)
    print('Thank you!')
    print('Order taken successfully!\n')

def count_orders_full_sum():
    """
    Count sum of all items in order
    Convert updated data to int
    """
    print("Calculating orders sum...\n")

    orders_values = orders.col_values(2)
   
    int_order_values = [int(x) for x in orders_values]
    
    full_sum = sum(int_order_values)
    print(f'Full sum of your order is {full_sum}')
    return full_sum

def main():
    """
    Run all program functions
    """
    menu()
    data = get_order()
    update_orders(data)
    count_orders_full_sum()


main()
