from customer import Customer

class Account:

    def __init__(self, customer):
        self.customer = customer
        self.balance = 0

    def get_customer(self):
        return self.customer

    def get_balance(self):
        return self.balance

    def deposit(self, sum):
        self.balance += sum

    def withdraw(self, sum):
        if self.balance >= sum:
            self.balance -= sum
            result = True
        else:
            result = False
        return result

    def transfer_to(self, account, sum):
        return False