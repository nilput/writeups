#!/usr/bin/env python3
out_bytes = b''
with open('ch3.zip', 'rb') as f:
    in_bytes = f.read()
    for b in in_bytes:
        out_bytes += bytes([ (b + 239) % 256])
        
with open('decrypted.zip', 'wb') as f:
    f.write(out_bytes)
