from staff import add_staff
from utils import save_to_json

#empty list
staff = save_to_json("data/staff.json")
devices = save_to_json("data/devices.json")
borrow_records = save_to_json("data/borrow_records.json")

def menu():
    print("\n1. Add Staff")
    print("2. Add Device")
    print("3. Borrow Device")
    print("4. Return Device")
    print("5. EXIT\n")

while True:
    menu()
    user = input("Chouse in a option: ")
    user_input = int(user)

    if user_input == 5:
        print('Thank you for using Smart Inventory CLI!')
        break
    elif user_input == 1:

        print("\nif you want to exit enter \"exit\".")
        name = input("Enter Name: ")
        if name.strip().lower() == "exit":
            continue

        department = input("Enter Department: ")
        if department.strip().lower() == "exit":
            continue

        print("Enter 1 if ACTIVE, 2 if INACTIVE")
        status = input("Enter Number: ")
        if status.strip().lower() == "exit":
            continue


        add_staff(staff, name, department, status)
    elif user_input == 2:
        print(staff)