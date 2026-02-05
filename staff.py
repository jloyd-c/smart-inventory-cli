import uuid

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
def add_staff(staff, name, department, status):

    if int(status) == 1:
        status = "ACTIVE"
    elif int(status) == 2:
        status = "INACTIVE"

    #validation for name
    if not name or not name.strip():
        print("Please enter your name!")
        return

    #valiation for department
    if not department or not department.strip():
        print("Please enter your department!")
        return

    #validation for status
    if not status or not status.strip():
        print("Please enter number!")
        return
    
    if staff_duplicate_validators(staff, name.strip(), department.strip()):
        print("Staff already exists!")
        return
    
    #using uuid for auti id generate with huge amount of number
    user_id = uuid.uuid4()

    staff.append({
        #used .int attribute / property 
        "id": user_id.int,
        "name": normalize(name),
        "department": normalize(department),
        "status": status
    })
