def f2c(f):
    return (f-32)*5/9

def c2f(c):
    return c*9/5+32

def main():
    temp_f = 75
    temp_c = f2c(temp_f)
    print(f"temp_f: {temp_f}, temp_c: {temp_c}")

    pass

if __name__ == '__main__':
    main()
