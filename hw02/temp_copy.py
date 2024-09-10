def f2c(temp_f: float) -> float:
    return (temp_f - 32) * 5 / 9

def main():
    temp_f = 75
    temp_c = f2c(temp_f)
    print(f"{temp_f}F => {temp_c:.1f}C")

    pass

if __name__ == '__main__':
    main()
