import tkinter


window = tkinter.Tk()
window.title("Login Form")
window.geometry("300x400")
window.configure(bg="#333333")

#creating Widgets
login_label= tkinter.Label(window, text="Login", bg="#333333", fg="white")
username_label = tkinter.Label(window, text="Username", bg="#333333", fg="white")
username_entry = tkinter.Entry(window)
password_entry = tkinter.Entry(window, show="*")
password_label = tkinter.Label(window, text="Password", bg="#333333", fg="white")
password_button = tkinter.Button(window, text = "Login")

#Placing Widgets on the screen
login_label.grid(row=0, column=0, columnspan=2)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1)
password_button.grid(row=3, column=0, columnspan=2)
window.mainloop()