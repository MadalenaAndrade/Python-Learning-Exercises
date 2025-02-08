class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros}.{self.__cents:02d} eur"

    def __value(self):
        return self.__euros * 100 + self.__cents

    def __set_value(self, cents: int):
        self.__euros = cents // 100
        self.__cents = cents - self.__euros * 100

    def __eq__(self, another):
        return self.__value() == another.__value()

    def __lt__(self, another):
        return self.__value() < another.__value()

    def __gt__(self, another):
        return self.__value() > another.__value()
    
    def __ne__(self, another):
        return self.__value() != another.__value()

    def __add__(self, another):
        sum = Money(0,0)
        sum.__set_value(self.__value()+another.__value())
        return sum
        
    def __sub__(self, another):
        subtraction = self.__value() - another.__value()
        if subtraction < 0:
            raise ValueError("a negative result if not allowed")
        difference = Money(0,0)
        difference.__set_value(subtraction)
        return difference
        
            
if __name__=="__main__":
    e1 = Money(2, 50)
    e2 = Money(1, 50)

    print(e1-e2)