print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

# pizzas
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

# extra pepperoni
small_pepperoni_price = 2
large_pepperoni_price = 3

# extra cheese
extra_cheese_price = 1

# logic
if size == "S":
    bill = small_pizza_price
elif size == "M":
    bill = medium_pizza_price
elif size == "L":
    bill = large_pizza_price
else:
    print("Invalid size")

# extra toppings

if pepperoni == "Y":
    if size == "S":
        bill = bill + small_pepperoni_price
    else:
        bill = bill + large_pepperoni_price
if extra_cheese == "Y":
    bill = bill + extra_cheese_price

print(f"Your final bill is ${bill}")
