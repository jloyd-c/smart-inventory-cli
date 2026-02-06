from data.data_handler import create_device
import uuid
from utils import save_to_json

def add_devices(devices, device_name, device_model):

    if not device_name or not device_name.strip():
        print("Please enter your device name!")
        return
    
    if not device_model or not device_model.strip():
        print("Please enter your device model!")
        return


    # auto generate id for devices
    device_id = uuid.uuid4()
    # auto generate serial number
    device_serial = str(uuid.uuid4())

    #saving devices to a empty list and to a json file
    save_devices = create_device(device_id.int, device_name, device_model, device_serial)
    devices.append(save_devices)
    save_to_json("data/devices.json", devices)