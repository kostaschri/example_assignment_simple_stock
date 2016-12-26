#define enum for stock symbol
from enum import Enum
class SSymbol(Enum):
    TEA = 1
    POP = 2
    ALE = 3
    GIN = 4
    JOE = 5


class SType(Enum):
    Common = 1
    Preferred = 2

class TIndicator(Enum):
    BUY = 1
    SELL = 2
    
