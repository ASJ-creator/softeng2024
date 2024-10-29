from tkinter import simpledialog
from tkinter import messagebox as msg


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def main():
    n = int(simpledialog.askstring(title="input", prompt="숫자를 입력하세요"))

    if is_prime(n):
        msg.showinfo(title="result", message="소수 입니다.")
    else:
        msg.showinfo(title="result", message="소수가 아닙니다.")

if __name__ == '__main__':
    main()
