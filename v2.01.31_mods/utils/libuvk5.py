#!/usr/bin/env python3
import serial
import time,struct
from os import getenv
from itertools import cycle

#CRC computation
def CrcByte(n, poly, size):
    m = 1 << (size - 1)
    for i in range(8):
        if n & m: n = (n << 1) ^ poly
        else: n = n << 1
    m = (1 << size) - 1
    return n & m

def CrcXmodem_le(data):
    Crc16Tab = [CrcByte(i << 8,0x11021,16) for i in range(256)]
    i = 0
    for j in range(0, len(data)):
        out = Crc16Tab[((i >> 8) ^ data[j]) & 0xFF]
        i = out ^ (i << 8)
    return struct.pack('<H', i & 0xFFFF)

#(Un)scrambling algorithm
def firmware_xor(fwcontent):
    Key = [
        0x47, 0x22, 0xC0, 0x52, 0x5D, 0x57, 0x48, 0x94, 0xB1, 0x60, 0x60, 0xDB, 0x6F, 0xE3, 0x4C, 0x7C,
        0xD8, 0x4A, 0xD6, 0x8B, 0x30, 0xEC, 0x25, 0xE0, 0x4C, 0xD9, 0x00, 0x7F, 0xBF, 0xE3, 0x54, 0x05,
        0xE9, 0x3A, 0x97, 0x6B, 0xB0, 0x6E, 0x0C, 0xFB, 0xB1, 0x1A, 0xE2, 0xC9, 0xC1, 0x56, 0x47, 0xE9,
        0xBA, 0xF1, 0x42, 0xB6, 0x67, 0x5F, 0x0F, 0x96, 0xF7, 0xC9, 0x3C, 0x84, 0x1B, 0x26, 0xE1, 0x4E,
        0x3B, 0x6F, 0x66, 0xE6, 0xA0, 0x6A, 0xB0, 0xBF, 0xC6, 0xA5, 0x70, 0x3A, 0xBA, 0x18, 0x9E, 0x27,
        0x1A, 0x53, 0x5B, 0x71, 0xB1, 0x94, 0x1E, 0x18, 0xF2, 0xD6, 0x81, 0x02, 0x22, 0xFD, 0x5A, 0x28,
        0x91, 0xDB, 0xBA, 0x5D, 0x64, 0xC6, 0xFE, 0x86, 0x83, 0x9C, 0x50, 0x1C, 0x73, 0x03, 0x11, 0xD6,
        0xAF, 0x30, 0xF4, 0x2C, 0x77, 0xB2, 0x7D, 0xBB, 0x3F, 0x29, 0x28, 0x57, 0x22, 0xD6, 0x92, 0x8B,
    ]
    return bytes([a ^ b for a, b in zip(fwcontent, cycle(Key))])

def payload_xor(payload):
    Key = [ 0x16, 0x6C, 0x14, 0xE6, 0x2E, 0x91, 0x0D, 0x40, 0x21, 0x35, 0xD5, 0x40, 0x13, 0x03, 0xE9, 0x80, ]
    return bytes([a ^ b for a, b in zip(payload, cycle(Key))])

#================================================================================================================

class uvk5:
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        pass

    def __init__(self,portName='COM1'):
        self.debug = False if getenv('DEBUG') is None else True
        self.serial = serial.Serial()
        self.serial.baudrate = 38400
        self.serial.timeout = 1
        self.serial.port = portName
        self.currTime = int(time.time()).to_bytes(4,'little')

        ##Genuine tags for commands
        #Bootloader only (ROM flash mode)
        self.CMD_NVR_PUT       = b'\x16\x05' #0x0516 -> 0x0518/7 //NVRAM block WRITE. Dangerous for OFW! Max payload size is 104 bytes
        self.CMD_ROMB_PUT      = b'\x19\x05' #0x0519 -> 0x0518/A //ROM block WRITE. Caution! [needs platform check]
        self.CMD_FLASH_ON      = b'\x30\x05' #0x0530 -> 0x518:ok //Platform check ('02' or '*') then enter flash ROM write mode [needs handshake]

        #Normal boot
        self.CMD_CONNECT       = b'\x14\x05' #0x0514 -> 0x0515   //SendVersion() handshake
        self.CMD_EEPB_GET      = b'\x1B\x05' #0x051B -> 0x051C   //EEPROM_ReadBuffer [needs handshake]
        self.CMD_EEPB_PUT      = b'\x1D\x05' #0x051D -> 0x051E   //EEPROM_WriteBuffer [needs handshake]
        ##self.CMD_051F          = b'\x1F\x05' #0x51F seems sanity check: killed
        ##self.CMD_0521          = b'\x21\x05' #0x521 seems sanity check: killed
        self.CMD_RSSI_GET      = b'\x27\x05' #0x0527 -> 0x0528   //RSSI Query
        self.CMD_ADC_GET       = b'\x29\x05' #0x0529 -> 0x052A   //Batt voltage query
        self.CMD_MNG_LOGIN     = b'\x2D\x05' #0x052D -> 0x052E   //AES challenge auth routine
        self.CMD_CONN_TEST     = b'\x2F\x05' #0x052F -> 0x0515   //SendVersion() handshake for factory test

        self.CMD_RESET         = b'\xDD\x05' #0x05DD -> no reply //NVIC_SystemReset()
        self.CMD_6902          = b'\x02\x69' #0x6902 -> no reply //May force payload obfuscation?

        #For RAM Reader MOD
        self.CMD_MEMB_GET      = b'\xDB\x05' #0x05DD -> no reply //Raw serial dump whatever memory area

        #For Read/Write BK4819 register MOD
        self.CMD_BKREG_GET     = b'\x01\x06' #0x0601 -> 0x0602	//Reg value query
        self.CMD_BKREG_PUT     = b'\x03\x06' #0x0603 -> 0x0604	//Reg value write, replies new value

    def __del__(self):
        self.serial.close()
        return not self.serial.is_open

    def connect(self):
        self.serial.open()
        return self.serial.is_open

    def serial_get(self,buffSize=128):
        ciphertext = self.serial.read(buffSize)
        if ciphertext == b'': return None   #Just in case of empty buffer
        if self.debug: print('<raw<',ciphertext.hex())
        for i in range(0,len(ciphertext)):
            if ciphertext[i:i+2] == b'\xAB\xCD': break
        datagram = ciphertext[i:i+4] + payload_xor(ciphertext[i+4:-2]) + ciphertext[-2:]
        if self.debug: print('<dec<',datagram.hex())
        return datagram

    def serial_put(self,tag,value=b''):
        tlv = tag + struct.pack('<H',len(value))+ value
        datagram = (b'\xAB\xCD' + struct.pack('<H',len(tlv)) + tlv + CrcXmodem_le(tlv) + b'\xDC\xBA')
        if self.debug: print('>dec>',datagram.hex())
        ciphertext = datagram[:4] + payload_xor(datagram[4:-2]) + datagram[-2:]
        if self.debug: print('>raw>',ciphertext.hex())
        return self.serial.write(ciphertext)

    def get_fw_version(self,timeStamp=False):
        if not timeStamp: timeStamp = self.currTime
        self.serial_put(self.CMD_CONNECT, timeStamp)
        reply = self.serial_get()
        if reply is None: return False
        version = reply[8:24]
        upwd,pop = struct.unpack('<BB',reply[24:26])
        chlg = struct.unpack('<IIII',reply[28:44])
        return {'ver': version, 'prot': upwd, 'pin': pop, 'nonce': chlg}

    def get_cfg_mem(self,address,size=16):
        self.serial_put(self.CMD_EEPB_GET, struct.pack('<HH',0x1FFF & address,size) + self.currTime)
        reply = self.serial_get(size+16)
        return reply[12:-4]
        
    def set_cfg_mem(self,address,data):
        if not len(data)%8 and address+len(data) <= 8192:
            self.serial_put(self.CMD_EEPB_PUT, struct.pack('<HH',address, len(data)) + self.currTime + data)
            reply = self.serial_get(14)
            return reply[8:10]
        else: return False

    def nvram_flash(self,block):
        ## datagram: (0x1905 + 0x0C01) + Length + <block 104 bytes fixed>
        ## Offset forced to 0x200 (as sector 1 of 4. sector 0 is OTP only)
        self.serial_put(self.CMD_NVR_PUT, block)
        return self.serial_get(44)

    def block_flash(self,address,bksize,rgnend,block):
        ## datagram: (0x1905 + 0x0C01) + Length + timestamp(little) + offset(BIG) + regionEnd(BIG) + length(BIG) + 0x0000 + <block 256 bytes max> + Crc
        self.serial_put(self.CMD_ROMB_PUT, self.currTime + struct.pack('>HH',address,rgnend) + int.to_bytes(bksize,2,'big') + b'\x00\x00' + block)
        return self.serial_get(44)

    def rom_flash_set(self,req_ver='*'):
        self.serial_put(self.CMD_FLASH_ON, bytes(req_ver,'ascii') + bytes(16-len(req_ver)) + self.currTime)
        reply = self.serial_get(48)
        return False if reply is None else {'ret': reply[4:6], 'pfm': reply[13:18], 'boot': reply[24:31]}

    def reboot(self):
        self.serial_put(self.CMD_RESET)
        return True

    def get_fw_ver_mute(self,timeStamp=False):
        if not timeStamp: timeStamp = self.currTime
        self.serial_put(CMD_CONN_TEST, timeStamp)
        reply = self.serial_get()
        if reply is None: return False
        version = reply[8:24]
        upwd,pop = struct.unpack('<BB',reply[24:26])
        chlg = struct.unpack('<IIII',reply[28:44])
        return {'ver': version, 'prot': upwd, 'pin': pop, 'nonce': chlg}

    def try_login(self,resp):
        self.serial_put(self.CMD_MNG_LOGIN, resp)
        reply = self.serial_get(16)
        return False if reply is None else int.from_bytes(reply[8:9],"little")
        
    def get_rssi(self):
        self.serial_put(self.CMD_RSSI_GET)
        reply = self.serial_get(16)
        rssi,noise,glitch = struct.unpack('<HBB',reply[8:-4])
        rssi = rssi / 2 - 160
        return {'rssi':rssi, 'noise':noise, 'glitch':glitch, 'raw':reply[8:-4].hex()}

    def get_adc(self):
        self.serial_put(self.CMD_ADC_GET)
        reply = self.serial_get(16)
        a,b = struct.unpack('<HH',reply[8:-4])
        return {'volt': a, 'amp': b}

#Memory reader MOD
    def read_mem(self,mode,address,length):
        self.serial_put(self.CMD_MEMB_GET, struct.pack('<HHII', mode, 0, address, length))
        reply = self.serial.read(length)
        return False if reply is b'' else reply

#Read/Write BK4819 register MOD
    def get_reg(self, num):
        self.serial_put(self.CMD_BKREG_GET, struct.pack('<H', num))
        reply = self.serial_get(16)
        if reply == None: raise Exception('ERR: No response from transceiver!')
        dat,a,b = struct.unpack('<HBB',reply[8:-4])
        return {'reg': a, 'val': dat, 'sta': b}

    def put_reg(self, num, val):
        self.serial_put(self.CMD_BKREG_PUT, struct.pack('<HH', num, val))
        reply = self.serial_get(16)
        if reply == None: raise Exception('ERR: No response from transceiver!')
        dat,a,b = struct.unpack('<HBB',reply[8:-4])
        return {'reg': a, 'val': dat, 'sta': b}

##Experiments only
    def cmd051F(self):                                     ##NOT IMPLEMENTED
        test =  struct.pack('<I',433000000) +      \
                struct.pack('<H',0x00) +           \
                struct.pack('<H',0x7F) +           \
                struct.pack('<H',0xFF) +           \
                struct.pack('<H',0x00) +           \
                struct.pack('<H',0x7F) +           \
                struct.pack('<H',0xFF) +           \
                struct.pack('<H',1) 

        #self.serial_put(self.CMD_051F, test)
        #return self.serial_get(128)
        return False
