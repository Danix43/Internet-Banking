from Bank import User, Bank

user1 = User("user1", 50)
user2 = User("user2", 30)

bank = Bank()

bank.send_money(user1, user2, 20)
bank.send_money(user1, user2, 20)
bank.send_money(user1, user2, 20)

bank.print_bank_logs()
