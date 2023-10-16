## Custom welcome/boot screen with adjustable length
## adapted/modded by LarSeN
## Use Img2Cpp.htm or http://en.radzio.dxp.pl/bitmap_converter/ to convert
# img2cpp.htm settings:
# Draw mode: Vertical
# Inverted colors
# Size: Width 128, Height: (choose<64 by multiples of 8, then adjust offset_from_top accordingly)
# Bit/pixel: 1bpp

clean_pattern = 0x44 # clearing pattern (0:clean screen - FF:black screen - AD,88,49,55,33...: horizontal stripes)
offset_from_top = 16

#MARIO
custom_logo = bytearray([ \
0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x80, 0x40, 0x20, 0x20, 0x10, 0x08, 0x08, 0x04, 
0x02, 0xe2, 0x11, 0x50, 0x30, 0xb0, 0xd0, 0x10, 0xe0, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x88, 0x74, 0x88, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x80, 0x40, 0x40, 0x38, 0x08, 0x06, 0x04, 0x03, 0x02, 0x03, 0x06, 0x04, 0x98, 0x08, 
0x0c, 0x50, 0x30, 0x50, 0xe0, 0x00, 0x00, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 0x25, 
0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x00, 0x00, 0x64, 0x12, 0x12, 0x0a, 0x1c, 
0xf8, 0x14, 0x22, 0xc2, 0x02, 0x02, 0x04, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0x80, 0xc0, 
0xa0, 0xa0, 0x90, 0x88, 0x88, 0x84, 0xa2, 0x92, 0x14, 0x08, 0x04, 0x02, 0x02, 0x01, 0x02, 0x02, 
0x04, 0x08, 0x90, 0xc4, 0xe2, 0x62, 0x61, 0xc0, 0x40, 0x40, 0xc0, 0xc0, 0x30, 0x00, 0x00, 0x00, 
0x00, 0x07, 0x08, 0x08, 0x0d, 0x0d, 0x08, 0x08, 0x07, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x78, 0x57, 0xa2, 0x57, 0x78, 0x80, 0x00, 0x00, 
0x02, 0x0f, 0x08, 0x1a, 0x1d, 0x38, 0x36, 0x28, 0x34, 0x3a, 0x18, 0x0f, 0x18, 0x32, 0x34, 0x28, 
0x34, 0x38, 0x0b, 0x0e, 0x03, 0x01, 0x00, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 0x82, 
0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0xff, 0x80, 0x80, 0x40, 0x20, 0x20, 0x10, 0x0f, 0xf8, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 0x08, 
0x08, 0x4a, 0xad, 0x5a, 0xad, 0x5a, 0xfd, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x30, 
0x90, 0xdb, 0xfb, 0xfc, 0xf9, 0xd9, 0xf8, 0xfa, 0x5a, 0x66, 0x63, 0x71, 0x00, 0x10, 0x20, 0x20, 
0x40, 0x40, 0x80, 0x00, 0x00, 0xe0, 0xd0, 0xa8, 0xd8, 0xa8, 0xd8, 0xb0, 0xe0, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0xf8, 0x47, 0xa2, 0x15, 0x08, 0x15, 0xa2, 0x47, 0xf8, 0x80, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 
0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd0, 0xd0, 0xd0, 0xd8, 0xd4, 0xd2, 0xd2, 
0xdf, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xde, 0xd1, 0xd1, 0xd1, 0xd1, 0xd1, 0xd1, 0xd1, 
0xd1, 0xd5, 0xdb, 0xd5, 0xdb, 0xd5, 0xde, 0xd0, 0xd0, 0x10, 0xf0, 0x80, 0x00, 0xd0, 0xf0, 0x00, 
0xf1, 0x10, 0x00, 0xb1, 0xd1, 0x00, 0xf0, 0xb0, 0x00, 0xf0, 0x10, 0xe0, 0x80, 0xd0, 0xd0, 0xd0, 
0xd0, 0xd0, 0xd0, 0xd1, 0xd0, 0xd0, 0xd3, 0xd4, 0xd4, 0xd4, 0xd4, 0xd3, 0xd0, 0xd0, 0xd0, 0xd0, 
0xd0, 0xd0, 0xd0, 0xd0, 0xdc, 0xd3, 0xd0, 0xd0, 0xd8, 0xd5, 0xd2, 0xd5, 0xd8, 0xd0, 0xd0, 0xd3, 
0xdc, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 
0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd0, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5, 0xd5])

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

if len(fw)!=58820: print('Incorrect firmware size! Exiting'); sys.exit(1)
else:
    print('Size OK. Adding custom boot image to firmware')

#shellcode = b'\x30\xB5\x55\x22\x06\x49\x07\x48\xF6\xF7\x2A\xFB\x06\x4A\x07\x49\x07\x48\xF6\xF7\x13\xFB\x01\xF0\xAD\xFD\x01\xF0\x6F\xFD\x30\xBD\x00\x04\x00\x00\x84\x06\x00\x20\xCC\xCC\xCC\xCC\xBB\xBB\xBB\xBB\xAA\xAA\xAA\xAA'
shellcode = b'\x70\xB5\x55\x22\x06\x49\x07\x48\xF1\xF7\xFA\xFD\x06\x4A\x07\x49\x07\x48\xF1\xF7\xE3\xFD\xFD\xF7\xA1\xF8\xFD\xF7\x63\xF8\x70\xBD\x00\x04\x00\x00\x84\x06\x00\x20\xCC\xCC\xCC\xCC\xBB\xBB\xBB\xBB\xAA\xAA\xAA\xAA'

shellcode = bytearray(shellcode)
shellcode[2] = clean_pattern   

shellcode = shellcode.replace(struct.pack('<I',0xAAAAAAAA), struct.pack('<I',0x20000684 + (16*offset_from_top)))  #destination of copymem
shellcode = shellcode.replace(struct.pack('<I',0xBBBBBBBB), struct.pack('<I',len(fw)+52))                         #source of copymem
shellcode = shellcode.replace(struct.pack('<I',0xCCCCCCCC), struct.pack('<I',len(custom_logo)))                   #len of copymem

#fw[0x9B3C:0x9B3C+len(shellcode)] = shellcode  # replace boot screen function at address 0x9B3C with above shellcode
fw[0x9C28:0x9C28+8] = b'\x04\xF0\xCC\xFC\x00\xBF\xF9\xE7'  #replace ST7565_FillScreen(0xFF) with our function call

fw += shellcode     #append our function code
fw += custom_logo   #append logo at the end of file

#fw[0xD264:0xD264+2] = b'\xC0\x00'  # 1 second delay
#fw[0xD264:0xD264+2] = b'\x00\x01'  # 2 seconds delay
fw[0xD262:0xD262+4] = b'\xBB\x20\x00\x01'  # ~3 seconds delay
#fw[0xD262:0xD262+4] = b'\xFA\x20\x00\x01'  # 4 seconds delay

open(sys.argv[1],'wb').write(fw)

