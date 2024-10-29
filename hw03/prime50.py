from lec01.is_prime import is_prime
from tkinter import simpledialog
from tkinter import messagebox as msg

def main():
    n=int(simpledialog.askstring(title="input", prompt="숫자를 입력하세요"))
    primes = []
    for i in range(2,n + 1):
        if is_prime(i):
            primes.append(i)
    msg.showinfo(title="result", message=primes)

if __name__ == "__main__":
    main()