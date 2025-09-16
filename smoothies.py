# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")

# TODO: Ask the user for their name using input()
name = input("What's your name? ")

# TODO: Ask how many smoothies they want to buy
quantity = input("How many smoothies would you like to buy?")

# TODO: Convert the number of smoothies to an integer
int(quantity)

# TODO: Calculate the total cost (each smoothie costs £3.50)
cost = quantity * 3.5

# TODO: Display a message using a formatted string
print("Order total:")
print(f"Customer name: {name}")
print(f"Smoothie ({quantity})")
print(f"The total cost is £{float(cost)}")

# OPTIONAL CHALLENGE:
# Ask if the customer wants a reusable cup for £1.00 extra
# Add the cost if they say yes
extra = input("Would you like a reusable cup for £1.00 extra?")
if(extra == "yes"):
    cost += 1
    print(f"The new total cost is £{float(cost)}")
