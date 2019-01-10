from datetime import datetime

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = datetime.now

    def to_hash(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': str(self.timestamp),
        }

    def to_string(self):
        return str(self.to_hash()).encode()
