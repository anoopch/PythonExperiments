import tkinter as t

from gui_tkinter.common_module import validate_field, is_data_in_file, is_authentication_valid


def perform_login():
    if validate_field([usernameEntry, passwordEntry]):
        if is_data_in_file(usernameEntry.get()):
            if is_authentication_valid(usernameEntry.get(), passwordEntry.get()):
                print('Valid login')
            else:
                print('Invalid login credentials')
        else:
            print('User not found. Register first')
    else:
        print('Enter all fields')


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
