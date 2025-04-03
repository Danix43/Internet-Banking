from Bank import User, Bank
import pickle

bank = Bank()

user1 = bank.create_user("user1", 50)
user2 = bank.create_user("user2", 20)

print("")
print("")
print("")
print("")


bank.send_money(user1, user2, 20)
bank.send_money(user1, user2, 10)

# bank.print_bank_logs()

# print(user1.export_acc())
# print("")
# print(user2.export_acc())

with open("bank_details.pkl", "wb") as f:
    pickle.dump(user1.export_acc(), f)
f.close()

with open("bank_details.pkl", "rb") as f:
    loaded_info = pickle.load(f)
    print(loaded_info)


# bank.send_money(user1, user2, 20)
# bank.send_money(user1, user2, 20)
# bank.send_money(user1, user2, 20)

# bank.print_bank_logs()
