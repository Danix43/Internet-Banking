import random as rnd
import datetime
import os
import pickle


class User:
    def __init__(self, name, password, initial_balance):
        self.name = name
        self.password = password
        self.balance = initial_balance
        # self.iban = name + str(rnd.random())
        self.iban = name
        self.__logs = tuple()

    def set_logs(self, logs):
        self.__logs = logs

    def get_logs(self):
        return self.__logs

    def print_logs(self):
        for i, j in self.get_logs():
            print(f"key {i}: {j}")

    def add_transaction(self, transaction):
        self.set_logs((*self.get_logs(), transaction))

    def export_acc(self):
        return {
            self.iban,
            (self.name, self.balance, self.get_logs()),
        }

    def __str__(self):
        return f"This is {self.name} \n Details: \n Current balance: {self.balance} \n IBAN: {self.iban}"


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

    def retrieve_data(self, path_to_file):
        """
        Should read the csv file that contains the user informations and load them into registered users list
        """
        with open(f"{path_to_file}/bankDetails.txt", "rb") as f:
            self.registered_users = pickle.load(f)
            self.bank_logs = pickle.load(f)

    def save_data(self, path_to_file):
        try:
            os.makedirs(path_to_file)
        except OSError:
            print("The data directory already exists")

        with open(f"{path_to_file}/bankDetails.txt", "wb") as f:
            pickle.dump(self.registered_users, f)
            pickle.dump(self.bank_logs, f)

    def create_user(self, name, password, initial_deposit):
        new_user = User(name, password, initial_deposit)
        self.registered_users.append(new_user)
        print(f"Made a new account \n {new_user}")
        return new_user

    def find_user_by_iban(self, iban):
        for usr in self.registered_users:
            if usr.iban == iban:
                print("User found")
                return usr
            else:
                print("User not registered")
                return None

    def find_user_by_username(self, username):
        for usr in self.registered_users:
            if usr.name == username:
                print("User found")
                return usr
            else:
                print("User not registered")
                return None

    def find_transactions_by_iban(self, iban):
        for trans in self.bank_logs:
            if trans.receiver.iban == iban or trans.sender.iban:
                print("Transactions found")
                return trans
            else:
                print("Transactions not found")
                return None

    def send_money(self, sender, receiver, amount):
        # not enoutf money
        if sender.balance < amount:
            print("Not enouth money")
        else:
            # enoutg money
            receiver.balance += amount
            sender.balance -= amount
            trans = Transaction(sender, receiver, amount)
            self.bank_logs.append(trans)
            sender.add_transaction(trans)
            receiver.add_transaction(trans)

    def print_bank_logs(self):
        for log in self.bank_logs:
            print(log)
