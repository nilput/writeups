#!/usr/bin/env python3
input_strings='''A1<1A1N1A
B1<1A1N1B
B1<1B1N1C
B1<1C1N1D
C1<1C1N1E
D1<1C1N1F
A1>1A1N1A
B1>1A1N1B
C1>1C1N1A
D1<1C1N1F
E1<1D1N1H'''

def bitwise_xor(string, key):
    string_bytes = list(string.encode('ascii'))
    for i,b in enumerate(string_bytes):
        string_bytes[i] = string_bytes[i] ^ key
    return bytes(string_bytes).decode('ascii', 'ignore')

def bytewise_add(string, key):
    string_bytes = list(string.encode('ascii'))
    for i,b in enumerate(string_bytes):
        string_bytes[i] = (string_bytes[i] + key) % 256
    return bytes(string_bytes).decode('ascii', 'ignore')

#try brute force bitwise xor 
for i in range(256):
    for line in input_strings.split('\n'):
        print('XOR {}: {}'.format(i, bitwise_xor(line, i)))

#try brute force bytewise addition
for i in range(256):
    for line in input_strings.split('\n'):
        print('ADD {}: {}'.format(i, bytewise_add(line, i)))
