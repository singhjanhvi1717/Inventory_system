#store inventory system naviagtion menu
def main_menu():
    print ("1.Product Managment \n2.Stock Management \n3.Order Management \n4.Sales Management \n5.Exit")
print("\033[1;32;40m     Store Inventory System      \033[0m")
while True:
    print("\033[1;32;40m Choose your desired option : \033[0m")
    main_menu()
    try:
        user_choice=int(input("Enter your desired option :"))
    except ValueError:
        print("Invalid Input, Try Entering a Number (integer value form 1 to 5 )")
        continue
    if user_choice ==1:
        print("\033[0;33;40m Product Managment Selected ...\033[0m")
    elif user_choice ==2:
        print("\033[0;33;40m Stock Management Selected ...\033[0m")
    elif user_choice ==3:
        print("\033[0;33;40m Order Management Selected ...\033[0m")
    elif user_choice ==4:
        print("\033[0;33;40m Sales Management Selected ...\033[0m")
    elif user_choice ==5:
        print("\033[1;31;40m Exiting the program ...\033[0m")
        break
    else :
        print("Invalid Choice, Try Again !!!")
    
