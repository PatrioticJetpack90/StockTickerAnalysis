#libraries

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


#Question 1: Use yfinance to Extract Tesla Stock Data

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
tesla_data.head()

#Question 2: Use Webscraping to Extract Tesla Revenue Data

tesla_revenue = tesla.get_revenue_estimate()
tesla_revenue.tail()


#Question 3: Use yfinance to Extract GameStop (GME) Stock Data

gamestop = yf.Ticker("GME")
gme_data = gamestop.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()

#Question 4: Use Webscraping to Extract GME Revenue Data

gme_revenue = gamestop.get_revenue_estimate()
gme_revenue.tail()


#Question 5: Plot Tesla Stock Graph Using make_graph()
def make_graph():
    tesla = yf.Ticker("TSLA")
    tesla_history = tesla.history(period="6mo")

    plt.figure(figsize=(10, 4))
    plt.plot(tesla_history.index, tesla_history['Close'])
    plt.title("Tesla (TSLA) Stock Price - Last 6 Months")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.show()

make_graph()
