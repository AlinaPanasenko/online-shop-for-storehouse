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

    column_prices = prices.col_values(3)
    column_product = prices.col_values(2)
    column_index = prices.col_values(1)

    list_for_customer = list(zip(column_index, column_product, column_prices))
    print(tabulate(list_for_customer))

    return list_for_customer




def get_order():
    print('Please, select from list below and type index to the console.')
    print('For example, A1')

    data_input = input('Enter your order here: \n')

print('Please, make your order')
print('Provide index of the product and quantity, separated by coma')
print('Fpr example: 1,60\n')

data_input = input('Enter your order here: \n')
order_data = data_input.split(',')
order_index = order_data[0]
order_product = order_data[1]


print(order_index)
print(order_product)
print(order_price)


menu()