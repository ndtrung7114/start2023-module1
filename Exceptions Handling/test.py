#1
result = True
while result:
    try:
        num = int(input("Nhập một số nguyên: "))
        result = 10 / num
        print("Kết quả: ", result)
        result = False
    except ZeroDivisionError:
        print("Lỗi: Không thể chia cho 0.")
    except ValueError:
        print("Lỗi: Hãy nhập một số nguyên.")
        
#2
try:
    file = open("tet.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Không tìm thấy file.")

        
#3
try:
    # Thử thực hiện mã có thể gây ra ngoại lệ
    result = 10 / 0
except ZeroDivisionError:
    # Xử lý ngoại lệ loại ZeroDivisionError
    print("Cannot divide by zero!")
finally:
    # Mã trong khối finally luôn được thực hiện
    print("Execution completed.")


