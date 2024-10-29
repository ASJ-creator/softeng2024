from tkinter import simpledialog
from tkinter import messagebox as msg

def is_even():
    if n % 2 == 0:
        return n

def main():
    n = int(simpledialog.askstring(title="input", prompt="숫자를 입력하세요"))
    if n % 2 == 0:
        msg.showinfo(title="result", message="짝수 입니다.")
    else:
        msg.showinfo(title="result", message="홀수 입니다.")

if __name__=='__main__':
    main()