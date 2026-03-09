myList = []

print("--- Menu ---")
print("Mayong hapon, Enter a number")

while True:
    print("\n1. Show Users\n2. Add User\n3. Update User\n4. Delete User\n5. Exit.")
    user = input("Enter a number: ")

    match user:
        case "1":
            print(myList)

        case "2":
            name = input("Enter a Username: ")
            myList.append(name)

        case "3":
            old_name = input("Enter username to update: ")
            if old_name in myList:
                new_name = input("Enter new username: ")
                index = myList.index(old_name)
                myList[index] = new_name
                print("User updated")
            else:
                print("User not found.")

        case "4":
            name = input("Enter a username to delete: ")
            if name in myList:
                myList.remove(name)
                print("User deleted")
            else:
                print("User not found")

        case "5":
            print("Exiting program...")
            break
        case _:
            print("Invalid, try again")