from Bank import User, Bank
import pickle

bank = Bank()

user1 = bank.create_user("user1", 50)
user2 = bank.create_user("user2", 20)

print("")
print("")
print("")
print("")

bank.save_users("bank/")

bank.registered_users = []

bank.retrieve_users("bank/")

for usr in bank.registered_users:
    print(usr)

# bank.print_bank_logs()

# print(user1.export_acc())
# print("")
# print(user2.export_acc())


# bank.send_money(user1, user2, 20)
# bank.send_money(user1, user2, 20)
# bank.send_money(user1, user2, 20)

# bank.print_bank_logs()
