# Hemaya Fawazer Q2

## Question:
Our neighbour invented a new encryption method, he claims it is more secure than worldwide accepted algorithms, he encrypted a file [ch3.zip](./ch3.zip) and lost the password, it is encrypted using **a single byte**, can you decrypt it and return it back to him?

## Strategies to reach the answer:
* Analyze the file, seeing whether it's recognized as any valid file format
* Analyze the file, looking for any human readable strings 
* We know that the file format is supposed to be .zip, compare the beginning of the file to valid zip headers

### Checking the file using command line tools
```
    file ch3.zip
```
### Output:
```
    ch3.zip: data
```

Hmm, it's saying it's data, which doesn't help, usually this is printed when it the command **file** cannot recognize the format of the file

Let's inspect the contents of the file using a hex dump

```
    hexdump -C ch3.zip | less
```

### the beginning of the file:
```
    00000000  61 5c 14 15 1b 11 11 11  11 11 78 2b ba 61 4b 2c  |a\........x+.aK,|
    00000010  05 44 29 50 11 11 29 50  11 11 19 11 2d 11 77 7d  |.D)P..)P....-.w}|
    00000020  72 78 3f 8b 7a 81 66 65  1a 11 14 13 08 c6 6f 13  |rx?.z.fe......o.|
    00000030  08 c6 6f 86 89 1c 11 12  15 06 12 11 11 15 25 11  |..o...........%.|
    00000040  11 11 61 5c 14 15 25 11  11 11 19 11 69 28 b9 61  |..a\..%.....i(.a|
    00000000  61 5c 14 15 1b 11 11 11  11 11 78 2b ba 61 4b 2c  |a\........x+.aK,|
    00000010  05 44 29 50 11 11 29 50  11 11 19 11 2d 11 77 7d  |.D)P..)P....-.w}|
    00000020  72 78 3f 8b 7a 81 66 65  1a 11 14 13 08 c6 6f 13  |rx?.z.fe......o.|
    00000030  08 c6 6f 86 89 1c 11 12  15 06 12 11 11 15 25 11  |..o...........%.|
    00000040  11 11 61 5c 14 15 25 11  11 11 19 11 69 28 b9 61  |..a\..%.....i(.a|
```
### towards the end we have:
```
    00003fd0  41 31 3c 31 41 31 4e 31  41 1b 42 31 3c 31 41 31  |A1<1A1N1A.B1<1A1|
    00003fe0  4e 31 42 1b 42 31 3c 31  42 31 4e 31 43 1b 42 31  |N1B.B1<1B1N1C.B1|
    00003ff0  3c 31 43 31 4e 31 44 1b  43 31 3c 31 43 31 4e 31  |<1C1N1D.C1<1C1N1|
    00004000  45 1b 44 31 3c 31 43 31  4e 31 46 1b 64 86 73 85  |E.D1<1C1N1F.d.s.|
    00004010  83 72 74 85 7a 80 7f 4b  1b 41 31 3e 31 41 31 4e  |.rt.z..K.A1>1A1N|
    00004020  31 41 1b 42 31 3e 31 41  31 4e 31 42 1b 43 31 3e  |1A.B1>1A1N1B.C1>|
    00004030  31 43 31 4e 31 41 1b 44  31 3c 31 43 31 4e 31 46  |1C1N1A.D1<1C1N1F|
    00004040  1b 45 31 3c 31 44 31 4e  31 48 1b 61 5c 12 13 2f  |.E1<1D1N1H.a\../|
    00004050  14 1b 11 11 11 11 11 78  2b ba 61 4b 2c 05 44 29  |.......x+.aK,.D)|
    00004060  50 11 11 29 50 11 11 19  11 29 11 11 11 11 11 11  |P..)P....)......|
    00004070  11 11 11 b5 92 11 11 11  11 77 7d 72 78 3f 8b 7a  |.........w}rx?.z|
    00004080  81 66 65 16 11 14 13 08  c6 6f 86 89 1c 11 12 15  |.fe......o......|
    00004090  06 12 11 11 15 25 11 11  11 61 5c 12 13 2f 14 1b  |.....%...a\../..|
    000040a0  11 11 11 11 11 dc 2a ba  61 ca da f5 b8 c0 11 11  |......*.a.......|
    000040b0  11 c0 11 11 11 19 11 29  11 11 11 11 11 11 11 11  |.......)........|
    000040c0  11 b5 92 6b 50 11 11 7a  7f 77 80 3f 85 89 85 66  |...kP..z.w.?...f|
    000040d0  65 16 11 14 ee 06 c6 6f  86 89 1c 11 12 15 06 12  |e......o........|
    000040e0  11 11 15 25 11 11 11 61  5c 16 17 11 11 11 11 13  |...%...a\.......|
    000040f0  11 13 11 ad 11 11 11 5c  51 11 11 11 11           |.......\Q....|
    000040fd
```
while most of the file seems to be binary and not readable, the bytes around **00003ff0** seem to be
readable.

### looking for strings in the file using the **strings** command

```
strings ch3.zip | less
```
### Output:
most of the output is binary, but towards the end we have these suspicious strings:
```
A1<1A1N1A
B1<1A1N1B
B1<1B1N1C
B1<1C1N1D
C1<1C1N1E
D1<1C1N1F
A1>1A1N1A
B1>1A1N1B
C1>1C1N1A
D1<1C1N1F
E1<1D1N1H
```

We can try to understand them, they seem to have originated from the plaintext, remember that in the question it is mentioned that
the unknown encryption algorithm used only 1 byte for the "encryption" key, so it could be the case that these are just ascii strings with a simple
**bitwise** or **bytewise** operation applied to them, in case of bitwise operations **(AND, NOR, NOT)** cannot be used,
because they result in the loss of information and therefore invalid encryption, but **XOR** can be used.

In terms of **bytewise** operations, it can be anything, but since these strings seem to hold their original structure from the plaintext, this suggests addition or subtraction mod 256?


We can create a simple python [script](./decrypt_strings.py) to try our possible candidates:
``` python
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
```

The output is huge, and most of it will be garbage, but somewhere in there we find this, which looks like a valid decryption of our original strings:
```
ADD 238: 2^_*^_1^_<^_4
ADD 238: 3^_*^_2^_<^_6
ADD 239: 0 + 0 = 0
ADD 239: 1 + 0 = 1
ADD 239: 1 + 1 = 2
ADD 239: 1 + 2 = 3
ADD 239: 2 + 2 = 4
ADD 239: 3 + 2 = 5
ADD 239: 0 - 0 = 0
ADD 239: 1 - 0 = 1
ADD 239: 2 - 2 = 0
ADD 239: 3 + 2 = 5
ADD 239: 4 + 3 = 7
ADD 240: 1!,!1!>!1
ADD 240: 2!,!1!>!2
```

let's write a [script](./decrypt.py) to do the same operation on the whole file:

``` python
#!/usr/bin/env python3
out_bytes = b''
with open('ch3.zip', 'rb') as f:
    in_bytes = f.read()
    for b in in_bytes:
        out_bytes += bytes([ (b + 239) % 256])
        
with open('decrypted.zip', 'wb') as f:
    f.write(out_bytes)
```

try decompressing the output file:

```
unzip decrypted.py
```

### Output:
```
Archive:  decrypted.zip
 extracting: flag.zip
 extracting: info.txt
```

```
unzip flag.zip
```

```
Archive:  flag.zip
  inflating: flag.bmp
```
![flag](./decrypted/flag.bmp)


That's it! we successfuly unpacked the file


Written by: Turki alsaleem

[github](https://github.com/nilput/)
