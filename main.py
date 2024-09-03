from person import *
cus = Customer()
sel = Seller()
def login():
    print("Please Login")
    print('\tPress 1 for Customer')
    print('\tPress 2 for Seller')
    choice = int(input())
    if choice == 1:
        email = input('Enter Your Email : ')
        password = input('Enter Your Password : ')

        if email in cus.customers:
            if cus.customers[email] == password:
                print('\tLogin Successful!')
                while True:
                    print('\n\tPress 1 for View Product')
                    print('\tPress 2 for Buy Product')
                    print('\tPress 3 Back to main page')

                    ch = int(input())
                    if ch == 1:
                        print("Products\tPrice\tQuantity")
                        for item in sel.products:
                            print(f'{item.name}\t{item.price}\t{item.quantity}')
                    elif ch == 2:
                        name = input("Enter Product Name: ")
                        quantity = int(input("Enter Product Quantity: "))
                        amount = int(input("Enter Amount: "))
                        cus.buy_product(name, quantity, amount)
                    elif ch == 3:
                        return
                    else:
                        print("Invalid Input")
                    

            else:
                print("\tInvalid Password!")
        else:
            print('User Not found!!')

    elif choice == 2:
        email = input('Enter Your Email : ')
        password = input('Enter Your Password : ')

        if email in sel.sellers:
            if sel.sellers[email] == password:
                print('\tLogin Successful!')
                while True:
                    print('\tPress 1 for Add Products')
                    print('\tPress 2 for Back to main page')
                    ch = int(input())

                    if ch == 1:
                        name = input("Enter Product Name: ")
                        price = int(input("Enter Product Price: "))
                        quantity = int(input("Enter Product Quantity: "))
                        sel.add_product(name, price, quantity)
                        print(f'{name} Added Successfully!!')
                    elif ch == 2:
                        return
                    else:
                        print("\tInvalid Input!!")
            else:
                print("\tInvalid Password!")
        else:
            print('User Not found!!')



while True:
    print('---Main Page---')
    print('\tPress 1 for Sign up as a Customer')
    print('\tPress 2 for Sign up as a Seller')
    print('\tPress 3 for Login')
    print('\tPress 4 for Exit')

    op = int(input())

    if op == 1:
        email = input('Enter Your Email : ')
        password = input('Enter Your Password : ')
        cus.add_customer(email, password)
        print("\tSign in Successfull!!")
        login()

    elif op == 2:
        email = input('Enter Your Email : ')
        password = input('Enter Your Password : ')
        sel.add_seller(email, password)
        print("\tSign up Successful!!")
        login()

    elif op == 3:
        login()


    elif op == 4:
        break

    else:
        print("Invalid Number!!")