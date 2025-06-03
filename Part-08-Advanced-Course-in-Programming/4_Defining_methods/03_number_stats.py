# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return 0 if not self.numbers else sum(self.numbers)

    def average(self):
        return 0 if not self.numbers else self.get_sum()/self.count_numbers()

print("Please type in integer numbers:")
numbers = NumberStats()
even_numbers = NumberStats()
odd_numbers = NumberStats()
number = 0
while number != -1:
    try:
        number = int(input())
        if number != -1:
            numbers.add_number(number)
            even_numbers.add_number(number) if number % 2 == 0 else odd_numbers.add_number(number)
    except:
        print("Please insert a valid integer")

print(f"Sum of numbers: {numbers.get_sum()}")
print(f"Mean of numbers: {numbers.average():.2f}")
print(f"Sum of even numbers: {even_numbers.get_sum()}")
print(f"Sum of odd numbers: {odd_numbers.get_sum()}")
    


