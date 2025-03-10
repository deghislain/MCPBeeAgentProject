import streamlit as st
from mcp_bee_agent_tools import StockTools as tool


if __name__ == "__main__":
    symbol = st.text_input(':blue[Enter a stock symbol:]')
    submit_btn = st.button("Submit")
    if symbol and submit_btn:
        income = tool.call_income_statement_info_service(symbol)
        balance = tool.call_balance_sheet_info_service(symbol)
        cash_flow = tool.call_cash_flow_info_service(symbol)
        earnings = tool.call_earnings_info_service(symbol)
        insiders_tx = tool.call_insider_tx_info_service(symbol)
        weekly_adjusted = tool.call_daily_adjusted_info_service(symbol)

