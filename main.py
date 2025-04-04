from Bank import Bank

bank = Bank()

user1 = bank.create_user("user1", 50)
user2 = bank.create_user("user2", 20)

print("")
print("")
print("")
print("")


bank.send_money(user1, user2, 20)
bank.send_money(user2, user1, 20)
bank.send_money(user2, user1, 20)

print(bank.find_transactions_by_iban(user2.iban))

# https://github.com/rdbende/Sun-Valley-ttk-theme - for gui
# https://github.com/hoffstadt/DearPyGui
