import datetime
import os
import pickle


class User:
    """
    Reprezintă clasa de client al bancii

    Atribute:
        name (str): Numele utilizatorului.
        password (str): Parola utilizatorului.
        balance (float): Soldul curent al contului.
        iban (str): IBAN-ul asociat contului.
        __logs (tuple): Jurnalul tranzacțiilor utilizatorului.
    """

    def __init__(self, name, password, initial_balance):
        """
        Inițializează un obiect de tip User.

        Args:
            name (str): Numele utilizatorului.
            password (str): Parola utilizatorului.
            initial_balance (float): Soldul inițial.
        """
        self.name = name
        self.password = password
        self.balance = initial_balance
        # NOTE: - iban-ul ar trebuii teoretic sa fie o combinatie de elemente ale contului si bancii combinate
        self.iban = name
        self.__logs = tuple()

    def set_logs(self, logs):
        """
        Setează jurnalul de tranzacții.

        Args:
            logs (tuple): Tranzacțiile utilizatorului.
        """
        self.__logs = logs

    def get_logs(self):
        """
        Returnează jurnalul de tranzacții.

        Returns:
            tuple: Lista tranzacțiilor.
        """
        return self.__logs

    def _print_logs(self):
        """
        Afișează în consolă jurnalul de tranzacții.
        - Folosit doar in enviroment de development!
        """
        for i, j in self.get_logs():
            print(f"key {i}: {j}")

    def add_transaction(self, transaction):
        """
        Adaugă o tranzacție în jurnal.
        - Folosit doar in enviroment de development!

        Args:
            transaction (Transaction): Tranzacția de adăugat.
        """
        self.set_logs((*self.get_logs(), transaction))

    def export_acc(self):
        """
        Exportă informațiile contului.

        Returns:
            dict: Dicționar cu datele contului.
        """
        return {
            self.iban,
            (self.name, self.balance, self.get_logs()),
        }

    def __str__(self):
        """
        Returnează o reprezentare string a utilizatorului.

        - Folosit doar in enviroment de development!
        Returns:
            str: Numele utilizatorului.
        """
        # return f"This is {self.name} \n Details: \n Current balance: {self.balance} \n IBAN: {self.iban} \n Password: {self.password}"
        return f"user: {self.name}"


class Transaction:
    """
    Reprezintă o tranzacție bancară intre doi utilizatori.

    Atribute:
        sender (User): Expeditorul.
        receiver (User): Destinatarul.
        amount (float): Suma transferată.
        date (datetime): Data efectuării tranzacției.
    """

    def __init__(self, sender, receiver, amount):
        """
        Inițializează o tranzacție.

        Args:
            sender (User): Expeditorul.
            receiver (User): Destinatarul.
            amount (float): Suma de transferat.
        """
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.date = datetime.datetime.now()

    def __str__(self):
        """
        Returnează o descriere detaliată a tranzacției.
        Functia este folosita si in prezentarea tranzactiilor in UI. O modificare a functie va duce la modificarea prezentarii in lista

        Returns:
            str: Detalii despre tranzacție.
        """
        return f"Transaction occured at {self.date}. \n Sender IBAN: {self.sender.iban} \n Receiver IBAN: {self.receiver.iban} \n Amount: {self.amount}"


class Bank:
    """
    Reprezintă banca și gestionarea utilizatorilor și tranzacțiilor.

    Atribute:
        registered_users (list): Lista utilizatorilor înregistrați.
        bank_logs (list): Lista tranzacțiilor efectuate.
    """

    def __init__(self):
        """
        Inițializează obiectul Bank cu liste initiale goale pentru utilizatori si tranzactii.
        """
        self.registered_users = []
        self.bank_logs = []

        self.retrieve_data()

    def retrieve_data(self, path_to_file="bank storage/"):
        """
        Încarcă datele utilizatorilor și ale tranzacțiilor din fișier.

        Args:
            path_to_file (str): Calea către directorul cu fișierul `bankDetails.txt`.
        """
        try:
            with open(f"{path_to_file}/bankDetails.txt", "rb") as f:
                self.registered_users = pickle.load(f)
                self.bank_logs = pickle.load(f)
        except FileNotFoundError:
            print("the save data file doesn't exist")
            self.save_data()

    def save_data(self, path_to_file="bank storage/"):
        """
        Salvează datele utilizatorilor și ale tranzacțiilor in fișier.

        Args:
            path_to_file (str): Calea către directorul în care se salvează datele.
        """
        try:
            os.makedirs(path_to_file, exist_ok=True)
            with open(f"{path_to_file}/bankDetails.txt", "wb") as f:
                pickle.dump(self.registered_users, f)
                pickle.dump(self.bank_logs, f)
        except FileNotFoundError as err:
            print(f"the bank data doesn't exist\n error:{err}")
        except OSError as err:
            print(f"The data directory already exists\n error:{err}")

    def create_user(self, name, password, initial_deposit):
        """
        Creează un utilizator nou.

        Args:
            name (str): Numele utilizatorului.
            password (str): Parola acestuia.
            initial_deposit (float): Suma inițială.

        Returns:
            User: Utilizatorul creat.
        """
        new_user = User(name, password, initial_deposit)
        self.registered_users.append(new_user)
        return new_user

    def find_user_by_iban(self, iban):
        """
        Caută un utilizator după IBAN.

        - NOTA: Numele de utilizator si IBAN-ul sunt aceleasi
        Args:
            iban (str): IBAN-ul căutat.

        Returns:
            User | None: Utilizatorul găsit sau None dacă nu există.
        """
        for usr in self.registered_users:
            if usr.iban == iban:
                return usr

    def find_user_by_username(self, username):
        """
        Caută un utilizator după nume.

        - NOTA: Numele de utilizator si IBAN-ul sunt aceleasi
        Args:
            username (str): Numele utilizatorului.

        Returns:
            User | None: Utilizatorul găsit sau None.
        """
        for usr in self.registered_users:
            if usr.name == username:
                return usr

    def find_transactions_by_iban(self, iban):
        """
        Găsește toate tranzacțiile în care utilizatorul cu IBAN-ul dat a fost destinatar.

        Args:
            iban (str): IBAN-ul utilizatorului.

        Returns:
            list: Lista tranzacțiilor.
        """
        transactions = list()

        for tran in self.bank_logs:
            if tran.sender.iban == iban:
                transactions.append(tran)

        return transactions

    def send_money(self, sender_iban, receiver_iban, amount):
        """
        Efectuează un transfer de bani între doi utilizatori.

        Args:
            sender_iban (str): IBAN-ul expeditorului.
            receiver_iban (str): IBAN-ul destinatarului.
            amount (float): Suma de transferat.

        Returns:
            bool: True dacă tranzacția a fost realizată cu succes, False în caz contrar.
        """
        sender = self.find_user_by_iban(sender_iban)
        receiver = self.find_user_by_iban(receiver_iban)

        if receiver == None:
            return False, "the account doesn't exist"
        # not enoutf money
        if sender.balance < amount:
            return False, "not enough money to send"
        elif sender == receiver:
            return False, "can't send money to self"
        elif amount <= 0.00:
            return False, "can't send negative money"
        else:
            # enoutg money
            receiver.balance += amount
            sender.balance -= amount
            trans = Transaction(sender, receiver, amount)
            self.bank_logs.append(trans)
            sender.add_transaction(trans)
            receiver.add_transaction(trans)
            return True, "Transfer done"

    def _print_bank_logs(self):
        """
        Afișează toate tranzacțiile înregistrate de bancă.
        - Folosit doar in enviroment de development!

        """
        for log in self.bank_logs:
            print(log)
