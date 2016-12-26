from Stock import Stock
from enum import Enum
import time
import datetime

#define class of stockTran
class stockTran(object):
    def __init__(self,Stock,quantity,indicator,price):
        self.Stock = Stock
        self.trndate = datetime.datetime.fromtimestamp(time.time())
        self.quantity = quantity
        self.indicator = indicator
        self.price = price
