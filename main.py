import dearpygui.dearpygui as dpg
from Bank import Bank

bank = Bank()

user1 = bank.create_user("user1", "password", 50)
user2 = bank.create_user("user2", "password", 20)


def handle_login_callback():
    username = dpg.get_value("username_input")
    password = dpg.get_value("password_input")

    # find user by username
    user = bank.find_user_by_username(username)

    if user is not None and user.password == password:
        dpg.configure_item("status_text", default_value="Login successful!", show=True)
        dpg.configure_item("login_window", show=False)
        show_main_app(username)
    else:
        dpg.configure_item(
            "status_text", default_value="Invalid username or password", show=True
        )


def logout_callback():
    dpg.configure_item("main_window", show=False)
    dpg.configure_item("login_window", show=True)
    dpg.set_value("username_input", "")
    dpg.set_value("password_input", "")
    dpg.configure_item("status_text", default_value="", show=False)


def show_main_app(username):
    dpg.set_value("welcome_text", f"Welcome, {username}!")
    dpg.configure_item("main_window", show=True)


dpg.create_context()
dpg.create_viewport(
    title="Internet Banking",
    width=600,
    height=400,
    resizable=False,
)
dpg.setup_dearpygui()

with dpg.window(
    label="Login",
    tag="login_window",
    width=600,
    height=400,
    no_close=True,
    no_move=True,
    no_collapse=True,
):
    dpg.add_text("Username")
    dpg.add_input_text(tag="username_input")

    dpg.add_text("Password")
    dpg.add_input_text(tag="password_input", password=True)

    dpg.add_button(label="Login", callback=handle_login_callback)
    dpg.add_text("", tag="status_text", color=[255, 0, 0], show=False)

with dpg.window(
    label="Homepage",
    tag="main_window",
    width=600,
    height=400,
    show=False,
    no_close=True,
    no_move=True,
    no_collapse=True,
):
    dpg.add_text("", tag="welcome_text")
    dpg.add_button(label="Logout", callback=logout_callback)

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
