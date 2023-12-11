#!/usr/bin/env python3
## Bin2Array.py
## Exports binary file contents to a text-formatted bytearray

from sys import argv,exit
from os import path

if len(argv)!=3:
   print(f'Usage: {path.basename(argv[0])} <input_file.bin> <output_file.txt>')
   exit(1)

if path.exists(argv[2]):
   print(f'Warning: {path.basename(argv[2])} exists in current directory. Please delete it before proceeding.')
   exit(1)

raw = open(argv[1],'rb').read().hex()
output = r"0x" + r", 0x".join(raw[n : n+2] for n in range(0, len(raw), 2))

open(argv[2],'wt').write(output)
print(f'Binary successfully converted to {path.basename(argv[2])}')
