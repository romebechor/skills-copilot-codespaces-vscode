import sqlite3 as sq
import yfinance as yf 
from model import *
from tabulate import tabulate
import matplotlib.pyplot as plt

def main():
    adapter=dbadapter()
    #adapter.createdb("transactions")
   # adapter.buy()
    trans=adapter.read()
 #   print("Transactions:",trans)
    headers= ['ID','Date','Amount','Description']
    #סוג של לולאה list coprehation
    table_date- [(t['id'],t['date'],t['amount'],t['description']) for t in trans]
    #display the table 
    print(tabulate(table_date,headers=headers,tabledmt='grid'))

    amounts= [t['amount'] for t in trans]
    descriptions = [t['description'] for t in trans]

    plt.figure(figsize=(7,7))
    plt.pie(amounts,labels=descriptions, autopct='%1.1f%%', startangle=90)
    plt.title("Transaction Amount Distribution")
    plt.show()  # Display the pie chart



    data= yf.download("MSFT")
    print(data.info())


if __name__ == "__main__":
    main()
