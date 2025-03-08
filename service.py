from jnius import autoclass
from time import sleep

BluetoothAdapter = autoclass("android.bluetooth.BluetoothAdapter")

# Get Bluetooth adapter
bt_adapter = BluetoothAdapter.getDefaultAdapter()

# Define the target Bluetooth device MAC address (Replace with actual MAC)
TARGET_DEVICE_MAC = "8C:5A:C1:7A:51:8D"

def enable_bluetooth():
    """Enable Bluetooth if it's turned off."""
    if not bt_adapter.isEnabled():
        bt_adapter.enable()

def connect_bluetooth():
    """Check for paired devices and connect to the target device."""
    if bt_adapter.isEnabled():
        paired_devices = bt_adapter.getBondedDevices().toArray()
        
        for device in paired_devices:
            if device.getAddress() == TARGET_DEVICE_MAC:
                
                # Get remote device and try to connect
                remote_device = bt_adapter.getRemoteDevice(TARGET_DEVICE_MAC)
                remote_device.createBond()  # Request connection
                
                break
        else:
            print(".") 

# Run the service in a loop every minute
while True:
    enable_bluetooth()
    connect_bluetooth()
    sleep(60)