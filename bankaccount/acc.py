"""
Balance shoud start with 4500.0
>>> with open('balance.txt', 'w') as file:
...    file.write(str(4500))
...
4
>>> acc = Account('balance.txt')
>>> print(acc.balance)
4500.0
>>> acc.withdraw(500)
>>> print(acc.balance)
4000.0
>>> acc.commit()
>>> acc = Account('balance.txt')
>>> print(acc.balance)
4000.0
>>> acc.deposit(500)
>>> print(acc.balance)
4500.0
>>> acc.commit()
"""


class Account:

    def __init__(self, filepath):
        self.filepath = filepath

        with open(self.filepath, 'r') as file:
            self.balance = float(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self, path=''):
        if path:
            old_path = self.filepath
            self.filepath = path

        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

        if path:
            self.filepath = old_path
