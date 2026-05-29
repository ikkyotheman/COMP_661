def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print('Invalid decimal value. Please try again.')

def get_quantity():
    while True:
        try:
            quantity = float(input("Enter quantity: "))
            return quantity
        except ValueError:
            print('Invalid decimal value. Please try again.')

def main():
    print('The Total Price Calculator')
    # Get price and quantity
    price = get_price()
    quantity = get_quantity()
    # Calculate total
    total = price * quantity
    # Display results
    print()
    print('Price: ', price)
    print('Quantity: ', quantity)
    print('Total: ', total)

if __name__ == '__main__':
    main()