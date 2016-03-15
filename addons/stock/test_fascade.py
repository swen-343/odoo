from fascade import Fascade

print("This script simulates incoming requests to the Inventory Management system.")
req = Fascade()

while(True):
    option = input("1. Request quantity of Mid-Range phones\n2. Add 1 Mid-Range phone to inventory\n3. Request quantity of batteries in stock\n4. Remove 5 batteries from stock\n5. Quit")
    if option == 1:
        print("In stock: ",req.get_quantity("phone"))
    elif option == 2:
        if req.modify_quantity("phone",1):
            print("Added successfully")
    elif option == 3:
        print("In stock: ",req.get_quantity("battery"))
    elif option == 4:
        if req.modify_quantity("battery",-5):
            print("Removed successfully")
        else:
            print("Insufficient stock")
    else:
        break;