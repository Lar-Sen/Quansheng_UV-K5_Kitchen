## Replaces big and small digits
## modified by larsen: VCR corrected - BBC mode 7 - Geneva

#VCR
##big_digits=b'\x00\x00\xF8\xFC\x0E\x06\x86\xC6\xE6\x6E\xFC\xF8\x00\x00\x00\x1F\x3F\x76\x67\x63\x61\x60\x70\x3F\x1F\x00\x00\x00\x00\x00\x18\x1C\xFE\xFE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x7F\x7F\x60\x60\x00\x00\x00\x00\x00\x18\x1C\x8E\x86\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x7E\x7F\x63\x61\x61\x61\x61\x61\x60\x60\x00\x00\x00\x18\x1C\x0E\x06\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x18\x38\x70\x60\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x80\xC0\xE0\x70\x38\x1C\xFE\xFE\x00\x00\x00\x00\x00\x07\x07\x06\x06\x06\x06\x7F\x7F\x06\x06\x00\x00\x00\x7E\x7E\x66\x66\x66\x66\x66\xE6\xC6\x86\x00\x00\x00\x18\x38\x70\x60\x60\x60\x60\x70\x3F\x1F\x00\x00\x00\xF8\xFC\x8E\x86\x86\x86\x86\x8E\x1C\x18\x00\x00\x00\x1F\x3F\x71\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x06\x06\x06\x06\x06\x86\xC6\xE6\x7E\x3E\x00\x00\x00\x00\x00\x00\x00\x7F\x7F\x01\x00\x00\x00\x00\x00\x00\x78\xFC\xCE\x86\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x1E\x3F\x73\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x78\xFC\xCE\x86\x86\x86\x86\x8E\xFC\xF8\x00\x00\x00\x18\x38\x71\x61\x61\x61\x61\x71\x3F\x1F\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01\x00\x00'

#BBCmode7
##big_digits=b'\x00\x00\xF0\xF8\x1C\x0E\x06\x06\x0E\x1C\xF8\xF0\x00\x00\x00\x0F\x1F\x38\x70\x60\x60\x70\x38\x1F\x0F\x00\x00\x00\x00\x00\x18\x1C\xFE\xFE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x7F\x7F\x60\x60\x00\x00\x00\x00\x00\x18\x1C\x0E\x06\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x78\x7C\x6E\x67\x63\x61\x61\x61\x60\x60\x00\x00\x00\x06\x06\x06\x86\xC6\xE6\xF6\xBE\x1E\x0E\x00\x00\x00\x18\x38\x70\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x80\xC0\xE0\x70\x38\x1C\xFE\xFE\x00\x00\x00\x00\x00\x07\x07\x06\x06\x06\x06\x7F\x7F\x06\x06\x00\x00\x00\x7E\x7E\x66\x66\x66\x66\x66\xE6\xC6\x86\x00\x00\x00\x18\x38\x70\x60\x60\x60\x60\x70\x3F\x1F\x00\x00\x00\xE0\xF0\xB8\x9C\x8E\x86\x86\x86\x00\x00\x00\x00\x00\x1F\x3F\x71\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x06\x06\x06\x06\x86\xC6\xE6\x76\x3E\x1E\x00\x00\x00\x00\x00\x7E\x7F\x03\x01\x00\x00\x00\x00\x00\x00\x00\x78\xFC\xCE\x86\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x1E\x3F\x73\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x78\xFC\xCE\x86\x86\x86\x86\x8E\xFC\xF8\x00\x00\x00\x00\x00\x61\x61\x61\x71\x39\x1D\x0F\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x60\x60\x60\x60\x60\x60\x60\x60\x00'
big_digits=b'\x00\x00\xF0\xF8\x1C\x0E\x06\x06\x0E\x1C\xF8\xF0\x00\x00\x00\x0F\x1F\x38\x70\x60\x60\x70\x38\x1F\x0F\x00\x00\x00\x00\x00\x18\x1C\xFE\xFE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x60\x60\x7F\x7F\x60\x60\x00\x00\x00\x00\x00\x18\x1C\x0E\x06\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x78\x7C\x6E\x67\x63\x61\x61\x61\x60\x60\x00\x00\x00\x06\x06\x06\x86\xC6\xE6\xF6\xBE\x1E\x0E\x00\x00\x00\x18\x38\x70\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x80\xC0\xE0\x70\x38\x1C\xFE\xFE\x00\x00\x00\x00\x00\x07\x07\x06\x06\x06\x06\x7F\x7F\x06\x06\x00\x00\x00\x7E\x7E\x66\x66\x66\x66\x66\xE6\xC6\x86\x00\x00\x00\x18\x38\x70\x60\x60\x60\x60\x70\x3F\x1F\x00\x00\x00\xE0\xF0\xB8\x9C\x8E\x86\x86\x86\x00\x00\x00\x00\x00\x1F\x3F\x71\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x06\x06\x06\x06\x86\xC6\xE6\x76\x3E\x1E\x00\x00\x00\x00\x00\x7E\x7F\x03\x01\x00\x00\x00\x00\x00\x00\x00\x78\xFC\xCE\x86\x86\x86\x86\xCE\xFC\x78\x00\x00\x00\x1E\x3F\x73\x61\x61\x61\x61\x73\x3F\x1E\x00\x00\x00\x78\xFC\xCE\x86\x86\x86\x86\x8E\xFC\xF8\x00\x00\x00\x00\x00\x61\x61\x61\x71\x39\x1D\x0F\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x40\x40\x40\x40\x40\x40\x40\x40\x40\x00\x00'

#OldComputer
## modified by @DO7OO
##big_digits  =b'\x00\xFE\xFF\x01\x01\x01\x01\x01\x81\x81\xFF\xFF\x00\x00\x7F\x7F\x40\x40\x40\x40\x40\x7F\x7F\x7F\x7F\x00\x00\x00\x00\x00\x00\x00\x80\x80\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7F\x7F\x7F\x7F\x00\x00\x00\x00\x01\x81\x81\x81\x81\x81\x81\x81\x81\xFF\xFE\x00\x00\x7F\x7F\x7F\x7F\x40\x40\x40\x40\x40\x40\x40\x00\x00\x81\x81\x81\x81\x81\x81\x81\x81\x81\xFF\xFE\x00\x00\x40\x40\x40\x40\x40\x40\x40\x7F\x7F\x7F\x7F\x00\x00\x7F\xFF\x80\x80\x80\x80\x80\x80\x80\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7F\x7F\x7F\x7F\x00\x00\xFE\xFF\x81\x81\x81\x81\x81\x81\x81\x81\x81\x00\x00\x40\x40\x40\x40\x40\x40\x40\x7F\x7F\x7F\x7F\x00\x00\xFE\xFF\x81\x81\x81\x81\x81\x81\x81\x81\x81\x00\x00\x7F\x7F\x7F\x7F\x40\x40\x40\x40\x40\x7F\x7F\x00\x00\x01\x01\x01\x01\x01\x01\x01\x81\x81\xFF\xFE\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7F\x7F\x7F\x7F\x00\x00\xFE\xFF\x81\x81\x81\x81\x81\x81\x81\xFF\xFF\x00\x00\x7F\x7F\x40\x40\x40\x40\x40\x7F\x7F\x7F\x7F\x00\x00\xFE\xFF\x81\x81\x81\x81\x81\x81\x81\xFF\xFF\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7F\x7F\x7F\x7F\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x03\x03\x03\x03\x03\x03\x03\x03\x03\x00\x00'
##small_digits=b'\x00\x7E\x41\x41\x41\x79\x7F\x00\x00\x00\x00\x78\x7F\x00\x00\x79\x79\x49\x49\x49\x4E\x00\x49\x49\x49\x49\x79\x7E\x00\x07\x08\x08\x08\x78\x7F\x00\x4E\x49\x49\x49\x79\x79\x00\x7E\x79\x49\x49\x49\x79\x00\x01\x01\x01\x01\x79\x7E\x00\x7E\x49\x49\x49\x79\x7F\x00\x0E\x09\x09\x09\x79\x7F\x00\x08\x08\x08\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'

#Terminus
##small_digits=b'\x00\x7E\x41\x41\x41\x79\x7F\x00\x00\x00\x00\x78\x7F\x00\x00\x79\x79\x49\x49\x49\x4E\x00\x49\x49\x49\x49\x79\x7E\x00\x07\x08\x08\x08\x78\x7F\x00\x4E\x49\x49\x49\x79\x79\x00\x7E\x79\x49\x49\x49\x79\x00\x01\x01\x01\x01\x79\x7E\x00\x7E\x49\x49\x49\x79\x7F\x00\x0E\x09\x09\x09\x79\x7F\x00\x08\x08\x08\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'

#Genuine
##small_digits=b'\x00\x3E\x41\x41\x41\x41\x3E\x00\x00\x42\x7F\x40\x00\x00\x00\x62\x51\x51\x49\x49\x46\x00\x22\x41\x49\x49\x4D\x32\x00\x18\x14\x12\x11\x7F\x10\x00\x27\x45\x45\x45\x45\x39\x00\x3E\x49\x49\x49\x49\x30\x00\x01\x71\x09\x05\x03\x00\x00\x36\x49\x49\x49\x49\x36\x00\x46\x49\x49\x49\x29\x1E\x00\x08\x08\x08\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'

#Geneva
small_digits=b'\x00\x00\x3E\x41\x41\x41\x3E\x00\x00\x00\x02\x7F\x00\x00\x00\x00\x42\x61\x51\x49\x46\x00\x00\x21\x49\x4D\x4B\x31\x00\x00\x18\x14\x12\x7F\x10\x00\x00\x27\x45\x45\x45\x39\x00\x00\x3C\x4A\x49\x49\x30\x00\x00\x01\x01\x71\x0D\x03\x00\x00\x36\x49\x49\x49\x36\x00\x00\x06\x49\x49\x29\x1E\x00\x00\x40\x40\x40\x40\x40\x00\x00\x00\x00\x00\x00\x00'

##--------------------- do not modify below this line ---------------------------------------------------
import os,sys,struct
print('* Running',os.path.basename(sys.argv[0]),'mod...')
fw =  bytearray(open(sys.argv[1],'rb').read())

fw[0xD576:0xD576+len(big_digits)]   = big_digits
fw[0xD694:0xD694+len(small_digits)] = small_digits

if len(fw)<0xEFFF:
    open(sys.argv[1],'wb').write(fw)
else:
    print('ERROR file too big!')