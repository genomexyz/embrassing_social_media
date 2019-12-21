#!/usr/bin/python3

from cryptography.fernet import Fernet

#setting
fileinput_msg = 'pesan.txt'
fileoutput_encrypted_msg = 'pesan_terenkripsi.txt'
key_file = 'key.txt'

def encrypt(message: bytes, key: bytes) -> bytes:
	return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
	return Fernet(key).decrypt(token)


#generate key
key = Fernet.generate_key()  # store in a secure location
print("Key:", key.decode())

#save key
key_file_open = open(key_file, 'w')
key_file_open.write(key.decode())

#encrypt message
fileinput_msg_open = open(fileinput_msg)
msg = fileinput_msg_open.read()
encrypt_msg = encrypt(msg.encode(), key)
fileoutput_encrypted_msg_open = open(fileoutput_encrypted_msg, 'w')
fileoutput_encrypted_msg_open.write(encrypt_msg.decode())
