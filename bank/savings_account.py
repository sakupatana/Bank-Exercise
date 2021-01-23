from account import Account

class SavingsAccount(Account):

    def __init__(self, customer):
        super().__init__(customer)

    def transfer_to(self, account, sum):
        if self.get_customer_by_name() == account.get_customer_by_name():
            if self.balance >= sum:
                self.balance = self.balance - sum
                account.balance = account.balance + sum
                return True
            else:
                return False
        else:
            return False
