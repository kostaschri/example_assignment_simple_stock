from StockEnums import SSymbol,SType
#define class of Stock
class Stock(object):
    def __init__(self, stockSymbol,Type,lastDividend,fixedDividend,parValue):
        self.stockSymbol = stockSymbol
        self.Type = Type    
        self.lastDividend = lastDividend    
        self.fixedDividend = fixedDividend    
        self.parValue = parValue
        self.flagprice = 1 #used for optimization for calculating the geometric mean(check StoreTrade.py for details)
        self.cnt = 0 #also used for optimization for calculating the geometric mean(check StoreTrade.py for details)
        

    #calculate divendyield for a given price
    def calcDivendyield(self,price):  
        try:  	
    	    if SType(self.Type).name=="Common":
    	        return self.lastDividend/price
    	    elif SType(self.Type).name=="Preferred":
    	        return ((self.fixedDividend/100)*self.parValue)/price  
        except ZeroDivisionError:
    	    return float('Inf')
    
    #calculate the P/E Ratio for a given price
    def calcperatio(self,price):
        try:
            return price/self.calcDivendyield(price)     
        except ZeroDivisionError:
            return float('Inf')
