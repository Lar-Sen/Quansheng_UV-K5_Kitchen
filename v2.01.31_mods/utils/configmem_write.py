#!/usr/bin/env python3
import libuvk5
from sys import argv,exit
from os import path

# Handle arguments
if len(argv) not in [4,5]: print(f'Usage: {path.basename(argv[0])} <COMx> <address> <hex_payload>') ; exit(1)

arg_port = argv[1]
arg_addr = int(argv[2],0)
payload  = bytes.fromhex(argv[3])
print('PAYLOAD=',payload.hex())

# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        if radio.get_fw_version()["prot"] == 1: print('\nWARN: Config is password protected. Make sure you logged in first.')

        reply = radio.set_cfg_mem(arg_addr,payload)
        if reply: print(f'\nWrote offset {int.from_bytes(reply,"little"):04X} OK')
        else: print('ERR: I/O error or incorrect format!\nData length should divide by 8')
