import turtle as t

t.forward(200)
t.left(90)
t.forward(100)
t.left(90)
t.forward(200)
t.left(90)
t.forward(100)
t.exitonclick()


import math

print(math.pi)
print(math.e)

print(math.sqrt(25))

print(math.sin(math.radians(-90)))

import random

# Tạo số ngẫu nhiên từ 0 đến 1
random_num = random.random()

# Tạo số nguyên ngẫu nhiên trong khoảng từ a đến b (bao gồm cả a và b)
random_int = random.randint(1, 10)

# Lựa chọn ngẫu nhiên một phần tử từ một danh sách
fruits = ['apple', 'banana', 'cherry', 'date']
random_fruit = random.choice(fruits)

# Trộn ngẫu nhiên một danh sách
random.shuffle(fruits)

# In kết quả
print("Random number between 0 and 1:", random_num)
print("Random integer between 1 and 10:", random_int)
print("Randomly chosen fruit:", random_fruit)
print("Shuffled fruits:", fruits)


import coffee_shop as cs

# Output the information we know from the module
print("Welcome to", cs.shop_name)
print("Available sizes:", cs.coffee_sizes)
print("Available roasts:", cs.coffee_roasts)

# Get some inputs from the user
order_size = input("What size coffee do you want? ")
order_roast = input("What roast do you want? ")

# Send the order to the coffee shop module
shop_says = cs.order_coffee(order_size, order_roast)
# Print out whatever it gave back to us
print(shop_says)

# See if the user wants to add milk
add_milk_response = input("Do you want to add milk (y/n)? ")
# Convert the response to lowercase, then check for a "yes" answer
if "y" in add_milk_response.lower():
    milk_fat = input("What percent milk do you want added? ")
    shop_says = cs.add_milk_please(milk_fat)
    # Print out whatever it gave back to us
    print(shop_says)

# They better give a tip...
print("THAT'S GOOD COFFEE!  Very good.  Your brain is working again.")
print("You better give a tip.")
tip_amount = input("Tip amount? ")
cs.give_tip(tip_amount)

