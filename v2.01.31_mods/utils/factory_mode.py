#!/usr/bin/env python3
import libuvk5
from sys import argv,exit
from os import path

# Handle arguments
if len(argv) not in [2,]: print(f'Usage: {path.basename(argv[0])} <COMx>') ; exit(1)

arg_port = argv[1]

# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        reply = radio.get_fw_ver_mute()
        version = reply["ver"].split(b'\0', 1)[0].decode()
        print(version,'Firmware [FACTORY MODE]\nPIN ok? ',reply["pin"] == 0,'\nConfig password protected? ',reply["prot"] == 1,'\nAES Challenge :',reply["nonce"])
