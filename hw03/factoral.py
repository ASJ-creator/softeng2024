from tkinter import simpledialog
from tkinter import messagebox as msg

from lec01.factoral import factorial



def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n = simpledialog.askstring(title="input", prompt="정수를 입력하세요")
    msg.showinfo(title="result", message=factorial(int(n)))

if __name__ == '__main__':
    main()

