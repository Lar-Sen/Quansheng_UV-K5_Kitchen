##COMBO Mod
##051F UART command patch to RAM Reader, Ported to v2.00.31, updated
##ZVEI signalling function, to replace 2nd method for 1750Hz burst tone (press long-F1). Courtesy of LarSeN
##Limitation: Tone step is 10Hz. But you can set VERY long sequence if you wanna play.

#cmd05DBcode = b'\x10\xB5\x0A\x4B\x1A\x88\x01\x2A\x0D\xD1\x09\x4A\x51\x88\x10\x88\x09\x04\x01\x43\x07\x4A\x50\x88\x14\x88\x00\x04\x20\x43\x0B\xF0\xB3\xF8\x00\x20\x10\xBD\x08\x21\x03\x48\xF8\xE7\x88\x05\x00\x20\x8E\x05\x00\x20\x8A\x05\x00\x20\x68\x0D\x00\x00\x55\x6E\x6B\x6E\x20\x72\x65\x71\x00\x00'
cmd05DBcode = b'\x10\xB5\x81\x88\x01\x29\x12\xD1\x81\x68\x01\x22\xD2\x03\x01\x32\x92\x03\x91\x42\x0B\xD2\xC2\x89\x81\x89\x12\x04\x11\x43\x42\x89\x00\x89\x12\x04\x10\x43\x0B\xF0\xAF\xF8\x00\x20\x10\xBD\x0A\x21\x00\x48\xF8\xE7\x64\x0D\x00\x00\x43\x4D\x44\x3A\x45\x72\x72\x6F\x72\x21\x00\x00\x00\x00'
ZVEIcode = b'\xFE\xB5\x0B\xF0\xCE\xF9\xE0\x21\x09\x02\x70\x20\x0A\xF0\xF7\xF8\x03\x20\x09\xF0\x18\xFB\x09\xF0\xEC\xFF\x50\x20\x0C\xF0\xE7\xF9\x01\x26\x19\x48\x04\x21\x0B\xF0\x5E\xF9\x00\x24\x5C\x25\x7D\x44\x29\x5D\xCA\xB2\x05\x2C\x16\xDA\x00\x2A\x0E\xD0\x44\x32\x11\x48\x00\xBF\x42\x43\xD1\x0B\x71\x20\x0A\xF0\xD9\xF8\x0B\xF0\xB7\xF9\x46\x20\x0C\xF0\xCC\xF9\x0B\xF0\xA4\xF9\x08\x20\x0C\xF0\xC7\xF9\x62\x1C\xD4\xB2\xE4\xE7\x96\x42\x0A\xDA\x70\x1C\xC6\xB2\x06\x48\x04\x21\x0B\xF0\x12\xF9\x08\x20\x80\x01\x0C\xF0\xB8\xF9\xD0\xE7\x00\xF0\xAD\xF9\xFE\xBD\x2C\xA3\x33\x00\x00\x10\x06\x40'

#All 3 values below max to 255
repeat = 3
tonedur = 70
tonedelay = 8
#Warning! seqdelay takes only any of: 512, 256, 0. Zero is 128ms (to get NO delay, please un/comment related line below)
seqdelay = 512
pattern = b'\x30\x26\x48\x26\x48'	#Default is ZVEI-2 Emergency sequence for Channel E in Europe (Swiss - Italy - France)
##pattern = b'\x30\x26\x3B\xAC\x26'       #Emergency Channel E TEST sequence

#Pattern is a sequence of 10*kHz, minus 68.
#Example: 0x30 is 48. 48+68=116. This is 1160Hz tone.

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct

print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if fw[0x0D2C:0x0D2C+8] == b'\xF8\xB5\x04\x46\x38\x48\x00\x78':
    fw[0x0D2C:0x0D2C+70] = cmd05DBcode
    ##fw[0x0D2C+68:0x0E20] = b'\x00'*176   #Freed bytes to 00
    fw[0x0D2C+70:0x0E00] = ZVEIcode
    fw[0x0E00:0x0E00+32] = b'\x00'*32   #Free bytes for tone sequence
    fw[0x7B4A:0x7B4A+4] = b'\xF9\xF7\x12\xF9'
    fw[0x0DA6:0x0DA6+1] = len(pattern).to_bytes(1,'big')
    fw[0x0DC2:0x0DC2+1] = tonedur.to_bytes(1,'big')
    fw[0x0DCC:0x0DCC+1] = tonedelay.to_bytes(1,'big')
    fw[0x0DEA:0x0DEA+1] = int(seqdelay/4).to_bytes(1,'big')     #inter sequence delay, comment if needed
    ##fw[0x0DEA:0x0DEA+2] = b'\x00\x00'   #NO inter sequence delay, UNcomment if needed
    fw[0x0E00:0x0E00+1+len(pattern)] = pattern + repeat.to_bytes(1,'big')
else:
    print('Error: original function for 051F command was not found!');sys.exit(1)

open(sys.argv[1],'wb').write(fw)
