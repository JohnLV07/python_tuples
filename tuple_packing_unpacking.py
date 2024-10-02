#3. Mastering Tuple Packing and Unpacking in Python

'''
Objective: The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python.

Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.

Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple and print the order details in a user-friendly format.
'''

Costco = [ 
    ("Alejandro", ("Chicken Baked", 3)),
    ("Yessica", ("Ice Cream", 1)),
    ("Jonathan", ("Pizza", 3))
]

# Function to view all customer names
def view_name(Costco):
    print("Customer Names:")
    for customer in Costco:
        print(customer[0])  # Print the name (first element in the tuple)

# Function to view product orders for each customer
def product_order(Costco):
    print("Product Orders:")
    for customer in Costco:
        print(f"{customer[0]} ordered {customer[1][0]}")  # Print the product name (second element in the inner tuple)

# Function to view quantities ordered by each customer
def customer_quantity(Costco):
    print("Customer Quantities:")
    for customer in Costco:
        print(f"{customer[0]} ordered {customer[1][1]} items") 

while True:
    print("\nCostco Kiosko")
    print("\n1: View customer's name\n2: View Product order\n3: View Customer quantity\n4: Exit")
    choice = input("Select your choice: ")

    if choice == '1':
        view_name(Costco)

    elif choice == '2':
        product_order(Costco)

    elif choice == '3':
        customer_quantity(Costco)

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice, please try again.")
