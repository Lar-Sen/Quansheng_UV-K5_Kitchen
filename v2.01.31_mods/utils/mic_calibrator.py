#!/usr/bin/env python3
##Mic gain factors editor
#There are 5 corresponding menu levels to values @1F80 in EEPROM. Max value is 31.
#Courtesy of LarSeN

import libuvk5
import struct
from sys import argv,exit
from os import path

if len(argv)<3: print(f'Usage: {path.basename(argv[0])} <COMx> <read | write  lev0 lev1 lev2 lev3 lev4>') ; exit(1)
arg_port = argv[1]
action   = argv[2]

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        if radio.get_fw_version()["prot"] == 1:
            print('\nWARN: Config is password protected. Make sure you logged in first.')
        calib_raw = radio.get_cfg_mem(0x1F80,8)
        calib_data     = list(struct.unpack('<8c',calib_raw))
        calib_data_old = [i for i in calib_data]
        if action == 'read':
            print('Level {}: {:.0f} /31'.format(0, int.from_bytes(calib_data[0], byteorder='big')), '(Lowest)')
            print('Level {}: {:.0f} /31'.format(1, int.from_bytes(calib_data[1], byteorder='big')), '(Lower)')
            print('Level {}: {:.0f} /31'.format(2, int.from_bytes(calib_data[2], byteorder='big')), '(Mid)')
            print('Level {}: {:.0f} /31'.format(3, int.from_bytes(calib_data[3], byteorder='big')), '(Higher)')
            print('Level {}: {:.0f} /31'.format(4, int.from_bytes(calib_data[4], byteorder='big')), '(Highest)')

        if action=='write': 
            if len(argv)!=8: print(f'Usage: {path.basename(argv[0])} <COMx> write lev0 lev1 lev2 lev3 lev4') ; exit(1)
            calib_data[0] = int(argv[3],0).to_bytes(1,'big')
            calib_data[1] = int(argv[4],0).to_bytes(1,'big')
            calib_data[2] = int(argv[5],0).to_bytes(1,'big')
            calib_data[3] = int(argv[6],0).to_bytes(1,'big')
            calib_data[4] = int(argv[7],0).to_bytes(1,'big')
            calib_raw = struct.pack('8c',*calib_data)
            radio.set_cfg_mem(0x1F80,calib_raw)
            print('OK. New values written to eeprom')
            print('Previous mic gain factors(hex):',calib_data_old[0:4])            
            print('Current mic gain factors(hex):',struct.unpack('<8c',radio.get_cfg_mem(0x1F80,8))[0:4])
            print('!!! PLEASE REBOOT RADIO FOR THE CHANGES TO TAKE EFFECT !!!')