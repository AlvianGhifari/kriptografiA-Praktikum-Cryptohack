from pwn import xor
from Crypto.Util import *; strxor.strxor(b"C", b"H")

#nomor3xor 
hex = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

def decode(i):
    return ''.join([chr(i ^ a) for a in hex])

for i in range(0, 127):
    if "crypto" in decode(i):
        print("nomor3xor:")
        print(decode(i),"\n")