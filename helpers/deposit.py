from helpers.alert import display_alert
from helpers.transact import track_transaction
from shared import shared
from db.db import DbHelper


def deposit_amount(amount, window):
    try:
        amount = float(amount)
    except:
        display_alert(window, "Error", "Amount should be a number")

    db = DbHelper()
    cursor = db.get_cursor()

    sql = "SELECT balance FROM users WHERE username=%s"
    val = (shared.LOGGED_IN_USERNAME, )
    cursor.execute(sql, val)
    result = cursor.fetchone()
    current_balance = float(result[0])
    new_balance = current_balance + amount

    sql = "UPDATE users SET balance=%s WHERE username=%s"
    val = (new_balance, shared.LOGGED_IN_USERNAME, )
    cursor.execute(sql, val)
    DbHelper.mydb.commit()
    if cursor.rowcount == None or cursor.rowcount < 1:
        display_alert(window, "Error", "Unknown error occurred while updating")
    else:
        track_transaction("deposited", amount, current_balance, new_balance)
        display_alert(window, "Success!", "Amount deposited successfully")

