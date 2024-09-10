from lec01.prime_number import is_prime


def main():
    n=50
    primes = []
    for i in range(2,n + 1):
        if is_prime(i):
            primes.append(i)
    print(primes)

if __name__ == "__main__":
    main()
