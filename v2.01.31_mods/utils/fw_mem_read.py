#!/usr/bin/env python3
import libuvk5
import sys,os

# Handle arguments
if len(sys.argv) not in [4,5]: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <address> <len> [dest_file.bin]') ; sys.exit(1)

arg_port = sys.argv[1]
arg_addr = int(sys.argv[2],0)
arg_len  = int(sys.argv[3],0)
if len(sys.argv)==5: 
    arg_file=sys.argv[4] 
else: 
    arg_file=None


# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        buff=radio.get_fw_mem(arg_addr,arg_len)
        print(buff.hex())


    if arg_file is not None:
        with open(arg_file,'wb') as f:
            f.write(buff)