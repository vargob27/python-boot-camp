class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print('Sorry, balance is too low for this transaction')
        return self
    
    def display_user_balance(self):
        print(f'User: {self.name}, balance: ${self.account_balance}')
        return self

def transfer_money(self, other_user, amount):
    if self.account_balance >= amount:
        self.account_balance -= amount
        other_user.account_balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
    else:
        print("Sorry, balance is too low for this transfer")

guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bryce = User("Bryce Vargo", "bryce.vargo@gmail.com")

guido.make_deposit(100).make_deposit(25).make_deposit(500).make_withdrawal(250).display_user_balance()
# guido.make_deposit(25)
# guido.make_deposit(500)
# guido.make_withdrawal(250)
# guido.display_user_balance()

monty.make_deposit(50).make_deposit(10).make_withdrawal(25).make_withdrawal(50).display_user_balance()
# monty.make_deposit(10)
# monty.make_withdrawal(25)
# monty.make_withdrawal(50)
# monty.display_user_balance()

bryce.make_deposit(1000000).make_withdrawal(35000).make_withdrawal(15000).make_withdrawal(75925).display_user_balance()
# bryce.make_withdrawal(35000)
# bryce.make_withdrawal(15000)
# bryce.make_withdrawal(75925)
# bryce.display_user_balance()

transfer_money(guido, bryce, 100)