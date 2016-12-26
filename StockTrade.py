from Stock import Stock
from StockTran import stockTran
import time
import datetime
import decimal

#define class of StockTrade
class StockTrade(object):
    def __init__(self):        
        self.stockrecords=[] #here we will store the trade-object(which will be the transaction row) StockTran.py
        self.movingStocks=[] #here we will store the stocks that have performed a trade (e.g. if stock TEA has been traded 1 milion times there will be one record of stock TEA)
                             #we will be also storing 2 temporary variables(inside the Stock Object flagprice and cnt, see Stock.py) 
                             #flagprice will hold the multiplication of the trade prices every time a trade is performed
                             #cnt will hold the count of transactions made for the specific stock
                             #this is implemented in terms of optimization for section b when we will be calculating the geometric mean of prices of the specific stock
                             #so as to avoid parsing the whole memory table of the trades and direclty have the part p1*p2*...*pn stored in this temporary variable flagprice and the totalcount in cnt
        self.last15minlist=[]#here we will store the trades made in the last 15 minutes.The list will be updated every time we want to calculate the volume weighted stock price
                             #this is done for optimization so as to avoid looping through the whole list of trades and excluding row by row those that are not made the last 15 minutes
                             #in the getVolWeightedStockPrice function we have in commnets how we would scan the list to calculate our result which would be the same but in terms of performance
                             #it would have greater cost

    #record a trade
    def recordTrade(self,Stock,quantity,indicator,price):
        self.stockrecords.append(stockTran(Stock,quantity,indicator,price))
        self.updateStock(Stock,price)

    def getlast15mintrades(self,Stock):
        ttime = datetime.timedelta(minutes=15)
        self.last15minlist=list(filter(lambda x: x.trndate+ttime>=datetime.datetime.fromtimestamp(time.time()),self.stockrecords))#copy from the original trade list those that are performed the last 15 mins
        self.last15minlist=list(filter(lambda x: x.Stock==Stock, self.last15minlist))#keep records of the given Stock


    #update stock info
    def updateStock(self,Stock,price):
        #check if stock is inside the movingStocks list, if not add it and update the flagprice(p1*p2*...*pn) 
        if not any(x == Stock for x in self.movingStocks):
            Stock.cnt = Stock.cnt + 1
            Stock.flagprice = Stock.flagprice*price
            self.movingStocks.append(Stock)
        else:#update the flagprice
            pindex = self.movingStocks.index(Stock)#locate index of given stock
            self.movingStocks[pindex].flagprice = decimal.Decimal(self.movingStocks[pindex].flagprice)*decimal.Decimal(price)
            self.movingStocks[pindex].cnt = self.movingStocks[pindex].cnt+1  

    #Calculate Volume Weighted Stock Price based on trades in past 15 minutes for given stock
    def getVolWeightedStockPrice(self,Stock):
        self.getlast15mintrades(Stock)#refresh the list
        suma = 0
        sumb = 0        
        for i in range (0,len(self.last15minlist)):            
           suma = suma + decimal.Decimal(self.last15minlist[i].price*self.last15minlist[i].quantity)
           sumb = sumb + decimal.Decimal(self.last15minlist[i].quantity)
        try:
            return suma/sumb
        except ZeroDivisionError:
            return float('Inf')
        """ # original way of calculating the weigted stock price by scanning the whole trade dataset(without the temporary list 'last15minlist' of the last 15 minutes data) which would be more inneficient
            # this is why we prefer the solution above
        suma = 0
        sumb = 0
        ttime = datetime.timedelta(minutes=15)
        for i in range (0,len(self.stockrecords)):            
           if (self.stockrecords[i].trndate+ttime >= datetime.datetime.fromtimestamp(time.time())) and (self.stockrecords[i].Stock==Stock):
               suma = suma + (self.stockrecords[i].price*self.stockrecords[i].quantity)
               sumb = sumb + self.stockrecords[i].quantity
        try:
            return suma/sumb
        except ZeroDivisionError:
            return float('Inf')
        """
    #calculate geometric mean of prices of a given stock
    def getgeometricmean(self,Stock):
        try:
            #check if stock is inside the movingStocks list
            if any(x == Stock for x in self.movingStocks):
                pindex = self.movingStocks.index(Stock)#locate index of given stock
                return pow(decimal.Decimal(self.movingStocks[pindex].flagprice),decimal.Decimal(1/self.movingStocks[pindex].cnt))
            else:
                return 0
        except ZeroDivisionError:
            return float('Inf')
            
