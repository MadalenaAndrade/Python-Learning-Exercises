# I did more than three instances which the exercise explicity said to don't do. This has now been corrected similarly(with some but small differences) to the model solution:
class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    
    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight

class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__packed_items = []
    
    def weight(self):
        present_weight = 0
        for item in self.__packed_items:
            present_weight += item.weight()
        return present_weight
    
    def __str__(self):
        item_term = "s" if len(self.__packed_items) != 1 else ""
        return f"{len(self.__packed_items)} item{item_term} ({self.weight()} kg)"
    
    def add_item(self, item: Item):
        if item.weight() + self.weight() <= self.__max_weight:
            self.__packed_items.append(item)

    def print_items(self):
        for item in self.__packed_items:
            print(item)
    
    def heaviest_item(self): 
        heaviest = 0
        if self.__packed_items == []:
            heaviest_item = None
        else:
            for item in self.__packed_items:
                if item.weight() > heaviest:
                    heaviest = item.weight()
                    heaviest_item = item 
        return heaviest_item

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []
    
    def weight(self):
        current_weight = 0
        for suitcase in self.__suitcases:
            current_weight += suitcase.weight()
        return current_weight

    def __str__(self):
        end_term = "s" if len(self.__suitcases) != 1 else ""
        return f"{len(self.__suitcases)} suitcase{end_term}, space for {self.__max_weight-self.weight()} kg"
    
    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.weight() <= self.__max_weight:
            self.__suitcases.append(suitcase)
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()

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