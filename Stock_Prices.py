import streamlit
import yfinance
import pandas as pd

streamlit.title("Stock Price Application")
streamlit.write("This application can be used to fetch details about any Stock, Cryptocurrency, Index or ETFs you want! ")

tickerSymbol = streamlit.text_input("Enter the Ticker Symbol: ")

tickerData = yfinance.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='1d', start='2008-01-01', end='2023-12-31')

streamlit.line_chart(tickerDf.Close)
streamlit.line_chart(tickerDf.Volume)




