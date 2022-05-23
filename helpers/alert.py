from tkinter import Label, Toplevel

def display_alert(parent, title, message):
    alert= Toplevel(parent)
    alert.geometry("300x100")
    alert.geometry("+%d+%d" % (parent.winfo_rootx()+80,
            parent.winfo_rooty()+60
        )
    )
    alert.title(title)
    label_child= Label(alert, text=message, font=('Helvetica 15'))
    label_child.pack()
    alert.wm_transient(parent)
