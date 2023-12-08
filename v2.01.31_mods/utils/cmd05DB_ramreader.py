#!/usr/bin/env python3
##RAM Reader - An arbitrary RAM dumper for UV-K5
##needs corresponding mod and libuvk5 library installed

import sys,struct,argparse
import serial
import libuvk5

pl = argparse.ArgumentParser(description='UV-K5 RAM/ROM Dumper via serial interface cable (CMD 05DB)', epilog='Memory dumper for UV-K5 transceiver.\nNeeds companion mod applied to original firmware.')
pl.add_argument('interface', nargs=1, help='serial port to transceiver')
pl.add_argument('address', nargs=1, help='memory starting address to dump')
pl.add_argument('data_len', nargs=1, type=int, help='number of bytes to dump')
pl.add_argument('--filename', nargs=1, type=argparse.FileType('wb'), required=False, default=None, help='optional filename where to save dump')
params = pl.parse_args()

with libuvk5.uvk5(params.interface[0]) as radio:
    if radio.connect():
        reply=radio.read_mem(1,int(params.address[0],16),params.data_len[0])
        if reply == b'CMD:Error!\x00': print('ERR: Invalid memory read.\nOnly user RAM and ROM regions allowed.') ; sys.exit(1)

if reply:
    if params.filename is not None: params.filename[0].write(reply)
    else: print('[{}]'.format(', '.join(format(int(x), '#04x') for x in reply)))

else: print('\nERR: No response from transceiver!')