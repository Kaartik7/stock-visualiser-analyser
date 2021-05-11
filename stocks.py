import bs4
import requests
import yfinance as y
import pandas as pd
import altair as alt
from matplotlib import pyplot as plt


def visualise(company):
    """
    Visualises the 5 year stock record of the given company.
    """
    #for i in companies:
    #    data = y.download(i, period='5y')
    #    FD = pd.DataFrame(data, columns=['Date', 'Adj Close'])
    #    plt.plot(FD)
    data = y.download(company, period='5y')
    FD = pd.DataFrame(data, columns=['Date', 'Adj Close'])
    plt.plot(FD)
    plt.xlabel("Year")
    plt.ylabel("Close")
    plt.title("5 year stock visualisation of the companies")
    plt.show()





