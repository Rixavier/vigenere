# -*- coding:UTF-8 -*-
def vigenere_encrypt(plaintext,key):
	'''加密函数'''
	pt_len = len(plaintext)
	key_len = len(key)
	num = int(pt_len / key_len)
	remain = pt_len % key_len
	ciphertext = ''
	for i in range(0,num):
		for j in range(0,key_len):
			ciphertext += chr((ord(plaintext[i*key_len+j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
	for j in range(0,remain):
		ciphertext += chr((ord(plaintext[key_len*num+j]) - ord('a') + ord(key[j]) - ord('a')) % 26 + ord('a'))
	return ciphertext

def vigenere_decrypt(ciphertext,key):
	'''解密函数'''
	ct_len = len(ciphertext)
	key_len = len(key)
	num = int(ct_len / key_len)
	remain = ct_len % key_len
	plaintext = ''
	for i in range(0,num):
		for j in range(0,key_len):
			plaintext += chr((26 + ord(cliphertext[i*key_len+j]) - ord(key[j])) % 26 + ord('a'))
	for j in range(0,remain):
		plaintext += chr((26 + ord(cliphertext[key_len*num+j]) - ord(key[j])) % 26 + ord('a'))
	return plaintext

plaintext = input("Please inpt the plaintext:")
key = input("Please input the key:")
cliphertext = vigenere_encrypt(plaintext, key)
plaintext = vigenere_decrypt(cliphertext, key)
print('The cliphertext is : ' + cliphertext)
print('The plaintext is : ' + plaintext)


