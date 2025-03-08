from typing import List, Dict
from stock_service_utils import get_income_statement_keys
import requests
import os

AV_STOCK_API_KEY = os.environ.get('AV_STOCK_API_KEY')


def create_income_statement(stock_data) -> List[Dict]:
    """
    Retrieves income statement for the last consecutive 3 years from a JSON object
    and returns a list of dictionaries representing each year.

    Args:
        stock_data (object): Object containing JSON data with annual reports.

    Returns:
        list: List of dictionaries, each representing an income statement for a year.
    """
    annual_reports = stock_data.json()["annualReports"]

    income_statements = []
    for report in annual_reports[:3]:  # Get the last 3 annual reports
        income_statement = {key: report[key] for key in get_income_statement_keys()}
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
            return create_income_statement(stock_data)

        except Exception as e:
            print(f"Error fetching stock data: {e}")
            return []
