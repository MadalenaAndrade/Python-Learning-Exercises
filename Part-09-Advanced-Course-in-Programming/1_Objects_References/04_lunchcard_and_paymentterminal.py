# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        subtration = self.balance - amount
        if subtration >= 0:
            self.balance = subtration
        return subtration >= 0
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        lunch = 2.5
        # Increase the value of the funds at the terminal by the price of the lunch,
        self.funds += lunch
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        if payment >= lunch:
            self.lunches += 1
            return payment - lunch
        else:
            return payment

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        special_lunch = 4.3
        # Increase the value of the funds at the terminal by the price of the lunch,
        self.funds += special_lunch
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        if payment >= special_lunch:
            self.specials += 1
            return payment - special_lunch
        else:
            return payment

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        lunch = 2.5
        initial_condition = card.balance >= lunch
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if initial_condition:
            card.balance -= lunch
            self.lunches += 1
        return initial_condition

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        special_lunch = 4.3
        initial_condition = card.balance >= special_lunch
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        if initial_condition:
            card.balance -= special_lunch
            self.specials += 1
        return initial_condition

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.balance += amount

if __name__ == "__main__":
    exactum = PaymentTerminal()

    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)

    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")

    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")

    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)