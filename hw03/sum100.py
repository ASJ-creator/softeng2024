from tkinter import messagebox as msg


# def main():
#     total = 0
#
#     for i in range(1, 101):
#         if is_even():
#             total +=i
#     print(f"1부터 100까지 짝수의 합은 {total}입니다.")
#     return total

even_100 = [i for i in range(1, 101) if i % 2 == 0]
msg.showinfo(title='Result', message=even_100)

if __name__ == '__main__':
    main()