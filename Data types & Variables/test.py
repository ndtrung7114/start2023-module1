# Datatype_Variable.py

# 1. Số nguyên (Integer)
num1 = 10  
# Ví dụ về kiểu int

# 2. Số thực (Float) 
num2 = 10.5
# Ví dụ về kiểu float

# 3. Chuỗi (String)
name = "John" 
# Ví dụ về kiểu string

# 4. Boolean (True/False)
done = True
# Ví dụ về kiểu boolean 

# 5. List - danh sách
nums = [1, 2, 3]
# Ví dụ về kiểu list

# 6. Tuple - tuple
colors = ("red", "green", "blue")  
# Ví dụ về kiểu tuple

# 7. Set - tập hợp  
s = {1, 2, 3}
# Ví dụ về kiểu set 

# 8. Dictionary - từ điển
info = {"name": "John", "age": 30}
# Ví dụ về kiểu dictionary

# 9. Biến toàn cục và biến cục bộ
x = 5 # biến toàn cục

def func():
  y = 10 # biến cục bộ
  print(x)

func()
print(y) # Lỗi vì y là biến cục bộ

# 10. Gán giá trị 
count = 0
count += 1

# 11. Kiểu dữ liệu None
age = None

# 12. Gán nhiều giá trị
a, b, c = 1, 2, 3

# 13. Chuyển đổi kiểu 
n = float(10) 

# 14. Nhập dữ liệu
name = input("Enter your name: ")

# 15. In dữ liệu 
print("Hello", name)

# 16. Ép kiểu 
n = 10
n_str = str(n)

# 17. Kiểm tra kiểu dữ liệu
print(type(name)) 

# 18. Hằng số  
PI = 3.14

# 19. Ký tự đặc biệt
tab = "\t"
new_line = "\n"

# 20. Một số hàm dành cho string
s = "hello"
print(len(s)) # Độ dài 
print(s.upper()) # Viết hoa
print(s.lower()) # Viết thường
print(s.strip()) # Xóa khoảng trắng


# 21. Khai báo list 
items = ["apple", "banana", "orange"]

# 22. Khai báo tuple
colors = ("red", "green", "blue")

# 23. Khai báo set
unique_nums = {1, 2, 3, 2}

# 24. Khai báo dict
info = {"name":"John", "age":30}

# 25. Cộng hai số nguyên 
a = 10
b = 20
sum = a + b

# 26. Nối hai chuỗi
s1 = "Hello"
s2 = "World"
s = s1 + " " + s2

# 27. Lấy phần tử trong list
fruits = ["apple", "banana", "orange"]
first = fruits[0]

# 28. Lấy phần tử trong tuple 
colors = ("red", "green", "blue")
second = colors[1]

# 29. Cập nhật giá trị trong dict
user = {"name":"John", "age": 30}
user["age"] = 31 

# 30. Xóa phần tử khỏi set
s = {1,2,3,4}
s.remove(3)

# 31. Kiểm tra phần tử có trong list hay không
nums = [1, 2, 3]
print(4 in nums) # False

# 32. Độ dài của chuỗi
s = "hello" 
length = len(s)

# 33. Kiểu dữ liệu
pi = 3.14
print(type(pi)) # float

# 34. Ép kiểu 
n = 1 
f = float(n)

# 35. Nhập dữ liệu
name = input("Enter your name: ")

# 36. In dữ liệu
age = 20
print("John is", age, "years old")