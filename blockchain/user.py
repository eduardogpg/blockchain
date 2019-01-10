class User:
    def __init__(self):
        self.amount = 0
        self.generate_keys()

    def generate_keys(self):
        self.public_key = 'xxxx'
        self.private_key = 'yyyy'

    def amount(self):
        pass

    def add_amount(self, amount):
        self.amount += amount
