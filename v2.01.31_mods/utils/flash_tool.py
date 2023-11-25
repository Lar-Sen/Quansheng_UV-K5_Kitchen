#!/usr/bin/env python3
#Cleartext firmware writer for UV-K5 (partial / full)
#Please note that partial flashing requires bootloader mod, as QS derpily decided to erase full flash as soon as flasher gets block 1
#Courtesy of LarSeN
import libuvk5
import sys,os,struct
from time import sleep

# Handle arguments
if len(sys.argv) < 3:
    print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <unscrambled_rom.bin> [block number] [blocks to write]\nDevice must be set in ROM flash boot mode (PTT+Turn ON)')
    print('Note: Last block number is 240. Incomplete or missing blocks will be padded to 0xFF.')
    sys.exit(1)

if len(sys.argv) > 3:
    arg_block = int(sys.argv[3],0) ; SAFE = True
    ##TODO----------
    print('Partial flashing is not working for now: Correcting arguments to full flash.')
    arg_block = False ; SAFE = False
    ##----------TODO
else: arg_block = False ; SAFE = False		#Change 'SAFE' here to True, to wait for bootloader ack after each successful block write

if len(sys.argv) == 5: arg_nblocks = int(sys.argv[4],0)
else: arg_nblocks = False

arg_port = sys.argv[1]
arg_file = sys.argv[2]

# Connect and flash selected ROM region
with libuvk5.uvk5(arg_port) as radio:
    if os.path.exists(arg_file):
        if radio.connect():
            radio.get_fw_version()
            reply = radio.rom_flash_set('*.00.06')
            if reply["ret"].hex() == '1805':
                print('HELO', reply["pfm"].decode(),reply["boot"].decode())
                with open(arg_file,'rb') as f:
                    radio.debug = False
                    fw=f.read()
                    if len(fw) <= 0xF000: end = len(fw)
                    else: print('ERROR: firmware provided exceeds maximum size!')
                    if len(fw) & 0xFF: end = 256 + (len(fw) & 0xEF00)

                    if arg_block: offset = (arg_block-1)*0x100
                    else: offset=0

                    if arg_nblocks:
                        end = offset + arg_nblocks*256
                        if end > 0xF000: end=0xF000

                    print('\nAbout to FLASH',end-offset,'bytes to user ROM!\nSure?')
                    if input(' Confirm [Y/n]') == 'Y':
                        for i in range(offset,end,256):
                            print(f'\nWriting {i:04X}...')
                            delta = i + 256
                            if delta > len(fw):
                                wlen = 256 - (delta % len(fw))
                                delta = i + i % len(fw)
                                bin256 = fw[i:delta] + b'\xFF'*(256-len(fw[i:delta]))
                            else: bin256 = fw[i:delta] ; wlen = 256

                            ## payload: (0x1905 + 0x0C01) + {0x8A8D9F1D + offset(BIG) + regionEnd(BIG) + length(BIG) + 0x0000 + [256 data bytes]}
                            payload = b'\x8A\x8D\x9F\x1D' + struct.pack('>HH',i,end) + int.to_bytes(wlen,2,'big') + b'\x00\x00' + bin256
                            reply = radio.block_flash(payload)
                            print(payload.hex())
                            if SAFE:
                                #Wait for good ACK (0x518). A bad one is abcd24000e69 (0x51A)
                                while 'abcd0c000c69' not in reply.hex():
                                    reply = radio.serial.read(48)
                                    if radio.debug: print('<raw<',reply.hex())

                                print(1+int(i/256), 'OK')

                print('\nDone! Your transceiver will self reboot now...')

    else: print('ERROR: File not found');sys.exit(1)
