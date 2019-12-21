#!/usr/bin/python3

from cryptography.fernet import Fernet

#setting
file_encrypted_msg = 'pesan_terenkripsi.txt'
key_file = 'key.txt'

def encrypt(message: bytes, key: bytes) -> bytes:
	return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
	return Fernet(key).decrypt(token)


#read key
key_file_open = open(key_file)
key = key_file_open.read().encode()

#decrypt message
file_encrypted_msg_open = open(file_encrypted_msg)
encrypt_msg = file_encrypted_msg_open.read().encode()
decrypt_msg = decrypt(encrypt_msg, key)
print(decrypt_msg.decode())
