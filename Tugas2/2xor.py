from pwn import xor
from Crypto.Util import *; strxor.strxor(b"C", b"H")

#nomor2xor 
hasil1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
s2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
hasil2 = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(hasil1,s2))

s2 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
hasil3 = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(hasil2,s2))

a_list = [chr(int(a, 16) ^ int(b, 16)) for a,b in zip(hasil1, hasil3)]
hasiltemp = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(hasil1,hasil3))

hasil4 = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(hasiltemp,hasil2))

s2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"
flag = ''.join(format(int(a, 16) ^ int(b, 16), 'x') for a,b in zip(s2,hasil4))
hasiltotal= bytes.fromhex(flag)
print("nomor2xor:")
print(hasiltotal,"\n")