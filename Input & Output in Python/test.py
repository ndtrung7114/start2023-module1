# 1. Nhập một số từ bàn phím và in.
number = int(input("Nhập một số: "))
print(f"Số bạn vừa nhập là: {number}")

# 2. Nhập một chuỗi và in chuỗi.
string = input("Nhập một chuỗi: ")
print(f"Chuỗi bạn vừa nhập là: {string}")

# 3. Nhập hai số và in tổng của chúng.
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
print(f"Tổng của hai số là: {a + b}")


# 4. Nhập tên của bạn và chào mừng bạn.
name = input("Nhập tên của bạn: ")
print(f"Chào mừng bạn, {name}!")


# 5. Sử dụng print với dấu phân cách và kết thúc khác nhau.
print("Hello", "World", sep=".", end="!\n")

# 6. In nhiều biến với format.
x, y = 5, 10
print("x = {} và y = {}".format(x, y))

# 7. In chuỗi với f-string.
print(f"Giá trị của x và y lần lượt là: {x} và {y}")


# 8. Nhập một danh sách và in nó ra.
list_input = input("Nhập danh sách các số, phân tách bằng dấu phẩy: ").split(",")
print(f"Danh sách bạn nhập là: {list_input}")

# 9. In một dicionary.
dict_example = {"name": "John", "age": 30}
print(dict_example)

# 10. Nhập một tuple và in nó ra.
tuple_input = tuple(input("Nhập một tuple, phân tách bằng dấu phẩy: ").split(","))
print(f"Tuple bạn nhập là: {tuple_input}")


    
# 13. In một chuỗi nhiều dòng.
multi_line_string = """Đây là một
chuỗi có
nhiều dòng
"""
print(multi_line_string)


# 14. Sử dụng input để nhập một mảng số.
array_input = [int(x) for x in input("Nhập một mảng số, phân tách bằng dấu cách: ").split()]
print(f"Mảng số bạn nhập là: {array_input}")


# 15. In ra màn hình bằng end và sep.
print("A", "B", "C", sep="-", end="!!\n")


# 16. Sử dụng input để nhập giá trị boolean.
bool_input = input("Nhập giá trị True hoặc False: ").lower() == "true"
print(f"Giá trị boolean bạn nhập là: {bool_input}")

bool_input = input("Nhập một ký tự hoặc chuỗi: ").isupper()
print(f"Giá trị boolean bạn nhập là: {bool_input}")

# Giải thích về các kiểu dữ liệu trong Python:

# List: Là một tập hợp có thứ tự, có thể thay đổi và có thể chứa các phần tử trùng lặp.
# Được khai báo bằng dấu ngoặc vuông [].

# Tuple: Tương tự như list nhưng không thể thay đổi (immutable) và có thể chứa các phần tử trùng lặp.
# Được khai báo bằng dấu ngoặc đơn ().

# Set: Là một tập hợp không có thứ tự và không chứa các phần tử trùng lặp.
# Được khai báo bằng dấu ngoặc nhọn {} hoặc bằng hàm set().

# Dictionary: Là một tập hợp không có thứ tự nhưng có thể thay đổi. Bao gồm các cặp key-value.
# Khóa phải là duy nhất và không thể thay đổi. Được khai báo bằng dấu ngoặc nhọn {} với cú pháp key: value.