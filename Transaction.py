class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def __str__(self):
        return "{}{}{}".format(self.sender, self.recipient, self.amount)

# t = Transaction("Thang", "Minh", 20)
# print(str(t))