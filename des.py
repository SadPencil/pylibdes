#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from libdes import des_encrypt, des_decrypt, validate_des_key

if __name__ == '__main__':
    plaintext_hex: str = input('plaintext:')
    key1_hex: str = input('key:')

    plaintext: bytes = bytes.fromhex(plaintext_hex)
    key1: bytes = bytes.fromhex(key1_hex)

    if not validate_des_key(key1):
        raise Exception('Parity check failed on the key.')

    ciphertext: bytes = des_encrypt(plaintext, key1)
    print('ciphertext:', ciphertext.hex())

    plaintext: bytes = des_decrypt(ciphertext, key1)
    print('plaintext:', plaintext.hex())

# Example: https://www.hankcs.com/security/des-algorithm-illustrated.html

# Plaintext: 8787878787878787
# Key: 0E329232EA6D0D73
# Ciphertext: 0000000000000000

# Plaintext: 0123456789ABCDEF
# Key: 133457799BBCDFF1
# Ciphertext: 85e813540f0ab405
