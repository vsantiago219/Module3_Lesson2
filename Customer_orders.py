def customer_order_information(orders):
    #Gathering order information for customer
    customer_name = input("Enter customer name: ").title()
    product = input("Enter product: ").title()
    quantity = int(input("Enter the quantity: "))

    order = {
        "customer_name": customer_name,
        "product": product,
        "quantity": quantity
    }

    #Changing the tuple to a list and back to a tuple
    all_orders = list(orders)
    all_orders.append(order)
    orders = tuple(all_orders)

    print(f"{customer_name} ordered {quantity} {product}")
    return orders

    
def display_customer_orders(orders):
    #Check if there are orders to display
    if not orders:
        print("No orders to display.")
        return
    #Display each order

    for o in orders:
        print(f"({o['customer_name']}, {o['product']}, {o['quantity']}),")

    
def main():
    orders=()
    while True:
        print("1. Add Customer Order")
        print("2. View All Customer Orders")
        print("3. Exit")
        choice = input("Enter a choice: ")

        if choice == "1":
            orders = customer_order_information(orders) #updates the orders information

        elif choice ==  "2":
            display_customer_orders(orders) #Displays the customer orders

        elif choice == "3":
            print("Exiting Customer Orders")
            break #Exit the program

        else:
            print("Invalid option. Please try again.") #If the incorrect input is added, 

if __name__ == "__main__":
    main()