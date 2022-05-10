import sys
import base64
from Crypto.Util import *; strxor.strxor(b"C", b"H")
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

#nomor5
bytes = bytes.fromhex("72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf")
base = base64.b64encode(bytes)
print("Here is your flag:")
print(base)