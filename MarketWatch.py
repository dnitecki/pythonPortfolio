# import needed modules
from tkinter import *

import arrow
from yahoo_fin import stock_info as si

# create a root window hold all widgets
root = Tk()
#specify the title and size of the root window
root.title("U.S. Stock Market Watch")
root.geometry("1100x750")
# create a first label using hte Label() function
label = Label(text="", fg="Blue", font=("Helvetica", 80))
label.pack()
# create a second label
label2 = Label(text="", fg="Red", font=("Helvetica", 60))
label2.pack()
# set up tickers and names
tickers = ['^DJI','^GSPC','AAPL','AMZN','TSLA']
names = ['DOW JONES','S&P500', 'Apple', 'Amazon', 'Tesla']
# set up the oldprice values and price bounds
oldprice=[]
maxprice=[]
minprice=[]
for i in range(5):
    p=round(float(si.get_live_price(tickers[i])),2)
    oldprice.append(p)
    maxprice.append(p*1.05)
    minprice.append(p*0.95)
    if i<=1:
        print(f'The latest value for {names[i]} is {p}!')            
    else:
        print(f'The latest stock price for {names[i]} is ${p}!') 
# define the StockWatch() function
def StockWatch():
    #declare global variables 
    global oldprice
    #obtain live information about the DOW JONES index from Yahoo
    p1=round(float(si.get_live_price("^DJI")),2)
    m1=f'DOW JONES: {p1}'
    #obtain live information about the SP500 index from Yahoo 
    p2=round(float(si.get_live_price("^GSPC")),2)
    m2=f'S&P500: {p2}'      
    #obtain live price information for Apple stock from Yahoo        
    p3=round(float(si.get_live_price("AAPL")),2)
    m3=f'Apple: ${p3}'
    #obtain live price information for Amazon stock from Yahoo                
    p4=round(float(si.get_live_price("AMZN")),2)
    m4=f'Amazon: ${p4}'
    #obtain live price information for Tesla stock from Yahoo                
    p5=round(float(si.get_live_price("TSLA")),2)
    m5=f'Tesla: ${p5}'
    # put the five prices in a list p
    p=[p1,p2,p3,p4,p5]
    #obtain current date and time infomration         
    tdate=arrow.utcnow().format('MMMM DD, YYYY')
    tm=arrow.utcnow().format('hh:mm:ss A')
    #put the date and time information in the first label         
    label.configure(text=tdate+"\n"+tm)
    #put all the five messages on the stock market in the second label        
    label2.configure(text=m1+"\n"+m2+"\n"+m3+"\n"+m4+"\n"+m5, justify=LEFT)
    # if there is update in the marekt, announce it
    for i in range(5):     
        if p[i]!=oldprice[i]:
            oldprice[i]=p[i]
            if i<=1:
                print(f'The latest value for {names[i]} is {p[i]}!')            
            else:
                print(f'The latest stock price for {names[i]} is ${p[i]}!') 
    # if price goes out of bounds, announce it
    for i in range(5):     
        if p[i]>maxprice[i]:
            print(f'{names[i]} has moved above the upper bound!')            
        if p[i]<minprice[i]:
            print(f'{names[i]} has moved below the lower bound!')            
    #call the StockWatch() function after 5000 milliseconds
    root.after(120000, StockWatch)
# call the StockWatch() function
StockWatch()  
# run the game loop
root.mainloop()
