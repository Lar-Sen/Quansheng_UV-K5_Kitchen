#!/usr/bin/env python3
import libuvk5
import sys,os,struct
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
from os import urandom

if len(sys.argv)!=2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> ') ; sys.exit(1)

arg_port = sys.argv[1]
masterKey = b'\x4A\xA5\xCC\x60\x03\x12\xCC\x5F\xFF\xD2\xDA\xBB\x6B\xBA\x7F\x92'

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        #radio.cmd0530('*')
        #print(radio.get_adc())
        radio.debug=True
        print(radio.get_cfg_mem(0x0F30, 16))