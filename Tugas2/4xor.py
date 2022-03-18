from pwn import xor
from Crypto.Util import *; strxor.strxor(b"C", b"H")

#nomor4xor 
hex = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
format = "crypto{"
encoded = bytes.fromhex(hex)
print("nomor4xor:")
print(xor(encoded,format.encode()))
guessed_key = "myXORkey"
print("key= myXORkey")
print(xor(guessed_key.encode(), encoded))