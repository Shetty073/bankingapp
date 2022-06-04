
import os
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


def download_transactions():
    transactions = get_transactions()
    file = f"{os.getcwd()}/transactions.txt"

    with open(file, "w", encoding="utf-8") as file:
        data = ""
        i = 1
        for transaction in transactions:
            data += f"#{transaction[0]} - CIF {transaction[1]} {transaction[2]} ₹{transaction[3]} @ {transaction[6]} :: Balance before: ₹{transaction[4]} :: Balance after: ₹{transaction[5]}\n"
            i += 1
        file.write(data)
