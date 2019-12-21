#!/usr/bin/python3

from cryptography.fernet import Fernet

key = Fernet.generate_key()  # store in a secure location
print("Key:", key.decode())

def encrypt(message: bytes, key: bytes) -> bytes:
	return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
	return Fernet(key).decrypt(token)

coba = encrypt('aduhai'.encode(), key)
balik = decrypt(coba, key)
print(coba.decode())
print(balik.decode())
