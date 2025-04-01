import random as rnd
import datetime


class User:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        self.iban = name + str(rnd.random())
        self.__logs = dict()

    def set_logs(self, logs):
        self.__logs = logs

    def get_logs(self):
        return self.__logs

    def print_logs(self):
        for i, j in self.get_logs():
            print(f"key {i}: {j}")


class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        return f"Transaction occured at {self.date}. \n Sender IBAN: {self.sender.iban} \n Receiver IBAN: {self.receiver.iban} \n Amount: {self.amount}"


class Bank:
    def __init__(self):
        self.registered_users = []
        self.bank_logs = []

    def send_money(self, sender, receiver, amount):
        # not enoutf money
        if sender.balance < amount:
            print("Not enouth money")
        else:
            # enoutg money
            receiver.balance += amount
            sender.balance -= amount
            self.bank_logs.append(Transaction(sender, receiver, amount))

    def print_bank_logs(self):
        for log in self.bank_logs:
            print(log)
