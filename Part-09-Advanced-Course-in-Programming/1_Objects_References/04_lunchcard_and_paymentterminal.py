# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if self.balance - amount < 0:
            return False
        self.balance -= amount
        return True

class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        if payment < 2.50:
            return payment
        self.funds += 2.50
        self.lunches += 1

        return payment - 2.50

    def eat_special(self, payment: float):
        if payment < 4.30:
            return payment
        self.funds += 4.30
        self.specials += 1

        return payment - 4.30

    def eat_lunch_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(2.50):
            self.lunches += 1
            return True
        return False

    def eat_special_lunchcard(self, card: LunchCard):
        if card.subtract_from_balance(4.30):
            self.specials += 1
            return True
        return False

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.deposit_money(amount)
        self.funds += amount

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
