import pyotp
import pyqrcode
from pyqrcode import QRCode


key = "ThisSecretMisbahKeyAppIShereForYuo"

totp = pyotp.TOTP(key)
print(totp.now())

url = pyqrcode.create(str(totp.now()))
url.svg("totp.svg", scale=8)

url
 # => True
print(totp.verify('073874'))

class Device:
    def __init__(self, name):
        self.name = name
        self.secret_key = py    
        #read a device mac address
        self.mac_address = mac_address
        self.is_activated = False

class User:
    def __init__(self, name, email, password):
        self.devices = []
        self.name = name
        self.email = email
        self.password = password
        self.is_logged_in = False
        self.data = UserData()

    def add_device(self, device):
        self.devices.append(device)
    
    def remove_device(self, device):
        self.devices.remove(device)
    
    def get_devices(self):
        return self.devices

    def login(self, email, password):
        if self.email == email and self.password == password:
            self.is_logged_in = True
            return "Login successful"
        else:
            return "Login failed"

    def logout(self):
        self.is_logged_in = False
        return "Logged out"

class UserData:
    def __init__(self):
        self.data = {}

    def add_data(self, key, value):
        self.data[key] = value

    def remove_data(self, key):
        del self.data[key]

    def get_data(self, key):
        return self.data[key]

    def get_all_data(self):
        return self.data

    def update_data(self, key, value):
        self.data[key] = value