from customer import Customer
from account import Account
from personal_account import PersonalAccount
from savings_account import SavingsAccount

class Bank:

    def __init__(self, name):
        self.name = name
        self.customer_list = []

    def get_name(self):
        return self.name

    def get_customers(self):
        return self.customer_list

    def get_customers_by_name(self, name):
        customer_name = []
        for customer in self.customer_list:
            if customer.name == name:
                customer_name.append(customer)
        return customer_name

    def get_customer_by_id(self, id):
        for customer in self.customer_list:
            if customer.get_id() == id:
                return customer
        return None

    def add_customer(self, customer):
        if not self.customer_list:
            self.customer_list.append(customer)
        else:
            if customer in self.customer_list:
                pass
            else:
                self.customer_list.append(customer)

    def remove_customer(self, customer):
        if customer in self.customer_list:
            del self.customer_list[customer]
        else:
            pass

    def add_savings_account(self, customer):
        if customer in self.customer_list:
            new = SavingsAccount(customer)
            customer.account_list.append(new)
            return new
        else:
            return None


    def add_personal_account(self, customer):
        if customer in self.customer_list:
            new = PersonalAccount(customer)
            customer.account_list.append(new)
            return new
        else:
            return None

    def get_accounts(self, customer):
        accounts = []
        if customer in self.customer_list:
            if not customer.account_list:
                return accounts
            else:
                return customer.account_list
        else:
            return accounts




