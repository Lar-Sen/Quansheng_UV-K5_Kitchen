#!/usr/bin/env python3
#Cleartext firmware writer for UV-K5 (partial / full)
#Please note that partial flashing requires bootloader mod, as QS derpily decided to erase full flash as soon as flasher gets block 1
#Courtesy of LarSeN
import libuvk5
import sys,os,struct
from time import sleep,time

# Handle arguments
if len(sys.argv) < 3:
    print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <unscrambled_rom.bin> [block number] [blocks to write]\nDevice must be set in ROM flash boot mode (PTT+Turn ON)')
    print('Note: Last block number is 240. Incomplete or missing blocks will be padded to 0xFF.')
    sys.exit(1)

if len(sys.argv) > 3:
    arg_block = int(sys.argv[3],0) ; SAFE = True
    ##TODO----------
    print('\nNOTE: For many units, partial flashing is not working for now. Bootloader mod is needed.')
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
            reply = radio.rom_flash_set('*.01.31')
            if reply["ret"].hex() == '1805':
                print('\nHELO', reply["pfm"].decode(),reply["boot"].decode())
                with open(arg_file,'rb') as f:
                    radio.debug = True
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

                            reply = radio.block_flash(i,wlen,end,bin256)
                            if i == offset: sleep(2)		#lets take time to erase flash ROM blocks
                            #print(payload.hex())
                            if SAFE:
                                #Wait for good ACK (0x51A). BL keeps spitting (0x518) if error.
                                wd = int(time())
                                while reply[4:6] != b'\x1A\x05':
                                    reply = radio.uart_receive_msg(44)
                                    if int(time()) - wd == 10: print('ERROR: Timeout while waiting for ACK'); sys.exit(1)

                                if int.from_bytes(reply[14:15],'little') != 1: print(1+int.from_bytes(reply[12:-6],'little'), 'OK')
                                else: print('ERROR: Received bad ACK')
                            else: print(1+int(i/256), 'sent')
                        print('\nDone! Your transceiver will self reboot now...')

    else: print('ERROR: File not found');sys.exit(1)
