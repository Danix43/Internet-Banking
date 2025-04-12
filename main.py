import dearpygui.dearpygui as dpg
from Bank import Bank

bank = Bank()

user1 = bank.create_user("user1", "password", 50)
user2 = bank.create_user("user2", "password", 20)
bank.send_money(user1, user2, 10)
bank.send_money(user1, user2, 20)
bank.send_money(user2, user1, 10)


def set_user(user):
    dpg.set_value("user_name", user.name)
    dpg.set_value("user_iban", user.iban)
    dpg.set_value("user_balance", user.balance)


def switch_view(view):
    dpg.configure_item("homepage_view", show=(view == "homepage"))
    dpg.configure_item("send_view", show=(view == "send"))
    dpg.configure_item("register_view", show=(view == "register"))
    dpg.configure_item("login_view", show=(view == "login"))


def handle_login_callback():
    username = dpg.get_value("username_input")
    password = dpg.get_value("password_input")

    # find user by username
    user = bank.find_user_by_username(dpg.get_value("username_input"))
    print(f"find user query: {dpg.get_value("username_input")}")
    print(f"{user}")

    if user is not None and user.password == password:
        dpg.configure_item("status_text", default_value="Login successful!", show=True)
        dpg.configure_item("login_window", show=False)
        set_user(user)
        show_main_app()
        switch_view("homepage")
    else:
        dpg.configure_item(
            "status_text", default_value="Invalid username or password", show=True
        )


def handle_register_callback():
    username = dpg.get_value("register_username_input")
    password = dpg.get_value("register_username_input")
    initial_deposit = dpg.get_value("register_initial_deposit")

    if bank.find_user_by_username(username):
        print("user already exists")

    else:
        print("need to register")
        new_user = bank.create_user(
            username, password, initial_deposit if initial_deposit != None else 0.00
        )

        print(bank.registered_users)

        dpg.configure_item("login_window", show=False)
        set_user(new_user)
        show_main_app()
        switch_view("homepage")


def logout_callback():
    dpg.configure_item("main_window", show=False)
    dpg.configure_item("login_window", show=True)
    dpg.set_value("username_input", "")
    dpg.set_value("password_input", "")
    dpg.configure_item("status_text", default_value="", show=False)


def show_main_app():
    dpg.set_value("welcome_text", f"Welcome, {dpg.get_value("user_name")}!")
    dpg.configure_item("main_window", show=True)

    with dpg.group(parent="homepage_view", horizontal=True, horizontal_spacing=30):
        dpg.set_value("balance_text", f"Balance: {dpg.get_value("user_balance")}")
        dpg.set_value("iban_text", f"IBAN: {dpg.get_value("user_iban")}")

        dpg.set_value("details_text", "Transactions list:")

        dpg.configure_item(
            "transactions_list",
            items=bank.find_transactions_by_iban(dpg.get_value("user_iban")),
        )


dpg.create_context()
dpg.create_viewport(
    title="Internet Banking",
    width=600,
    height=400,
    resizable=False,
)
dpg.setup_dearpygui()

with dpg.value_registry():
    dpg.add_string_value(tag="user_name")
    dpg.add_string_value(tag="user_iban")
    dpg.add_double_value(tag="user_balance")
    dpg.add_string_value(tag="user_password")

# login window
with dpg.window(
    label="Login",
    tag="login_window",
    width=600,
    height=400,
    no_close=True,
    no_move=True,
    no_collapse=True,
    no_title_bar=True,
):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Login", callback=lambda: switch_view("login"))
        dpg.add_menu_item(label="Register", callback=lambda: switch_view("register"))

    with dpg.child_window(
        tag="login_view", autosize_x=True, autosize_y=True, border=False
    ):
        dpg.add_text("Username")
        dpg.add_input_text(tag="username_input")

        dpg.add_text("Password")
        dpg.add_input_text(tag="password_input", password=True)

        dpg.add_button(label="Login", callback=handle_login_callback)
        dpg.add_text("", tag="status_text", color=[255, 0, 0], show=False)

    with dpg.child_window(
        tag="register_view", autosize_x=True, autosize_y=True, border=False, show=False
    ):
        dpg.add_text("Username")
        dpg.add_input_text(tag="register_username_input")

        dpg.add_text("Password")
        dpg.add_input_text(tag="register_password_input", password=False)

        dpg.add_text("Initial Deposit")
        dpg.add_input_double(tag="register_initial_balance")

        dpg.add_button(label="Register", callback=handle_register_callback)
        # dpg.add_text("", tag="status_text", color=[255, 0, 0], show=False)


# main window
with dpg.window(
    label="Homepage",
    tag="main_window",
    width=600,
    height=400,
    show=False,
    no_close=True,
    no_move=True,
    no_collapse=True,
    no_title_bar=True,
):
    with dpg.menu_bar():
        dpg.add_menu_item(label="Home", callback=lambda: switch_view("homepage"))
        dpg.add_menu_item(label="Send Money", callback=lambda: switch_view("send"))
        dpg.add_menu_item(label="Logout", callback=logout_callback)

    # homepage view
    with dpg.child_window(
        tag="homepage_view", autosize_x=True, autosize_y=True, border=False
    ):

        with dpg.group(parent="homepage_view", horizontal=True, horizontal_spacing=30):
            with dpg.group():
                dpg.add_text("Those are your details: ")
                dpg.add_text("", tag="welcome_text")
                dpg.add_text("", tag="balance_text")
                dpg.add_text("", tag="iban_text")

            with dpg.group():
                dpg.add_text("", tag="details_text")
                dpg.add_listbox([], tag="transactions_list", num_items=15)

    # send money view
    with dpg.child_window(
        tag="send_view",
        auto_resize_x=True,
        auto_resize_y=True,
        show=False,
        border=False,
    ):
        dpg.add_text("Send money")


dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
