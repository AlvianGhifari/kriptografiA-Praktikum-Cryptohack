import sys
import base64
from Crypto.Util import *; strxor.strxor(b"C", b"H")
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

#nomor3
char = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
flag = ''
for x in char:
    flag = flag+ chr(x)
print("Here is your flag:")
print(flag)