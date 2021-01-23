# Bank-Exercise
Introduction
The purpose is to revise object-oriented programming by creating a small bank-project. The idea is to create a simple bank with individual customers, and in which currency can be transferred between the accounts of customers.

#Base code
In this exercise, the base code is only the main.py file, which has the purpose of simplyfying the testing of the project. You will have to create the files to be returned from scratch.

#Exercise
Create new files bank.py, customer.py, account.py, personal_account.py and savings_account.py, where you will implement the classes Bank, Customer, Account, PersonalAccount ja SavingsAccount.

Note. In this exercise, there is an older test program that tests the code, and it requires you to name the files as given above. Otherwise the tester will give a false feedback (”There’s no feedback available.”)

You can implement the classes in any way you want, as long as they contain at least the following methods:

#Bank

__init__(name): Creates a new Bank object called name.

get_name(): Returns the name of the bank.

get_customers(): Returns a list which contains all the Customer objects that are currently customers of the bank.

get_customers_by_name(name): Returns a list of Customer objects, with the name given as parameter. If there exists no customers with that name, the method returns an empty list.

get_customer_by_id(id): Return a Customer object with the given id, if there currently exist a customer with that id. If the customer cannot be found, the method returns None.

add_customer(customer): Adds the given Customer object to a customer of the bank. If the person is already a customer of the bank, the method does nothing.

remove_customer(customer): Finds and removes the given Customer object customer from the bank. If the given customer is not found, the method does nothing.

add_savings_account(customer): Adds a new SavingsAccount to the given Customer object customer and returns the added SavingsAccount object. If the given customer is not a customer of the bank, the method return None.

add_personal_account(customer): Adds a new PersonalAccount to the given Customer object customer and returns the added account. If the given customer is not a customer of the bank, the method returns None.

get_accounts(customer): Returns a list of all the accounts of the given Customer object customer. If no account or customer cannot be found, the method returns an empty list.

#Customer

__init__(name): Creates a new Customer object called name.

get_id(): Returns a customer specific id by which the customers can be identified regardless of the names. You are free to choose how you implement this. The id can be any type, for example a string or an integer. The only requirement is that no two customers can have the same id. You can assume here that all the customers are customers of the same bank. Hint: Class variables might be useful.

#Account

Account works as a parent class to different account types like PersonalAccount and SavingsAccount.
Note: To simplify the exercise, the currency in the accounts are handled as integers.
__init__(customer): Creates a new Account object and sets the given Customer object customer to be the owner of this account.

get_customer(): Returns the account owner’s Customer object.

get_balance(): Return an integer telling the account balance.

deposit(sum): Deposits the sum amount of money to the account.

withdraw(sum): Subtracts the sum amount of money from the account, if the account has that much money. Returns True if the subtraction was successful, otherwise False.

transfer_to(account, sum): This method always returns False, and does nothing else. The method will be properly implemented in the subclasses PersonalAccount and SavingsAccount.

#PersonalAccount

PersonalAccount inherits the superclass Account.
transfer_to(account, sum): Transfer the sum amount of money from the PersonalAccount to the given account. The method returns True if the transfer was successful, and False otherwise. The transfer fails also if the account does not have enough money.

#SavingsAccount

SavingsAccount inherits the superclass Account.
transfer_to(account, sum): Transfer the sum amount of money from the account to the account given, but only if the both accounts belong to the same customer. From the SavingsAccount, money cannot be transfered to accounts of other customers, but other customers can transfer money to any other customer’s SavingsAccount. The method returns True if the transfer was successful, and False otherwise. The transfer fails also if the account does not have enough money.
