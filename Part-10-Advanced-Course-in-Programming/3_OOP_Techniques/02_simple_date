# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
    
    def __date_days(self, date):
        month_days = (date.month - 1) * 30
        year_days = (date.year - 1) * 12 * 30

        return date.day + month_days + year_days
    
    def __convert_to_date(self, days):
        year = days // (12 * 30) + 1
        remaining_days = days % (12 * 30)

        month = remaining_days // 30 + 1
        day = remaining_days % 30

        if day == 0:
            day = 30
            month -= 1
            if month == 0:
                month = 12
                year = -1
        
        return SimpleDate(day, month, year)


    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __lt__(self, another):
        return self.__date_days(self) < self.__date_days(another)

    def __gt__(self, another):
        return self.__date_days(self) > self.__date_days(another)

    def __eq__(self, another):
        return self.__date_days(self) == self.__date_days(another)

    def __ne__(self, another):
        return self.__date_days(self) != self.__date_days(another)
    
    def __add__(self, days: int):
        total_days = self.__date_days(self) + days
        return self.__convert_to_date(total_days)

    def __sub__(self, another):
        total_days = self.__date_days(self) - self.__date_days(another)
        return abs(total_days)

if __name__=="__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
