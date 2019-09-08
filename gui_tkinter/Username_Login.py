import tkinter as t
from tkinter import messagebox

from quotes import Quotes
from gui_tkinter.common_module import validate_field, is_data_in_file, is_authentication_valid, get_name


def perform_login():
    if validate_field([usernameEntry, passwordEntry]):
        if is_data_in_file(usernameEntry.get()):
            if is_authentication_valid(usernameEntry.get(), passwordEntry.get()):
                quote = Quotes().random()
                messagebox.showinfo('Login successful', 'Welcome {0}'.format(get_name(usernameEntry.get()))
                                    + '\n\nQuote of the Day \n\n\t{0} \n\t\t\t\t- {1}'.format(quote[1], quote[0]))
            else:
                messagebox.showerror('Incorrect Login', 'Invalid login credentials.'
                                                        '\nPlease enter correct username and password')
        else:
            messagebox.showerror('No registered user', 'Sorry No User found with entered username. Register first')
    else:
        messagebox.showerror('Missing required fields', 'Please Enter all fields and try again')


window = t.Tk()
window.title('Register Account')

t.Label(window, text="Username").grid(row=0, column=0)
usernameEntry = t.Entry()
usernameEntry.grid(row=0, column=1)

t.Label(window, text="Password").grid(row=1, column=0)
passwordEntry = t.Entry()
passwordEntry.grid(row=1, column=1)

cancelButton = t.Button(window, text="Register")
cancelButton.grid(row=2, column=0)

registerButton = t.Button(window, text="Login", command=perform_login)
registerButton.grid(row=2, column=1)

window.mainloop()
