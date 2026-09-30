inventory = {}

while True:
    command = input("Enter a command (add/sell/search/show/save/report/exit): ")
    if command == "add":
        name = input("Enter the item name: ")
        count = int(input("Enter the item count: "))
        if name in inventory:
            inventory[name] = inventory[name] + count
        else:
            inventory[name] = count
        print("Item stock added.")
    elif command == "sell":
        name = input("Enter the item name: ")
        count = int(input("Enter the sell count: "))

        if name not in inventory:
            print("This item is not in the inventory.")
        elif count > inventory[name]:
            print("Not enough stock.")
        else:
            inventory[name] = inventory[name] - count
            if inventory[name] == 0:
                del inventory[name]
                print(
                    "Item stock reached zero and the item was removed from inventory."
                )
            else:
                print("Sale completed successfully.")

    elif command == "search":
        name = input("Enter the item name: ")
        if name in inventory:
            print("Stock of", name, ":", inventory[name])
        else:
            print("This item is not in the inventory.")
    elif command == "show":
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("Items in inventory:")
            for name in inventory:
                print(name, "-", inventory[name])
    elif command == "save":
        file = open("inventory.txt", "w")
        for name in inventory:
            file.write(name + " - " + str(inventory[name]) + "\n")
        file.close()
        print("Inventory data saved.")
    elif command == "report":
        if len(inventory) == 0:
            print("Inventory is empty.")

        else:
            total_items = len(inventory)
            total_inventory = 0
            max_name = ""
            min_name = ""
            max_count = -1
            min_count = 999999999
            for name in inventory:
                count = inventory[name]
                total_inventory = total_inventory + count
                if count > max_count:
                    max_count = count
                    max_name = name
                if count < min_count:
                    min_count = count
                    min_name = name
            print("Number of item types in inventory:", total_items)
            print("Total stock of all items:", total_inventory)
            print("Item with the most stock:", max_name, "-", max_count)
            print("Item with the least stock:", min_name, "-", min_count)

    elif command == "exit":
        print("Program ended.")
        break
    else:
        print("Invalid command.")
