def main():
    color = "red"
    filename="gugudan.html"
    dan = 5

    with open(filename, "w") as f:
        f.write("<html>\n")
        f.write("<body>\n")
        for i in range(9):
            f.write(f"{dan} X {i+1} = <font color='{color}'>{dan*(i+1)}</font><br>\n")
        f.write("</body>\n")
        f.write("</html>\n")


if __name__ == "__main__":
    main()
