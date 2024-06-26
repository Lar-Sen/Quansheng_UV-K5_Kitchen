#!/usr/bin/env python3
import libuvk5
from sys import argv,exit
from os import path

# Handle arguments
if len(argv)!=4: print(f'Usage: {path.basename(argv[0])} <COMx> backup | restore <dest_file.bin>') ; exit(1)

arg_port=argv[1]
arg_file=argv[3]

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        if radio.get_fw_version()["prot"] == 1:
            print('\nWARN: Config is password protected. Make sure you logged in first.')
        if argv[2] == 'backup' and not path.exists(arg_file):
            with open(arg_file,'wb') as f:
                for i in range(0,64):
                    print(f'Reading {i*0x80:04X}...' )
                    chunk = radio.get_cfg_mem(i*0x80,0x80)
                    f.write(chunk)
            print('Backed up',(1+i)/8,'Kbytes to',arg_file)

        if argv[2] == 'restore':
            #Read file and bulk write
            with open(arg_file,'rb') as f:
                eeprom=f.read()
                for i in range(0,64):
                    print(f'\nWriting {i*0x80:04X}...')
                    bin128 = eeprom[i*0x80:i*0x80+128]
                    offset=radio.set_cfg_mem(i*0x80, bin128)
                    print('Wrote', hex(int.from_bytes(offset,'little')))

            print('\nNow rebooting...')
            radio.reboot()