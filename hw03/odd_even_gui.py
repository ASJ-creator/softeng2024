import tkinter as tk
from tkinter import simpledialog
from lec01.odd_even import is_even

def is_odd(n):
    if n % 2 == 1:
        return n

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = int(simpledialog.askstring("Odd Even Test", "Enter number of odd even test"))

if is_even(USER_INP):
    print(f"{USER_INP} is an even number")
elif is_odd(USER_INP):
    print(f"{USER_INP} is an odd number")
else:
    print(f"{USER_INP} is 0")
