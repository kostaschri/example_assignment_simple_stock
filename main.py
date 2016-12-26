from Stock import Stock
from StockTrade import StockTrade
from StockEnums import SSymbol,SType,TIndicator
import random,decimal

#initialization of stocks in memory
#each stock is represented by a stock object (Stock.py)
stockArray = []
stockArray.append(Stock(SSymbol.TEA.value,SType.Common.value,0,None,100))  
stockArray.append(Stock(SSymbol.POP.value,SType.Common.value,8,None,100)) 
stockArray.append(Stock(SSymbol.ALE.value,SType.Common.value,23,None,60)) 
stockArray.append(Stock(SSymbol.GIN.value,SType.Preferred.value,8,2,100)) 
stockArray.append(Stock(SSymbol.JOE.value,SType.Common.value,13,None,250)) 
#initialization of object that will store the stock trades (is used for the purpose of a.iii a.iv and b section of the assignment )
trades=StockTrade()

#a ,i)For a given stock, given any price as input, calculate the dividend yield
def unit_test_a_i():
    print('unit_test_a_i')
	#test 1
	#given stock: 3rd from stockArray(common type)
	#given price: positive integer
    stock = stockArray[2] 
    price = 10
    Divendyield = stock.calcDivendyield(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))

    #test 2
	#given stock: 4th from stockArray(Preferred type)
	#given price: positive integer
    stock = stockArray[3]
    price = 30
    Divendyield = stock.calcDivendyield(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))

    #test 3
	#given stock: 3rd from stockArray(common type)
	#given price: positive decimal
    stock = stockArray[2] 
    price = 26.783
    Divendyield = stock.calcDivendyield(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))

    #test 4
	#given stock: 4th from stockArray(Preferred type)
	#given price: positive decimal
    stock = stockArray[3]
    price = 110.3427
    Divendyield = stock.calcDivendyield(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))

    #test 5
	#given stock: 4th from stockArray(Preferred type)
	#given price: zero price (this test will have the same result as if the giving stock was of common type)
	#             here an exception will be raised for dividing by zero(we handle this exception by returning inf)
	#             depending on the problem we could be more strict handling this exception
    stock = stockArray[3]
    price = 0
    Divendyield = stock.calcDivendyield(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))

    #test 6
	#given stock: 4th from stockArray(Preferred type)
	#given price: negative decimal
	#             again here depending on the problem we could be more strict handling negative values (for this case we assume it is valid to have a negative price)
    stock = stockArray[3]
    price = -11.27
    Divendyield = stock.calcDivendyield(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))
    print('---------------------------------------------------------------------------')

#a ,ii)For a given stock, given any price as input, calculate the P/E Ratio
def unit_test_a_ii():
    print('unit_test_a_ii')
    
    #test 1
	#given stock: 5th from stockArray(Common type)
	#given price: positive integer
    stock = stockArray[4]
    price = 15
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    #test 2
	#given stock: 1st from stockArray(Common type)
	#given price: positive integer with value that raises exception by zero
    stock = stockArray[0]
    price = 55
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    #test 3
	#given stock: 4th from stockArray(Preferred type)
	#given price: positive integer
    stock = stockArray[3]
    price = 15
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    #test 4
	#given stock: 4th from stockArray(Preferred type)
	#given price: positive decimal
    stock = stockArray[3]
    price = 19.286
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    #test 5
	#given stock: 1st from stockArray(Common type)
	#given price: zero price
	#             here we see an example of 0/inf which produces a result of 0. Denpending on the demands of the problem we can handle the result of this situation
    stock = stockArray[0]
    price = 0
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    #test 6
	#given stock: 4th from stockArray(Preferred type)
	#given price: negative decimal
    stock = stockArray[3]
    price = -43.26
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    #test 7
	#given stock: 1st from stockArray(Common type)
	#given price: negative integer 
    stock = stockArray[0]
    price = -5
    peratio = stock.calcperatio(price)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))

    print('---------------------------------------------------------------------------')

#a ,iii Record a trade, with timestamp, quantity of shares, buy or sell indicator and traded price
def unit_test_a_iii():    
    print('unit_test_a_iii')
    #1 two simple record of 1st stock
    stock = stockArray[0]
    quantity = 10
    indicator = TIndicator.BUY.value;
    price = 5
    trades.recordTrade(stock,quantity,indicator,price)

    quantity = 3
    indicator = TIndicator.BUY.value;
    price = 2
    trades.recordTrade(stock,quantity,indicator,price)    
    
    print('Recorded 2 Trades ')    
    print('---------------------------------------------------------------------------')

def unit_test_a_iii_stress_test(cnt):
    print('unit_test_a_iii_stress_test')
    #stress test (we will insert cnt trades of the stocks (randomly of the 5 we have) 
    for i in range(1,cnt+1):
        stock = stockArray[random.randint(0, 4)] #random selection of the 5 stocks
        quantity = random.randint(1, 70000) #random integer quantity and positive
        indicator = random.randint(TIndicator.BUY.value,TIndicator.SELL.value)
        price = decimal.Decimal('%d.%d' % (random.randint(1,9999),random.randint(1,999999))) #random non-zero positive prices
        trades.recordTrade(stock,quantity,indicator,price)
    print('Recorded {0} Trades'.format(cnt))
    print('---------------------------------------------------------------------------')

#a ,iv Calculate Volume Weighted Stock Price based on trades in past 15 minutes
def unit_test_a_iv():
    print('unit_test_a_iv')
	#calc Weighted Stock Price for 1st stock
    stock = stockArray[0]
    volumeweightedprice = trades.getVolWeightedStockPrice(stock)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,Volume Weighted Stock Price: {0}'.format(volumeweightedprice))

    #calc Weighted Stock Price for 2nd stock
    stock = stockArray[1]
    volumeweightedprice = trades.getVolWeightedStockPrice(stock)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,Volume Weighted Stock Price: {0}'.format(volumeweightedprice))

    #calc Weighted Stock Price for 3rd stock
    stock = stockArray[2]
    volumeweightedprice = trades.getVolWeightedStockPrice(stock)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,Volume Weighted Stock Price: {0}'.format(volumeweightedprice))

    #calc Weighted Stock Price for 4th stock
    stock = stockArray[3]
    volumeweightedprice = trades.getVolWeightedStockPrice(stock)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,Volume Weighted Stock Price: {0}'.format(volumeweightedprice))

    #calc Weighted Stock Price for 5th stock
    stock = stockArray[4]
    volumeweightedprice = trades.getVolWeightedStockPrice(stock)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,Volume Weighted Stock Price: {0}'.format(volumeweightedprice))

    print('---------------------------------------------------------------------------')

#b  Calculate the GBCE All Share Index using the geometric mean of prices for all stocks
def unit_test_b():
    print('unit_test_b')
    for i in range (0,len(stockArray)):
        stock=stockArray[i]  
        geomean=trades.getgeometricmean(stock) 
        print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' geometric mean of stock prices: {0}'.format(geomean))
    print('---------------------------------------------------------------------------')

def unit_tests():
    unit_test_a_i()
    unit_test_a_ii()
    unit_test_a_iii()
    unit_test_a_iii_stress_test(100001)
    unit_test_a_iv()
    unit_test_b()

def calculate_dividend_yield():
    stocknum=input("Select stock (0..4): ")
    stock = stockArray[int(stocknum)]
    price = input("Select price: ")
    Divendyield = stock.calcDivendyield(float(price))
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' , Dividend yield: {0}'.format(Divendyield))

def calculate_peratio():
    stocknum=input("Select stock (0..4): ")
    stock = stockArray[int(stocknum)] 
    price = input("Select price: ")
    peratio = stock.calcperatio(float(price))
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' Input Price: {0}'.format(price)+' ,P/E Ratio: {0}'.format(peratio))
    
def record_trade():
    stocknum=input("Select stock (0..4): ")
    stock = stockArray[int(stocknum)]  
    quantity = input("Select quantity: ")
    indicator = input("Select indicator: BUY={0}".format(TIndicator.BUY.value)+' SELL={0}'.format(TIndicator.SELL.value)+' :')
    price = input("Select price: ")
    trades.recordTrade(stock,float(quantity),int(indicator),float(price) )       
    print('Recorded Trade ')       

def calculate_volume_weighted_stock_price_15min():
    stocknum=input("Select stock (0..4): ")
    stock = stockArray[int(stocknum)]
    volumeweightedprice = trades.getVolWeightedStockPrice(stock)
    print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,Volume Weighted Stock Price: {0}'.format(volumeweightedprice))

def calculate_gbce_all_share_index():
    for i in range (0,len(stockArray)):
        stock=stockArray[i]  
        geomean=trades.getgeometricmean(stock) 
        print('Input Stock: {0}'.format(SSymbol(stock.stockSymbol).name) +' ,geometric mean of stock prices: {0}'.format(geomean))

ans=True
while ans:
    print("""
    1.Calculate the dividend yield.
    2.Calculate the P/E Ratio.
    3.Record a trade
    4.Calculate Volume Weighted Stock Price based on trades in past 15 minutes
    5.Calculate the GBCE All Share Index using the geometric mean of prices for all stocks
    6.Unit Tests
    7.Exit
    """)
    ans=input("Select option: ")
    if ans=="1":
        calculate_dividend_yield()
    elif ans=="2":
        calculate_peratio()
    elif ans=="3":
        record_trade()
    elif ans=="4":
        calculate_volume_weighted_stock_price_15min()
    elif ans=="5":
        calculate_gbce_all_share_index()
    elif ans=="6":
        unit_tests()
    elif ans=="7":
        print("\n Exit!!!") 
        ans = None
    else:
       print("\n Not Valid Option!Try again:")
