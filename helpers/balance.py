
from db.db import DbHelper
from shared import shared


def get_balance():
    db = DbHelper()
    cursor = db.get_cursor()
    sql = "SELECT balance FROM users WHERE username=%s"
    val = (shared.LOGGED_IN_USERNAME, )
    cursor.execute(sql, val)
    result = cursor.fetchone()
    if result == None:
        return 0
    else:
        return float(result[0])
