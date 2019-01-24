import datetime
from collections import OrderedDict

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def to_hash(self):
        return OrderedDict({
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': str(self.timestamp),
        })

    def __str__(self):
        return str(self.to_hash())
