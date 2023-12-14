# Quansheng_UV-K5_Kitchen
Mods collection for the Quansheng VHF/UHF transceiver I use or made.

![Alt text](screen_preview.jpg?raw=true "Main display preview after mod")

### News
- 2.01.32 official fixes now backported. No need to upgrade.
- Anti-counterfeiting measures removed
- Updated config file for unbricking via OpenOCD using ST-Link v2 probe (the `unbrick_toolkit`)
- Added python flasher tool. No more need for scrambled firmware and QS Updater app. Implements partial flashing too.
- Added bootloader mod to get partial flashing working, and hide unique device identification.
- Refreshed libuvk5.py and some python utils to match present knowledge
- Added login function and ability to remove a forgotten user password to regain uart config access

`v2.01.31`
Firmware ROM patches written in Python, and targeted for 2.01.31 UV-K5 firmware version (inheriting fixes from 2.01.32 firmware).
A ready to flash .bin firmware file is provided, updated everytime needed.

`Bootloader_mods`
One mod for the moment: Implement select block updating. No more need to flash full image.

`Unbrick_toolkit`
A ready-to-use preconfigured OpenOCD package (Windows x64) with only necessary files needed to unbrick and update any UV-K5 using a cheap ST-Link v2 debug probe.
Easy custom made commands include uv_flash_bl (bootloader recovery), uv_flash_fw (main firmware update), uv_fastflash_bl and uv_fastflash_fw (ways faster than the classic others, may have issues: Readme for more info)

`Updater`
Latest Quansheng decompressed windows tool to flash firmware to DP32G030 MCU in bootloader's "ROM update" mode (PTT+PowerOn), using a standard Kenwood serial cable (USB or RS-232 adapter)

Have a look to other README files in subdirectories :)