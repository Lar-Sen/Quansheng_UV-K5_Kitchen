#!/usr/bin/env python3
import libuvk5
import sys,os

# Handle arguments
if len(sys.argv) not in [2,]: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx>') ; sys.exit(1)

arg_port = sys.argv[1]

# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        reply = radio.get_fw_version()
        version = reply["ver"].split(b'\0', 1)[0].decode()
        print(version,'Firmware\nPIN ok? ',reply["pin"] == 0,'\nConfig password protected? ',reply["prot"] == 1,'\nAES Challenge :',reply["nonce"])
