# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 19:07:26 2020

@author: Juan Esteban Cepeda
"""

# Import libraries.
import binascii

# Text to bits.
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# Int2bytes.
def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

# IntToString.
def int2string(i, encoding='utf-8', errors='surrogatepass'):
    bytes_ = int2bytes(i)
    return bytes_.decode(encoding, errors)

# String to int.
def string2int(text):
    bits_ = text_to_bits(text)
    return int(bits_, 2)

# Convert a string to a list of substring of length 4 or less.
def string_to_4list(text):
    list_of_messages = list()
    pos = 0
    while pos < len(text):
        try:
            list_of_messages.append(text[pos: pos + 4])
            pos += 4
        except:
            list_of_messages.append(text[pos: len(text)])
    return list_of_messages

# Rejoin lists.
def joinTextList(text_list): 
    return "".join(text_list)