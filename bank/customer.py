import random

class Customer:

    def __init__(self, name):
        self.name = name
        self.id = random.randint(100000, 999999)
        self.account_list = []

    def get_id(self):
        return self.id