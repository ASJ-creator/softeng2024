from lec01.odd_even  import is_even


def main():
    total = 0

    for i in range(1, 101):
        if is_even(i):
            total +=i
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")

    even_100 = [i for i in range(1, 101) if i % 2 == 0]
    print(even_100)

if __name__ == '__main__':
    main()
