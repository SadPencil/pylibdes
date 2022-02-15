#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from libdes import des_encrypt, des_decrypt, validate_des_key

if __name__ == '__main__':
    plaintext_hex: str = input('plaintext:')
    key1_hex: str = input('key1:')
    key2_hex: str = input('key2:')
    key3_hex: str = input('key3:')

    plaintext: bytes = bytes.fromhex(plaintext_hex)
    key1: bytes = bytes.fromhex(key1_hex)
    key2: bytes = bytes.fromhex(key2_hex)
    key3: bytes = bytes.fromhex(key3_hex)

    if not (validate_des_key(key1) and validate_des_key(key2) and validate_des_key(key3)):
        raise Exception('Parity check failed on the key.')

    ciphertext: bytes = des_encrypt(
        des_decrypt(
            des_encrypt(plaintext, key1),
            key2,
        ),
        key3,
    )

    print('ciphertext:', ciphertext.hex())

    plaintext: bytes = des_decrypt(
        des_encrypt(
            des_decrypt(ciphertext, key3),
            key2,
        ),
        key1,
    )

    print('plaintext:', plaintext.hex())
