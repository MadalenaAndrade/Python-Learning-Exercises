# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"
    
class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
    
    def weight(self):
        weight = 0
        if self.__items:
            for current_item in self.__items:
                weight += current_item.weight()
        
        return weight

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)

    def print_items(self):
        for item in self.__items:
            print(item)

    def heaviest_item(self):
        if not self.__items:
            return None
        
        heaviest = self.__items[0]
        for item in self.__items:
            if item.weight() > heaviest.weight():
                heaviest = item
        return heaviest

    def __str__(self):
        item_synthax = "item" if len(self.__items) == 1 else "items"
        return f"{len(self.__items)} {item_synthax} ({self.weight()} kg)"

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []

    def weight(self):
        weight = 0
        if self.__suitcases:
            for current_suitcase in self.__suitcases:
                weight += current_suitcase.weight()
        
        return weight
    
    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)

    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

    def __str__(self):
        suitcase_synthax = "suitcase" if len(self.__suitcases) == 1 else "suitcases"
        return f"{len(self.__suitcases)} {suitcase_synthax}, space for {self.__max_weight-self.weight()} kg"

if __name__=="__main__":
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)

    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()
