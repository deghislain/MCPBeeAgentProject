from typing import List, Dict
import stock_service_utils as stock_dict_keys
import requests
import os

AV_STOCK_API_KEY = os.environ.get('AV_STOCK_API_KEY')


def get_dictionary_keys(key_type):
    if key_type == 'income_statement':
        return stock_dict_keys.get_income_statement_keys()
    elif key_type == 'balance_sheet':
        return stock_dict_keys.get_balance_sheet_keys()


def parse_stock_data(stock_data, key_type) -> List[Dict]:
    """
    Retrieves stock information for the last consecutive 3 years from a JSON object
    and returns a list of dictionaries representing each year.

    Args:
        stock_data (object): Object containing JSON data with annual reports.
        key_type: The type of key representing a specific type of stock data e.g income statement

    Returns:
        list: List of dictionaries, each representing a specific type of stock data for a year.
    """
    annual_reports = stock_data.json()["annualReports"]

    income_statements = []
    for report in annual_reports[:3]:  # Get the last 3 annual reports
        income_statement = {key: report[key] for key in get_dictionary_keys(key_type)}
        income_statements.append(income_statement)

    return income_statements


class StockTools:
    def call_income_statement_info_service(stock_symbol: str) -> List[Dict]:
        """
           Retrieves the income statements info for a given stock for the last 3 years'

           Args:
               stock_symbol: The stock symbol, e.g., "IBM".

           Returns:
               A set of dictionary containing the income statements info for a given stock for the last 3 years
           """
        print(f"Getting last year net income for {stock_symbol}")
        try:
            stock_url = f"https://www.alphavantage.co/query?function=INCOME_STATEMENT&symbol={stock_symbol}&apikey={AV_STOCK_API_KEY}"
            stock_data = requests.get(stock_url)
            return parse_stock_data(stock_data, 'income_statement')

        except Exception as e:
            print(f"Error fetching stock data: {e}")
            return []

    def call_balance_sheet_info_service(stock_symbol: str) -> List[Dict]:
        """
           Retrieves the balance sheet info for a given stock for the last 3 years'

           Args:
               stock_symbol: The stock symbol, e.g., "IBM".

           Returns:
               A set of dictionary containing the balance sheet info for a given stock for the last 3 years
           """
        print(f"Getting last year net income for {stock_symbol}")
        try:
            stock_url = f"https://www.alphavantage.co/query?function=BALANCE_SHEET&symbol={stock_symbol}&apikey={AV_STOCK_API_KEY}"
            stock_data = requests.get(stock_url)
            return parse_stock_data(stock_data, 'balance_sheet')

        except Exception as e:
            print(f"Error fetching stock data: {e}")
            return []
