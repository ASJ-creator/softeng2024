from tkinter import simpledialog
from tkinter import messagebox as msg

def f2c(f):
    return (int(f)-32)*5/9

def c2f(c):
    return c*9/5+32

def main():
    temp_f = simpledialog.askstring(title="input", prompt="화씨 온도를 입력해주세요")
    temp_c = f2c(temp_f)
    msg.showinfo(title="result", message=temp_c)

    pass

if __name__ == '__main__':
    main()