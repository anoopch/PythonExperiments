import tkinter as tk
from tkinter import messagebox
from gui_tkinter.common_module import validate_field, is_data_in_file, insert_into_file


def get_comma_separated_line():
    return usernameEntry.get() + "," + nameEntry.get() + "," + passwordEntry.get() + "," + confirmPasswordEntry.get() \
           + "," + dateOfBirthEntry.get() + "," + hintQuestionEntry.get() + "," + hintAnswerEntry.get() + "," \
           + checkbox_val


def new_registration():
    if validate_field([nameEntry, usernameEntry, passwordEntry, confirmPasswordEntry, dateOfBirthEntry,
                       hintQuestionEntry, hintAnswerEntry]):
        if is_data_in_file(usernameEntry.get()):
            message_box = tk.messagebox.askquestion('Existing User', 'Do you want to replace the data?', icon='warning')
            if message_box != 'yes':
                tk.messagebox.showinfo('Data mismatch', 'Please enter a new username and try again')
                return
        insert_into_file(get_comma_separated_line())
        messagebox.showinfo("Registration Success", "User successfully registered")
    else:
        messagebox.showerror("Registration Failed", "User Not registered")
    print('validation Completed')


window = tk.Tk()
window.title('Register Account')

tk.Label(window, text="Full Name").grid(column=0, row=0)
nameEntry = tk.Entry()
nameEntry.grid(row=0, column=1)

tk.Label(window, text="Username").grid(column=0, row=1)
usernameEntry = tk.Entry()
usernameEntry.grid(row=1, column=1)

tk.Label(window, text="Password").grid(column=0, row=2)
passwordEntry = tk.Entry()
passwordEntry.grid(row=2, column=1)

tk.Label(window, text="Confirm Password").grid(column=0, row=3)
confirmPasswordEntry = tk.Entry()
confirmPasswordEntry.grid(row=3, column=1)

tk.Label(window, text="Date of Birth").grid(column=0, row=4)
dateOfBirthEntry = tk.Entry()
dateOfBirthEntry.grid(row=4, column=1)

tk.Label(window, text="Hint Question").grid(column=0, row=5)
hintQuestionEntry = tk.Entry()
hintQuestionEntry.grid(row=5, column=1)

tk.Label(window, text="Hint Answer").grid(column=0, row=6)
hintAnswerEntry = tk.Entry()
hintAnswerEntry.grid(row=6, column=1)

checkbox_val = 'No'
promoSubscriptionCheckbutton = tk.Checkbutton(window, compound=tk.CENTER,
                                              text="Subscribe to Newsletter and Promotion Emails.",
                                              variable=checkbox_val)
promoSubscriptionCheckbutton.grid(row=7)

cancelButton = tk.Button(window, text="Cancel", command=window.quit())
cancelButton.grid(row=8, column=0)

registerButton = tk.Button(window, text="Register", command=new_registration)
registerButton.grid(row=8, column=1)

window.mainloop()
