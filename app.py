from tkinter import *
from tkinter import ttk

from helpers.auth import login


window = Tk()
window.geometry("640x320+0+0")
window.title("Banking App by Vinita")

login_frame = ttk.Frame(window, padding=10)
login_frame.grid()

# This the screen's title
ttk.Label(login_frame, text="Universal Bank - Login", foreground="blue", font=("Arial", 25)).grid(column=1, row=0)

# Username label and its entry box
ttk.Label(login_frame, text="Username: ").grid(column=0, row=1)
uname_entry = ttk.Entry(login_frame, width=50)
uname_entry.grid(column=1, row=1)

# Password label and its entry box
ttk.Label(login_frame, text="Password: ").grid(column=0, row=2)
pass_entry = ttk.Entry(login_frame, width=50)
pass_entry.grid(column=1, row=2)

# Login button, onclick it will call the above defined login() function
ttk.Button(login_frame, text="Login", command=lambda:login(uname_entry, pass_entry, window, login_frame)).grid(column=1, row=3)

window.mainloop()