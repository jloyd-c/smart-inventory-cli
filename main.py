from staff import add_staff
from devices import add_devices
from utils import load_form_json, save_to_json
from tabulate import tabulate

#empty list
staff = load_form_json("data/staff.json")
devices = load_form_json("data/devices.json")
borrow_records = load_form_json("data/borrow_records.json")

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
        print("Chouse an option!")
        print("1. Add Staff")
        print("2. Show Staff in table")

        staff_action = input("Enter action: ")
        if staff_action.strip().lower() == "exit":
            continue

        if int(staff_action)== 1:
            print("\nif you want to exit enter \"exit\".")
            name = input("Enter Name: ")
            if name.strip().lower() == "exit":
                continue

            department = input("Enter Department: ")
            if department.strip().lower() == "exit":
                continue
            add_staff(staff, name, department)

        elif int(staff_action) == 2:
            if not staff:
                print("No Staff Found!")
            else:
                print(tabulate(staff, headers="keys", tablefmt="rounded_outline"))
    
    elif user_input == 2:
        print("Chouse an option!")
        print("1. Add Devices")
        print("2. Show Devices in table")

        device_action = input("Enter action: ")
        if device_action.strip().lower() == "exit":
            continue

        if int(device_action) == 1:
        
            print("\nif you want to exit enter \"exit\".")
            device_name = input("Enter Device Name: ")
            if device_name.strip().lower() == "exit":
                continue

            device_model = input("Enter Device Model: ")
            if device_model.strip().lower() == "exit":
                continue
            
            add_devices(devices, device_name, device_model)
        
        elif int(device_action) == 2:
            if not devices:
                print("No Devices Found!")
            else:
                print(tabulate(devices, headers= "keys", tablefmt="rounded_outline"))


    elif user_input == 3:
        print(devices, staff)