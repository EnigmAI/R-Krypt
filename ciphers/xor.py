from itertools import izip, cycle
import base64

def encrypt(message, key):
    text = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(message, cycle(key)))
    return base64.encodestring(text).strip()
def decrypt(message, key):
    message = base64.decodestring(message)
    text = ''.join(chr(ord(x) ^ ord(y)) for (x,y) in izip(message, cycle(key)))
    return text

