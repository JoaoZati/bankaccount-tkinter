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
>>> check = Checking('balance.txt')
>>> check.deposit(100)
>>> print(check.balance)
4600.0
>>> check.transfer(100)
>>> print(check.balance)
4500.0
>>> check.commit()
>>> check_fee = Checking('balance.txt', 100)
>>> check_fee.transfer(1000)
>>> print(check_fee.balance)
3400.0
>>> print(check_fee.type)
checking
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


class Checking(Account):
    """
    One Checking account for transfer money

    :arg filepath: Path that have a text file with a float value
    :arg fee: float, amount of fee that will pey for transfer
    """

    type = 'checking'

    def __init__(self, filepath, fee=0):
        Account.__init__(self, filepath)
        self.fee = fee

    def transfer(self, amount):
        self.balance -= amount + self.fee


if __name__ == '__main__':
    check = Checking('balance.txt')
    print(check.__doc__)
