
# FirmwareFudger
## Intro:

This code is for automated analysis of files you may find around the internet. Primarily it was coded for the investigation of firmwares of devices. But you can use it generally for pattern recognition.

The original version had been built in 2007. In the last weeks, i had started to fix a lot of code, add features or clean some parts up. 

FirmwareFudger is far from what it's goal is, but it is already handy :)


## How to use the tool:

Get some help (or simply give no argument at all):
` %./ffudger.py -h `
Output:
```
usage: FirmwareFudger v0.5.2 by dash (May of 2019) [-h] [-f INFILE]
                                                   [-o OUTDIR] [-O OUTPREFIX]
                                                   [-x] [-F] [-S]
                                                   [-Sl STR_MINLEN]
                                                   [-Sf STR_FILTER] [-M]
                                                   [-Fp LONELYPLUGIN]
                                                   [-Fc FF_CAT] [-Fl]
                                                   [-Flc FUDGELIST_CAT]
                                                   [--threads THREADS] [-v]
                                                   [--debug] [-r] [-V]

FirmwareFudger, written to do better firmware analysis

optional arguments:
  -h, --help            show this help message and exit
  -f INFILE, --input-file INFILE
                        define the file to analyze
  -o OUTDIR, --outdir OUTDIR
                        define the directory to save extracted files and logs
                        to
  -O OUTPREFIX, --output-prefix OUTPREFIX
                        define the prefix for the extracted name (default: FF-
                        Extract)
  -x, --extract         flag if you want to extract found files
  -F, --fudge           use fudge mode (FirmwareFudgers own database)
  -S, --strings         run strings on file and conduct analysis
  -Sl STR_MINLEN, --strings-len STR_MINLEN
                        the minimum length for string check
  -Sf STR_FILTER, --strings-filter STR_FILTER
                        the strings check filter, use regular expressions
  -M, --magic           use magic mode (libmagic database)
  -Fp LONELYPLUGIN, --fudge-plugin LONELYPLUGIN
                        run only one specified plugin test
  -Fc FF_CAT, --fudge-category FF_CAT
                        run only a section of possible plugins (e.g. EXEC)
  -Fl, --fudge-list     show plugins of FirmwareFudger
  -Flc FUDGELIST_CAT, --fudge-list-cat FUDGELIST_CAT
                        show plugins of defined group
  --threads THREADS     define the value of maximum threads used, default is
                        20
  -v, --verbose         run in verbose mode
  --debug               run in debug mode
  -r, --report          create a report for the session
  -V, --version         show version and tool information
```

List all FirmwareFudger internal database magics:

``` %./ffudger.py -Fl

 FS:
                - MSDOS - MSDOS - Filesystem
                - CRAMFS1 - CRAMFS - Compressed ROMFS
                - CRAMFS2 - CRAMFS2 - Compressed ROMFS
                - ROM1FS - ROM1FS - ROM FILE SYSTEM
                - SQUASHFS - SQUASHFS - Big Endian

 [...] 
```

Around 86 supported magics right now.

List all FirmwareFudger internal database magics for a certain category:

```
%./ffudger.py -Flc CRYPTO

 [+] CRYPTO:
                - DSAPRIV - DSAPRIV - Private Key in DSA Format
                - RSAPRIV - RSAPRIV - Private Key in RSA Format
                - SSHDSS - SSHDSS - Public ssh key
                - CACERT - CACERT - Certificate Format
                - CERTREQ - CERTREQ - Certificate Request Format
                - PGPMSG - PGPMSG - Pretty Good Privacy Message Format
```

Searching for all  patterns:

```
%./ffudger.py -f /bin/ls 

 [+] Open /bin/ls
 [+] Filename /bin/ls
 [+] Size 134.45K - 137680B
 [+] User 0
 [+] Group 0
 [+] Checking for all FF plugins
 [+] FOUND ELF at Offset 0 to 4
 [+] Found 1 possible types

```

Search with all magics of FF database and extract the results:

```
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
```

Check that file with "file":
```
% file _bin_ls/FF-Extract-True-0.elf
_bin_ls/FF-Extract-True-0.elf: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0
```

If no directory is given, FF will create one, given by the name of the to analyse file. However, you can of course set one:

```
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
```


Searching for just one patterntype:

```
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
```

Searching for a class of patterns:

```
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
```

## Magic FF Database

This is my approach 2008 back to build up an own database of interesting magic headers. It is
sort of outdated nowadays as we have magic. However, it can be quickly enhanced for your matters
as it is quite easy to understand. In the future i might change it to a (No)Sql database, for 
easier use.
If you got magic headers from analysis you want to share, not part of libmagic or
not described correctly you are more then welcome.

## Supply/strings.txt

Ok, what is this feature you might ask. First, lets do a cat on supply/strings.txt:

```
linux;Linux string has been found; possibly linux OS or file;http://www.kernel.org
kernel;Kernel strings has been found; sneak around and check if more information is existing;hexdump -C
supertask;Supertask(RTOS) found;google 
trontask;Trontask(RTOS) found;google 
ILC 150 GSM Upgrade;inline gsm modem;https://www.phoenixcontact.com/online/portal/de?uri=pxc-oc-itemdetail:pid=2916545&library=dede&tab=1
SPI Flash Image; SPI access available;http://linux-sunxi.org/Bootable_SPI_flash
/etc;linux etc directory;google
```

This is a CSV oriented file, the delimiter is ';'. The idea is to place strings and sort of 
description to support analysis of firmwares or files found. It is not made as a place for magic
headers but to aid on certain interesting strings which can be found. 
It is *definitly* a place for strings which name the Operating System used or special build 
parts or alike. I'am quite happy if you add new items, add a merge request or send it to 
me via E-Mail.




# Roadmap

## Roadmap Version 0.6.0

For release 0.6.0 the following features are planed:

- logging import, for better logging and output
- enhance strings function
- libmagic feature, to enhance the checking database
- entropy scan
- setup.py setuptools installer
- bruteforce unpacker :)

## Roadmap Version 0.7.0

For release 0.7.0 the following features are planed:

- design plugin interface for extra code and 3rd party plugins
- automatic unpackers for lzma,bzip,zip,gzip and others
- sanity checks for packers (decrease counts of false positives like .gz or .arj)
- enhance reporting feature
- add pdf output format

# Contact:

Although, i do have quite an feature list by myself, I'am quite happy if you have feature requests or even better input from your analysis to add to FirmwareFudger. 
Also, open up bugs if you find them, i will find the time to fix them.
Everything you do not want to share directly over github.com send here:

d4shmail@gmail.com

# Disclaimer:

None :)

# Outro:

That's it guys'n'girls. I hope you can use it for some good. For any further questions on the code you can contact me via email
