import libuvk5
from sys import argv,exit
from os import path

# Handle arguments
if len(argv) not in [4,5]: print(f'Usage: {path.basename(argv[0])} <COMx> <address> <len> [dest_file.bin]') ; exit(1)

arg_port = argv[1]
arg_addr = int(argv[2],0)
arg_len  = int(argv[3],0)
if len(argv)==5: 
    arg_file=argv[4] 
else: 
    arg_file=None

# Connect and read
with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        if radio.get_fw_version()["prot"] == 1:
            print('\nWARN: Config is password protected. Make sure you logged in first.')
        buff = radio.get_cfg_mem(arg_addr,arg_len)
        print(buff.hex() if buff is not None else 'ERR: No response from transceiver!')
    
    if arg_file is not None and buff is not None:
        with open(arg_file,'wb') as f:
            f.write(buff)