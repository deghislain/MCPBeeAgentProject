import streamlit as st
from mcp_bee_agent_tools import StockTools as tool


if __name__ == "__main__":
    symbol = st.text_input(':blue[Enter a stock symbol:]')
    st.button("Submit")
    if symbol:
        result = tool.call_income_statement_info_service(symbol)
        print(result)
