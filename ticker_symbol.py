import csv
import pandas as pd


def ticker_symbol(company: str) -> str:
    """
    Returns the ticker symbol of the given company
    """
    with open('listings.csv') as CSV_FILE2:
        stock_data = csv.reader(CSV_FILE2)
        next(stock_data)  # to skip the first row
        for row in stock_data:
            if str(row[1]) == company:
                return str(row[0])
        return ('Company not found')

