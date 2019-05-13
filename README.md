
# FirmwareFudger
##Intro:

This code is for automated analysis of files you may find around the internet. Primarily it was coded for the investigation of firmwares of devices. But you can use it generally for pattern recognition.

The original version had been built in 2007. In the last weeks, i had started to fix a lot of code, add features or clean some parts up. 

FirmwareFudger is far from what it's goal is, but it is already handy :)


##How to use the tool:

Get some help (or simply give no argument at all):
> %./ffudger.py -h 

List all FirmwareFudger internal database magics:

> %./ffudger.py -Fl
>
> FS:
>                - MSDOS - MSDOS - Filesystem
>                - CRAMFS1 - CRAMFS - Compressed ROMFS
>                - CRAMFS2 - CRAMFS2 - Compressed ROMFS
>                - ROM1FS - ROM1FS - ROM FILE SYSTEM
>                - SQUASHFS - SQUASHFS - Big Endian
>
> [...] 

Around 86 supported magics right now.

List all FirmwareFudger internal database magics for a certain category:

%./ffudger.py -Flc CRYPTO

[+] CRYPTO:
                - DSAPRIV - DSAPRIV - Private Key in DSA Format
                - RSAPRIV - RSAPRIV - Private Key in RSA Format
                - SSHDSS - SSHDSS - Public ssh key
                - CACERT - CACERT - Certificate Format
                - CERTREQ - CERTREQ - Certificate Request Format
                - PGPMSG - PGPMSG - Pretty Good Privacy Message Format

Searching for all  patterns:

%./ffudger.py -f /bin/ls 

[+] Open /bin/ls
[+] Filename /bin/ls
[+] Size 134.45K - 137680B
[+] User 0
[+] Group 0
[+] Checking for all FF plugins
[+] FOUND ELF at Offset 0 to 4
[+] Found 1 possible types

Search with all magics of FF database and extract the results:

./ffudger.py -f /bin/ls -x

[+] Creating directory _bin_ls
[+] Open /bin/ls
[+] Found 1 interesting string(s) during analysis
[+] Filename /bin/ls
[+] Size 134.45K - 137680B
[+] User 0
[+] Group 0
[+] Checking for all FF plugins
[+] FOUND ELF at Offset 0 to 4
[+] FILENAME: _bin_ls/FF-Extract-True-0.elf

% file _bin_ls/FF-Extract-True-0.elf
_bin_ls/FF-Extract-True-0.elf: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0

If no directory is given, FF will create one, given by the name of the to analyse file. However, you can of course set one:


./ffudger.py -f /bin/ls -x -o test_dir

[+] Creating directory test_dir
[+] Open /bin/ls
[+] Found 1 interesting string(s) during analysis
[+] Filename /bin/ls
[+] Size 134.45K - 137680B
[+] User 0
[+] Group 0
[+] Checking for all FF plugins
[+] FOUND ELF at Offset 0 to 4
[+] Found 1 possible types
[+] FILENAME: test_dir/FF-Extract-True-0.elf

Searching for just one patterntype:

%./ffudger.py -f /bin/ls -Fp ELF

[+] Fudger Version 0.5.2 - Fileinformation
[+] Filename /bin/ls
[+] Size 134.45K - 137680B
[+] User 0
[+] Group 0
[+] Analyzing for ELF
[.] Waiting for threads to finish 1
[+] FOUND ELF at Offset 0 to 4
[+] Found 1 possible types
[+] FILENAME: _bin_ls/FF-Extract-True-0.elf


Searching for a class of patterns:

%python fudge.py -f /bin/ls -P EXEC

[+] Open /bin/ls
[+] Fudger Version 0.5.2 - Fileinformation
[+] Filename /bin/ls
[+] Size 134.45K - 137680B
[+] User 0
[+] Group 0
[+] Testing only for EXEC plugins
[+] FOUND ELF at Offset 0 to 4
[.] Waiting for threads to finish 2
[.] Waiting for threads to finish 1
[+] Found 1 possible types
[+] FILENAME: _bin_ls/FF-Extract-True-0.elf

Outro:
======

That's it guys'n'girls. I hope you can use it for some good. For any further questions on the code you can contact me via email

Disclaimer:
===========

None :)
