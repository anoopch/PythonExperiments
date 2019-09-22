import tkinter as t
from gui_tkinter.common_module import validate_field
from tkinter import messagebox


def perform_validation():
    if validate_field([first_number_entry, second_number_entry]) and is_data_valid(first_number_entry.get()) \
            and is_data_valid(second_number_entry.get()):
        return True
    else:
        messagebox.showerror("Invalid Input", "Please correct the input\n\n Only integers can be operated")


def is_data_valid(entered_value):
    try:
        int(entered_value)
        return True
    except Exception:
        return False


def perform_addition():
    if perform_validation():
        first_no, second_no = int(first_number_entry.get()), int(second_number_entry.get())
        messagebox.showinfo("Result", "Added result = {0}".format(first_no + second_no))


def perform_subtraction():
    if perform_validation():
        first_no, second_no = int(first_number_entry.get()), int(second_number_entry.get())
        messagebox.showinfo("Result", "Subtraction result = {0}".format(first_no - second_no))


def perform_multiplication():
    if perform_validation():
        first_no, second_no = int(first_number_entry.get()), int(second_number_entry.get())
        messagebox.showinfo("Result", "Multiplication result = {0}".format(first_no * second_no))


def perform_division():
    if perform_validation():
        first_no, second_no = int(first_number_entry.get()), int(second_number_entry.get())
        messagebox.showinfo("Result", "Division result = {0}".format(first_no / second_no))


window = t.Tk()
window.title('Hello Python')
window.geometry("450x200+150+150")

t.Label(window, text="First Number").grid(row=0, column=1)
first_number_entry = t.Entry()
first_number_entry.grid(row=0, column=2)

t.Label(window, text="Second Number").grid(row=1, column=1)
second_number_entry = t.Entry()
second_number_entry.grid(row=1, column=2)

cancelButton = t.Button(window, text="Add", command=perform_addition)
cancelButton.grid(row=2, column=0)

registerButton = t.Button(window, text="Subtract", command=perform_subtraction)
registerButton.grid(row=2, column=1)

registerButton = t.Button(window, text="Divide", command=perform_division)
registerButton.grid(row=2, column=2)

registerButton = t.Button(window, text="Multiply", command=perform_multiplication)
registerButton.grid(row=2, column=3)

window.mainloop()
