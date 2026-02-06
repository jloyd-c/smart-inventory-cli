from datetime import datetime

def create_staff(id, name, department, status="active"):
    return {
        "id": id,
        "name": name,
        "department": department,
        "status": status
    }

def create_device(id, name, model, serial, status="available"):
    return {
        "id": id,
        "name": name,
        "model": model,
        "serial": serial,
        "status": status
    }

def today():
    return datetime.now().strftime("%Y-%m-%d")

def create_borrow_record(id, staff_id, device_id, remarks=""):
    return {
        "id": id,
        "staff_id": staff_id,
        "device_id": device_id,
        "date_issued": today(),
        "date_returned": None,
        "remarks": remarks
    }
