
from db.db import DbHelper
from helpers.alert import display_alert
from pages.main_menu import main_menu
from shared import shared

def login(uname_entry, pass_entry, window, login_frame):
    username = uname_entry.get()
    password = pass_entry.get()

    db = DbHelper()
    cursor = db.get_cursor()
    sql = "SELECT cif, username, password FROM users WHERE username=%s"
    val = (username, )
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result == None:
        display_alert(window, "Error!", "Invalid credentials")
    else:
        if result[1] == username:
            if result[2] == password:
                shared.LOGGED_IN_USERNAME = username
                shared.LOGGED_IN_USER_CIF = result[0]
                main_menu(window, login_frame)
            else:
                display_alert(window, "Error!", "Invalid credentials")
        else:
            display_alert(window, "Error!", "Invalid credentials")