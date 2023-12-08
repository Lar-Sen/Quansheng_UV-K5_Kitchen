## BootLoader mod for Quansheng UV-K5

### Prerequisites 
 - Cheap ST-Link v2 debug probe "baite" or similar (you may have to use another "interface init" OpenOCD script)
 - OpenOCD with UV-K5 specific target script (a ready to use package sits in this repo)
 - Kenwood type serial comms cable (USB or RS-232)
 - Pre-modded file is provided. If you prefer apply mod by yourself, you'll find 2 delta patch files in IPS and BPS format
 - Genuine bootloader dump. For now, bootloader version doesn't matter, as it implements a modded check to be compatible with any >=v2 firmware ('*' joker still available)

### What it does
 - allows for PARTIAL flashing of selected sectors. Genuine bootloader code just erase all 120 sectors as soon as it gets data for sector 1, rendering full flash mandatory.
   This mod circonvents this, you can flash any block in 0x1000-0xFF00 range.
   If you enjoy modding and testing, this should improve a lot CPU flash memory lifespan. Also, reflashing only modded sectors saves a precious time.
 - accepts any firmware version, provided it is at least v2. '*' joker still accepted too.
 - hides your CPU serial number from "Hello" packets following cmd 0x530. Welcome data is now "518  UV-K5 Ready".
   Main reason for this is not really privacy; in fact I use a mod to make CPUid the "emergency masterkey" which is unique for each device (not Quansheng's universal one)
 - stays compatible with genuine flasher tool
 - k5prog tool from SQ5BPF should be fully working after applying mod. You can also use my `flashtool.py` which implements partial flashing.

## Notes
 - Remember that ERASE size is 2 times bigger than a block's size: 512 bytes.
   When sending data to flash, make sure that provided offset is 512 byte aligned, and has at least a length bigger than 256 bytes.
   You can flash only 256 bytes but it serves nothing excepted at the very end of the firmware, as the resulting sector would be <your data>+256 bytes of 'FF'.
 - As inner working is "erase 1 sector, flash 2 blocks and so on" : Flashing full ROM takes a little more time (a few seconds) than genuine. Not an issue here.
<hr>

### How to

With provided OpenOCD package (the unbrick_toolkit), and transceiver connected and ready (note: with battery charged..as I experienced very strange issues with a flat battery!), just launch this at a command prompt:

`openocd -f interface/stlink.cfg -f target/dp32g030.cfg -c "uv_flash_bl bootloader_UVK5_(partial_flashing)_MODDED.bin" -c "shutdown"`

No need to reflash main firmware after that.

<hr>

	LarSeN.

