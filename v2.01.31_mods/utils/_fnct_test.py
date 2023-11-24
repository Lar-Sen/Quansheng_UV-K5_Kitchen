#!/usr/bin/env python3
import libuvk5
import sys,os,time,struct
from itertools import cycle

def payload_xor(payload):
    Key = [ 0x16, 0x6C, 0x14, 0xE6, 0x2E, 0x91, 0x0D, 0x40, 0x21, 0x35, 0xD5, 0x40, 0x13, 0x03, 0xE9, 0x80, ]
    return bytes([a ^ b for a, b in zip(payload, cycle(Key))])

if len(sys.argv)< 2: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> [timestamp]') ; sys.exit(1)
if len(sys.argv) == 3: timeStamp = int(sys.argv[2],0).to_bytes(4,'big')
else: timeStamp = int(time.time()).to_bytes(4,'little')
arg_port = sys.argv[1]
masterKey = b'\x4A\xA5\xCC\x60\x03\x12\xCC\x5F\xFF\xD2\xDA\xBB\x6B\xBA\x7F\x92'

with libuvk5.uvk5(arg_port) as radio:
    if radio.connect():
        radio.debug=True
        radio.uart_send_msg(radio.build_uart_command(radio.CMD_EEPB_GET, struct.pack('<HH',0x0F30,16) + timeStamp))
        reply = radio.serial.read(32)
        print(reply.hex())
        v=payload_xor(reply[4:-2])
        print(v[8:-2].hex())