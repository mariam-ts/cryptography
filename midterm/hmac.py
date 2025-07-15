import hmac
import hashlib

key = b'secretkey123'

with open('data.txt', 'rb') as f:
    msg = f.read()

h = hmac.new(key, msg, hashlib.sha256)
print("HMAC:", h.hexdigest())