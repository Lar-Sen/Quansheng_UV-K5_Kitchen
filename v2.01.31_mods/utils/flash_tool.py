#!/usr/bin/env python3
#Cleartext firmware writer for UV-K5
#Courtesy of LarSeN
import libuvk5
import sys,os,struct
from time import sleep

# Handle arguments
if len(sys.argv) != 3: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <unscrambled_rom.bin>\nDevice must be set in ROM flash boot mode (PTT+Turn ON)') ; sys.exit(1)

arg_port = sys.argv[1]
arg_file = sys.argv[2]

# Connect and flash whole user ROM
with libuvk5.uvk5(arg_port) as radio:
    if os.path.exists(arg_file):
        if radio.connect():
            radio.get_fw_version()
            reply = radio.rom_flash_set('*.00.06')
            if reply["ret"].hex() == '1805':
                print('HELO', reply["pfm"].decode(),reply["boot"].decode())
                with open(arg_file,'rb') as f:
                    fw=f.read()
                    if len(fw) & 0xFF: end = 256 + (len(fw) & 0xFF00)
                    else: end = len(fw)
                    for i in range(0,len(fw),256):
                        print(f'\nWriting {i:04X}...')
                        delta = i + 256
                        if delta > len(fw):
                            delta = i + i % len(fw)
                            bin256 = fw[i:delta] + b'\x00'*((i+256) % len(fw))

                        else: bin256 = fw[i:delta]

                        ## payload: 0x1905 + 0x0C01 + {0x8A8D9F1D + >H.address + 0xE600(>H.maxflashaddr) + 0x0100(<H.length) + 0x0000 + [256 data bytes]}
                        payload = b'\x8A\x8D\x9F\x1D' + struct.pack('>HH',i,end) + b'\x01\x00\x00\x00' + bin256
                        reply = radio.block_flash(payload)
                        print(payload.hex())
                        while 'abcd0c000c69' not in reply.hex():
                            reply = radio.serial.read(48)
                            #print(reply.hex())

                        #print('<dec<',reply.hex())
                        print(1+int(i/256), 'OK')

                print('\nDone! Your transceiver will self reboot now...')

    else: print('ERROR: File not found');sys.exit(1)
