#!/usr/bin/env python3
## Bin2Array.py
## Exports binary file contents to a text-formatted bytearray

import sys,os

if len(sys.argv)!=3:
   print(f'Usage: {os.path.basename(sys.argv[0])} <input_file.bin> <output_file.txt>')
   sys.exit(1)

if os.path.exists(sys.argv[2]):
   print(f'Warning: {os.path.basename(sys.argv[2])} exists in current directory. Please delete it before proceeding.')
   sys.exit(1)

raw = open(sys.argv[1],'rb').read().hex()
output = r"0x" + r", 0x".join(raw[n : n+2] for n in range(0, len(raw), 2))

open(sys.argv[2],'wt').write(output)
print(f'Binary successfully converted to {os.path.basename(sys.argv[2])}')
