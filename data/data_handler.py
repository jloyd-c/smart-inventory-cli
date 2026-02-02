import json

# 1: create a empty list
staff = []
devices = []
borrow_records = []

# 2: create a schema
# 2a: Staff dictionary example
staff_example = {
    "id": 1,
    "name": "Alice Johnson",
    "department": "IT",
    "status": "Active"
}

staff.append(staff_example)

# 2b: Device dictionary example
device_example = {
    "id": 1,
    "name": "Laptop",
    "model": "Dell XPS 13",
    "serial": "DX13-001",
    "status": "Available"
}

devices.append(device_example)

# 2c: Borrow Record dictionary example
borrow_example = {
    "staff_id": 1,
    "device_id": 1,
    "date_borrowed": "2026-02-02",
    "date_returned": None  # None = not returned yet
}

borrow_records.append(borrow_example)