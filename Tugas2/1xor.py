from pwn import xor
from Crypto.Util import *; strxor.strxor(b"C", b"H")

#nomor1xor
string = "label"
flag = ''
for x in string:
   flag += chr(ord(x) ^ 13)
print("nomor1xor:")
print("crypto{",flag,"}\n")