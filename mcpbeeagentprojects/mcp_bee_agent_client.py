import streamlit as st
from mcp_bee_agent_tools import StockTools as tool


if __name__ == "__main__":
    symbol = st.text_input(':blue[Enter a stock symbol:]')
    st.button("Submit")
    if symbol:
        result = tool.call_income_statement_info_service(symbol)
        print("***************************************income--", result)
        balance = tool.call_balance_sheet_info_service(symbol)
        print("***************************************balance--", balance)
