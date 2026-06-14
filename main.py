#store inventory system naviagtion menu
while True :
    print("\033[1;32;40m Store Inventory System \033[0m\n")
    print("\033[1;32;40m Choose your desired option :  \033[0m\n")
    print ("1.Product Managment \n2.Stock Management \n3.Order Management \n4.Stock Management \n5.Exit")
    user_choice=int(input("Enter your desired option :"))
    if user_choice ==1 :
        print("Product Managment Selected ...")
    elif user_choice ==2 :
        print("Stock Management Selected ...")
    elif user_choice ==3 :
        print("Order Management Selected ...")
    elif user_choice ==4 :
        print("Stock Management Selected ...")
    elif user_choice ==5 :
        print("Exiting the program ...")
        break
    else :
        print("Invalid Choice, Try Again !!!")
    