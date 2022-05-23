
from db.db import DbHelper
from helpers.alert import display_alert
from shared import shared


def track_transaction(action, amount, balance_before, balance_after):
    db = DbHelper()
    cursor = db.get_cursor()

    sql = "INSERT INTO transactions (user_cif, action, amount, balance_before, balance_after) VALUES (%s, %s, %s, %s, %s)"
    val = (shared.LOGGED_IN_USER_CIF, action, amount, balance_before, balance_after,)
    cursor.execute(sql, val)
    DbHelper.mydb.commit()
    if cursor.rowcount == None or cursor.rowcount < 1:
        print("Unable to track this transaction")


def get_transactions():
    db = DbHelper()
    cursor = db.get_cursor()

    sql = "SELECT * FROM transactions WHERE user_cif=%s"
    val = (shared.LOGGED_IN_USER_CIF,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    return result
