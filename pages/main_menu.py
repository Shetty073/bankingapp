from tkinter import ttk
import tkinter
from helpers.balance import get_balance
from helpers.deposit import deposit_amount
from helpers.transact import download_transactions, get_transactions
from helpers.withdraw import withdraw_amount


def main_menu(window, last_frame):
    last_frame.destroy()
    main_menu_frame = ttk.Frame(window, padding=10)
    main_menu_frame.grid()

    ttk.Label(main_menu_frame, text="Main Menu", foreground="blue", font=("Arial", 25), anchor="w").grid(column=0, row=0)
    ttk.Label(main_menu_frame, text="Please select any one option:", foreground="blue", font=("Arial", 18), anchor="w").grid(column=0, row=1)

    # Menu options
    ttk.Button(main_menu_frame, text="Check Balance", command=lambda:check_balance(window, main_menu_frame)).grid(column=0, row=2)
    ttk.Button(main_menu_frame, text="Deposit Money", command=lambda:deposit(window, main_menu_frame)).grid(column=0, row=3)
    ttk.Button(main_menu_frame, text="Withdraw Money", command=lambda:withdraw(window, main_menu_frame)).grid(column=0, row=4)
    ttk.Button(main_menu_frame, text="View Transactions", command=lambda:transactions(window, main_menu_frame)).grid(column=0, row=5)
    main_menu_frame.tkraise()


# Pages
# Check Balance page
def check_balance(window, last_frame):
    last_frame.destroy()
    check_balance_frame = ttk.Frame(window, padding=10)
    check_balance_frame.grid()

    balance = get_balance()
    balance = f"Your balance is: ₹{balance}"

    ttk.Label(check_balance_frame, text="Check Balance", foreground="blue", font=("Arial", 25), anchor="w").grid(column=0, row=0)
    ttk.Label(check_balance_frame, text=balance, font=("Arial", 18), anchor="w").grid(column=0, row=1)

    ttk.Button(check_balance_frame, text="Go Back", command=lambda:main_menu(window, check_balance_frame)).grid(column=0, row=2)
    check_balance_frame.tkraise()


# Deposit page
def deposit(window, last_frame):
    last_frame.destroy()
    deposit_frame = ttk.Frame(window, padding=10)
    deposit_frame.grid()

    ttk.Label(deposit_frame, text="Deposit Money", foreground="blue", font=("Arial", 25), anchor="w").grid(column=0, row=0)
    ttk.Label(deposit_frame, text="Enter amount: ").grid(column=0, row=1)

    amount = ttk.Entry(deposit_frame, width=50)
    amount.grid(column=0, row=1)

    ttk.Button(deposit_frame, text="Deposit", command=lambda:deposit_amount(amount.get(), window)).grid(column=0, row=2)

    ttk.Button(deposit_frame, text="Go Back", command=lambda:main_menu(window, deposit_frame)).grid(column=0, row=3)
    deposit_frame.tkraise()


# Withdraw page
def withdraw(window, last_frame):
    last_frame.destroy()
    withdraw_frame = ttk.Frame(window, padding=10)
    withdraw_frame.grid()

    ttk.Label(withdraw_frame, text="Withdraw Money", foreground="blue", font=("Arial", 25), anchor="w").grid(column=0, row=0)
    ttk.Label(withdraw_frame, text="Enter amount: ").grid(column=0, row=1)

    amount = ttk.Entry(withdraw_frame, width=50)
    amount.grid(column=0, row=1)

    ttk.Button(withdraw_frame, text="Withdraw", command=lambda:withdraw_amount(amount.get(), window)).grid(column=0, row=2)

    ttk.Button(withdraw_frame, text="Go Back", command=lambda:main_menu(window, withdraw_frame)).grid(column=0, row=3)
    withdraw_frame.tkraise()


# Transactions page
def transactions(window, last_frame):
    last_frame.destroy()
    transactions_frame = ttk.Frame(window, padding=10)
    transactions_frame.grid()

    ttk.Label(transactions_frame, text="Previous Transactions", foreground="blue", font=("Arial", 25), anchor="w").grid(column=0, row=0)

    transactions = get_transactions()
    i = 1
    for transaction in transactions:
        data = f"#{transaction[0]} - CIF {transaction[1]} {transaction[2]} ₹{transaction[3]} @ {transaction[6]} :: Balance before: ₹{transaction[4]} :: Balance after: ₹{transaction[5]}"
        ttk.Label(transactions_frame, text=data, font=("Arial", 10), anchor="w").grid(column=0, row=i)
        i += 1
        

    ttk.Button(transactions_frame, text="Download", command=download_transactions).grid(column=0, row=i)
    ttk.Button(transactions_frame, text="Go Back", command=lambda:main_menu(window, transactions_frame)).grid(column=0, row=i+1)
    transactions_frame.tkraise()
