import pyotpp


key = "THISISMYKEYSECRET"

totp = pyotp.TOTP(key)
print(totp.now())