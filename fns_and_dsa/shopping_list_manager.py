shopping_list = []

def display_menu():

    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

while True:
    display_menu()

    choice = input("Enter your choice(1-4): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        shopping_list.append(item)
        print(f"{item} has been added to your list")

    elif choice == '2':
        item = input("Remove an item: ")
        if item in shopping_list:
           shopping_list.remove(item)
           print(f"{item} has been removed")
        else:
            print(f"This {item} is not in the list")

    elif choice == '3':
        if shopping_list:
            print("\nShopping List: ")
            for item in shopping_list:
                print(f"* {item}")
        else:
            print("Your shopping list is empty")

    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again")