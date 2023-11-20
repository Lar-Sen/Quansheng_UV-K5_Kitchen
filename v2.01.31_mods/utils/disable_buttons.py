#!/usr/bin/env python3
import libuvk5
import sys,os

if len(sys.argv)!=2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> ') ; sys.exit(1)

arg_port = sys.argv[1]

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        radio.get_fw_ver_mute()
