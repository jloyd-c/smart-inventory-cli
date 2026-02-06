import uuid
from data.data_handler import create_staff
from utils import save_to_json

#normalizing string
def normalize(text):
    return " ".join(text.strip().lower().split())

#validation for staff name and department duplications
def staff_duplicate_validators(staff, name, department):
    for member in staff:
        if (
            normalize(member["name"]) == normalize(name)
            and normalize(member["department"]) == normalize(department)
        ):
            return True
    return False

#add staff
def add_staff(staff, name, department):
    #validation for name
    if not name or not name.strip():
        print("Please enter your name!")
        return

    #valiation for department
    if not department or not department.strip():
        print("Please enter your department!")
        return
    
    if staff_duplicate_validators(staff, name.strip(), department.strip()):
        print("Staff already exists!")
        return
    
    #using uuid for auti id generate with huge amount of number
    user_id = uuid.uuid4()

    save_staff = create_staff(user_id.int, name, department)
    staff.append(save_staff)
    save_to_json("data/staff.json", staff)