def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n =12
    print(f"{n}! = {factorial(n)} 입니다.")

if __name__ == '__main__':
    main()
