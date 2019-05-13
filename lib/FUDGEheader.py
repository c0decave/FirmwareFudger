#complete list
TYPES		= 0x00

#categories
FS			= 0x00
EXEC		= 0x01
PACKERS		= 0x02
DOCS		= 0x03
BOOT		= 0x04
ASM			= 0x05
PICTURES	= 0x06
DEVICES		= 0x07
#ROUTERS		= 0x08
CRYPTO		= 0x08

#Filesystem Type Definitions
MSDOS		= 0x00
CRAMFS1		= 0x01
CRAMFS2		= 0x02		#difference is another searchstring
ROM1FS		= 0x03
SQUASHFS1	= 0x04		#difference is another searchstring
SQUASHFS2	= 0x05
FAT32		= 0x06
CDUNIX		= 0x07
ADF			= 0x08
SGI			= 0x09
SGIXFS		= 0x0a
ST40		= 0x0b
CBM			= 0x0c
WINIMAGE	= 0x0d
COB			= 0x0e
UFS1		= 0x0f
QEMU1		= 0x10
JFFSL		= 0x11
JFFSB		= 0x12
JFFS2L		= 0x13
JFFS2B		= 0x14
FAT12		= 0x15
FAT16		= 0x16

#Executeable File Definitions
ELF			= 0x00
BFLT		= 0x01
PE			= 0x02
MSDOSCOM	= 0x03
DOSCOM		= 0x04
SPSSPORTABLE= 0x05
SPSSSYSTEM	= 0x06
PPCPEF		= 0x07

#Packing Specific definitions
ZIP1		= 0x00
ZIP2		= 0x01
BZIP		= 0x02
GZIP		= 0x03
ACE			= 0x04
TAR			= 0x05
TRX1		= 0x06
TRX2		= 0x07
LZMA		= 0x08
UPX			= 0x09
GNUTAR		= 0x0A
CRUSH		= 0x0B
HLSQZ		= 0x0B
SQWEZ		= 0x0C
HPAK		= 0x0D
LZOP		= 0x0E
MDCD		= 0x0F
MSCOMPRESS	= 0x10
INSTALLSHIELD	= 0x11
PAQ			= 0x12
JARARJ		= 0x13
STUFFIT		= 0x14
VAX3		= 0x15
VAX5		= 0x16
ARCHIVE		= 0x17
ARCHIVEFILE	= 0x18
HRB			= 0x19
RISCOS		= 0x1a
HAP			= 0x1b
LIM			= 0x1c
FREEZE		= 0x1d
ZOO			= 0x1e
RAR			= 0x1f
EET			= 0x20
RZIP		= 0x21
SQSH		= 0x22
ISC			= 0x23
NWFILE		= 0x24
DSIGDCC		= 0x25
ARJ			= 0x26

#Document Fileformats
PDF			= 0x00
DOC			= 0x01
RTF			= 0x02

#Bootloader Definitions
UBOOT		= 0x00

#Assembler object codes
AVR			= 0x00

#Image Files(pictures etc.)
GIMPXCF		= 0x00

#Devices Specific Firmware characteristics
LTRX1		= 0x00
LTRX2		= 0x01
WGR614BOOT	= 0x02
WGR614		= 0x03

#Router Specific Firmware characteristics specifications

#Crypto stuff, certificates, keys, typical indications of crypto
DSAPRIV		= 0x00 #-----BEGIN DSA PRIVATE KEY-----	    -----END DSA PRIVATE KEY-----
RSAPRIV		= 0x01 #-----BEGIN RSA PRIVATE KEY-----	    -----END RSA PRIVATE KEY-----
SSHPUB		= 0x02 # ssh-dss
CACERT		= 0x03 #-----BEGIN CERTIFICATE-----	    -----END CERTIFICATE-----
CERTREQ		= 0x04 #-----BEGIN CERTIFICATE REQUEST----- -----END CERTIFICATE REQUEST-----
PGPMSG		= 0x05 #-----BEGIN PGP MESSAGE-----	    -----END PGP MESSAGE-----

#Header definitions
HEADER1		= 0x01		#start header
HEADER2		= 0x02		#stop trailer/header
NAME		= 0x03		#the format name
DESC		= 0x04		#teh description
SUFFIX		= 0x05		#the ending of the file, some tools want to have a proper ending, gzip for instance
CHANCE		= 0x06		#chance calculator, if at least "chance" bytes are correct print out possibility...
TOOLS		= 0x07		#tools of trade to work with that kind of files


#Filesystem Specifications
#
#still much too add
###########################################
TYPES = { FS: { \
		MSDOS:{ \
			HEADER1: ('M','Z','H','H'),\
			HEADER2: None,\
			NAME: 'MSDOS',\
			DESC: "MSDOS - Filesystem",\
			SUFFIX: 'img',\
			CHANCE: 2},
		CRAMFS1:{ \
			HEADER1: ('\x45','\x3d','\xcd','\x28'),\
			HEADER2: None,\
			NAME: 'CRAMFS1',\
			DESC: "CRAMFS - Compressed ROMFS",\
			SUFFIX: 'img',\
			CHANCE: 2},

		CRAMFS2:{ \
			HEADER1: ('C','o','m','p','r','e','s','s','e','d','\x20','R','O','M','F','S'),\
			HEADER2: None,\
			NAME: 'CRAMFS2',\
			DESC: "CRAMFS2 - Compressed ROMFS",\
			SUFFIX: 'img',\
			CHANCE: 8},

		ROM1FS:{ \
			HEADER1: ('-','r','o','m','1','f','s'),\
			HEADER2: None,\
			NAME: 'ROM1FS',\
			DESC: "ROM1FS - ROM FILE SYSTEM",\
			SUFFIX: 'img',\
			CHANCE: 3},

		SQUASHFS1:{ \
			HEADER1: ('h','s','q','s'),\
			HEADER2: None,\
			NAME: 'SQUASHFS',\
			DESC: "SQUASHFS - Big Endian",\
			SUFFIX: 'img',\
			CHANCE: 2},

		SQUASHFS2:{ \
			HEADER1: ('s','q','s','h'),\
			HEADER2: None,\
			NAME: 'SQUASHFS2',\
			DESC: "SQUASHFS - Little Endian",\
			SUFFIX: 'img',\
			CHANCE: 2},

		FAT32:{ \
			HEADER1: ('\x46','\x41','\x54','\x33','\x32'),\
			HEADER2: None,\
			NAME: 'FAT32',\
			DESC: "FAT32 - Filessystem",\
			SUFFIX: 'img',\
			CHANCE: 2},

		FAT12:{ \
			HEADER1: ('\x46','\x41','\x54','\x31','\x32'),\
			HEADER2: None,\
			DESC: "FAT12 - Filessystem",\
			NAME: 'FAT12',\
			SUFFIX: 'img',\
			CHANCE: 2},

		FAT16:{ \
			HEADER1: ('\x46','\x41','\x54','\x31','\x36'),\
			HEADER2: None,\
			NAME: 'FAT16',\
			DESC: "FAT16 - Filessystem",\
			SUFFIX: 'img',\
			CHANCE: 2},

		CDUNIX:{ \
			HEADER1: ('\x01','\x43','\x44','\x30','\x30','\x31','\x01'),\
			HEADER2: None,\
			NAME: 'CDUNIX',\
			DESC: "CDUNIX - Filessystem",\
			SUFFIX: 'img',\
			CHANCE: 2},

		ADF:{ \
			HEADER1: ('D','O','S','\x00'),\
			HEADER2: None,\
			NAME: 'ADF',\
			DESC: "ADF - Amiga Filessystem",\
			SUFFIX: 'img',\
			CHANCE: 2},

		SGI:{ \
			HEADER1: ('\x0B','\xE5','\xA9','\x41'),\
			HEADER2: None,\
			NAME: 'SGI',\
			DESC: "SGI - SGI disk label (volume header)",\
			SUFFIX: 'img',\
			CHANCE: 2},

		SGIXFS:{ \
			HEADER1: ('\x58','\x46','\x53','\x42'),\
			HEADER2: None,\
			NAME: 'SGIXFS',\
			DESC: "SGI XFS - filesystem data",\
			SUFFIX: 'img',\
			CHANCE: 2},

		ST40:{ \
			HEADER1: ('\x13','\xa9','\xf1','\x7e'),\
			HEADER2: None,\
			NAME: 'ST40',\
			DESC: "ST40 - component image format",\
			SUFFIX: 'img',\
			CHANCE: 2},
		CBM:{ \
			HEADER1: ('C','B','M'),\
			HEADER2: None,\
			NAME: 'POWER64',\
			DESC: "Power 64 - C64 Emulator Snapshot",\
			SUFFIX: 'img',\
			CHANCE: 2},

		WINIMAGE:{ \
			HEADER1: ('W','I','N','I','M','A','G','E'),\
			HEADER2: None,\
			NAME: 'WinImage',\
			DESC: "WinImage - WinImage Archive data",\
			SUFFIX: 'img',\
			CHANCE: 2},
		COB:{ \
			HEADER1: ('C','o','B','1'),\
			HEADER2: None,\
			NAME: 'COB1',\
			DESC: "CoB1 - lantronix html/webserver filesystem",\
			SUFFIX: 'img',\
			CHANCE: 2},
		UFS1:{ \
			HEADER1: ('\x00','\x01','\x19','\x54'),\
			HEADER2: None,\
			NAME: 'UFS1',\
			DESC: "UFS1 - Unix Fast File system [v1] (little-endian)",\
			SUFFIX: 'img',\
			CHANCE: 2},
		QEMU1:{ \
			HEADER1: ('\x51','\x46','\x49','\xfb'),\
			HEADER2: None,\
			NAME: 'QEMU1',\
			DESC: "QEMU1 - Qemu Image, Format: Qcow",\
			SUFFIX: 'img',\
			CHANCE: 2},
		JFFSL:{ \
			HEADER1: ('\x31','\x39','\x38','\x34'),\
			HEADER2: None,\
			NAME: 'JFFS1_LE',\
			DESC: "JFFS1 - version 1, little endian",\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			SUFFIX: 'img',\
			CHANCE: 2},

		JFFSB:{ \
			HEADER1: ('\x34','\x38','\x39','\x31'),\
			HEADER2: None,\
			NAME: 'JFFS1_BE',\
			DESC: "JFFS1 - version 1, big endian",\
			SUFFIX: 'img',\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2},

		JFFS2L:{ \
			HEADER1: ('\x85','\x19','\x03','\x20'),\
			HEADER2: None,\
			NAME: 'JFFS2_LE',\
			DESC: "JFFS2 - version 2, little endian",\
			SUFFIX: 'img',\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2},

		JFFS2B:{ \
			HEADER1: ('\x19','\x85','\x20','\x03'),\
			HEADER2: None,\
			NAME: 'JFFS2_BE',\
			DESC: "JFFS2 - version 2, big endian",\
			SUFFIX: 'img',\
			TOOLS: "mtd-tools, mkfs.jffs etc.",\
			CHANCE: 2}
		},

	EXEC: {
		ELF:{ \
			HEADER1: ('\x7f','E','L','F'),\
			HEADER2: None,\
			NAME: 'ELF',\
			DESC: "ELF - File Format",\
			SUFFIX: 'elf',\
			CHANCE: 2},
		BFLT:{ \
			HEADER1: ('b','F','L','T'),\
			HEADER2: None,\
			NAME: 'BFLT',\
			DESC: "bFLT - File Format",\
			SUFFIX: 'bflf',\
			CHANCE: 2},
		PE:{ \
			HEADER1: ('P','E','\x00','\x00'),\
			HEADER2: None,\
			NAME: 'PE',\
			DESC: "PE - File Format",\
			SUFFIX: 'exe',\
			CHANCE: 2},
		MSDOSCOM:{ \
			HEADER1: ('\xfc','\x57','\xf3','\xa5','\xc3'),\
			HEADER2: None,\
			NAME: 'COM',\
			DESC: "COM executable for MS-DOS",\
			SUFFIX: 'com',\
			CHANCE: 2},
		DOSCOM:{ \
			HEADER1: ('\xfc','\x57','\xf3','\xa4','\xc3'),\
			HEADER2: None,\
			NAME: 'COMDOS',\
			DESC: "COM executable for DOS",\
			SUFFIX: 'com',\
			CHANCE: 2},
		SPSSPORTABLE:{ \
			HEADER1: ('\xc1','\xe2','\xc3','\xc9'),\
			HEADER2: None,\
			NAME: 'SPSS',\
			DESC: "SPSS Portable File",\
			SUFFIX: None,\
			CHANCE: 2},
		SPSSSYSTEM:{ \
			HEADER1: ('$','F','L','2'),\
			HEADER2: None,\
			NAME: 'SPSS2',\
			DESC: "SPSS System File",\
			SUFFIX: None,\
			CHANCE: 2},
		PPCPEF:{ \
			HEADER1: ('J','o','y','!','p','e','f','f','p','w','p','c'),\
			HEADER2: None,\
			NAME: 'PPC_PEF',\
			DESC: "header for PowerPC PEF executable",\
			SUFFIX: None,\
			CHANCE: 2}
	},

	PACKERS:  {
		ZIP1:{ \
			HEADER1: ('\x50','\x4b','\x03','\x04'),\
			HEADER2: None,\
			NAME: 'ZIP1',\
			DESC: "ZIP1 - Phil Katz ",\
			SUFFIX: 'zip',\
			CHANCE: 2},
		ZIP2:{ \
			HEADER1: ('\x50','\x4b','\x01','\x02'),\
			HEADER2: None,\
			NAME: 'ZIP2',\
			DESC: "ZIP2 - Phil Katz ",\
			SUFFIX: 'zip',\
			CHANCE: 2},
		BZIP:{ \
			HEADER1: ('\x42','\x5a','\x68'),\
			HEADER2: None,\
			NAME: 'BZIP',\
			DESC: "BZIP - a block-sorting file compressor",\
			SUFFIX: 'bz2',\
			CHANCE: 2},
		GZIP:{ \
			HEADER1: ('\x1f','\x8b'),\
			HEADER2: None,\
			NAME: 'GZIP',\
			DESC: "GZIP - Lempel-Ziv coding (LZ77)",\
			SUFFIX: 'gz',\
			CHANCE: 2},
		ACE:{ \
			HEADER1: ('*','*','A','C','E','*','*'),\
			HEADER2: None,\
			NAME: 'ACE',\
			DESC: "ACE - e-merge GmbH - winace.com",\
			SUFFIX: 'ace',\
			CHANCE: 2},
		TAR:{ \
			HEADER1: ('\x00','u','s','t','a','r','\x00'),\
			HEADER2: None,\
			NAME: 'TAR',\
			DESC: "TAR - tape archiver",\
			SUFFIX: 'tar',\
			CHANCE: 2},
		TRX1:{ \
			HEADER1: ('\x30','\x52','\x44','\x48'),\
			HEADER2: None,\
			NAME: 'TRX1',\
			DESC: "TRX1 - ",\
			SUFFIX: None,\
			CHANCE: 2},
		TRX2:{ \
			HEADER1: ('H','D','R','0'),\
			HEADER2: ('0','R','D','H'),\
			NAME: 'TRX2',\
			DESC: "TRX2 - ",\
			SUFFIX: None,\
			CHANCE: 2},
		LZMA:{ \
			HEADER1: ('\x5d','\x00','\x00','\x80'),\
			HEADER2: None,\
			NAME: 'LZMA',\
			DESC: "LZMA - Lempel-Ziv-Markov chain-Algorithm",\
			SUFFIX: 'lzma',\
			CHANCE: 2},
		UPX:{ \
			HEADER1: ('U','P','X','!'),\
			HEADER2: None,\
			NAME: 'UPX',\
			DESC: "UPX - Ultimate Packer for eXecuteables",\
			SUFFIX: 'upx',\
			CHANCE: 2},
		GNUTAR:{ \
			HEADER1: ('u','s','t','a','r','\x20','\x20','\x00'),\
			HEADER2: None,\
			NAME: 'GNUTAR',\
			DESC: "GNUTAR - tar == teer + tape archiver",\
			SUFFIX: 'tar',\
			CHANCE: 2},
		CRUSH:{ \
			HEADER1: ('C', 'R', 'U', 'S', 'H'),\
			HEADER2: None,\
			NAME: 'CRUSH',\
			DESC: "CRUSH - Crush archive data",\
			SUFFIX: None,\
			CHANCE: 2},

		HLSQZ:{ \
			HEADER1: ('H', 'L', 'S', 'Q', 'Z'),\
			HEADER2: None,\
			NAME: 'HLSQZ',\
			DESC: "HLSQZ - Squeeze It archive data",\
			SUFFIX: None,\
			CHANCE: 2},

		SQWEZ:{ \
			HEADER1: ('S', 'Q', 'W', 'E', 'Z'),\
			HEADER2: None,\
			NAME: 'SQWEZ',\
			DESC: "SQWEZ - archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		HPAK:{ \
			HEADER1: ('H', 'P', 'A', 'K'),\
			HEADER2: None,\
			NAME: 'HPAK',\
			DESC: "HPAK - archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		LZOP:{ \
			HEADER1: ('\x89','\x4c','\x5a','\x4f','\x00','\x0d','\x0a','\x1a','\x0a'),\
			HEADER2: None,\
			NAME: 'LZOP',\
			DESC: "LZOP - lzop comrpressed data",\
			SUFFIX: None,\
			CHANCE: 2},
		MDCD:{ \
			HEADER1: ('M', 'D', 'm', 'd'),\
			HEADER2: None,\
			NAME: 'MDCD',\
			DESC: "MDCD - archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		MSCOMPRESS:{ \
			HEADER1: ('\x88','\xf0','\x27'),\
			HEADER2: None,\
			NAME: 'MS',\
			DESC: "MS Compress archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		INSTALLSHIELD:{ \
			HEADER1: ('\x13','\x5d','\x65','\x8c'),\
			HEADER2: None,\
			NAME: 'MSIS',\
			DESC: "InstallShield - Z archive Data",\
			SUFFIX: None,\
			CHANCE: 2},
		PAQ:{ \
			HEADER1: ('\xaa','\x40','\x5f','\x77','\x1f','\xe5','\x82','\x0d'),\
			HEADER2: None,\
			NAME: 'PAQ',\
			DESC: "PAQ - archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		JARARJ:{ \
			HEADER1: ('\x1a','J','a','r','\x1b'),\
			HEADER2: None,\
			NAME: 'JAR',\
			DESC: "JAR (ARJ Software, Inc.) archive data",\
			SUFFIX: 'arj',\
			CHANCE: 2},
		STUFFIT:{ \
			HEADER1: ('S','t','u','f','f','I','t'),\
			HEADER2: None,\
			NAME: 'STUFFIT',\
			DESC: "StuffIt Archive",\
			SUFFIX: 'stuffit',\
			CHANCE: 2},
		VAX3:{ \
			HEADER1: ('\x65','\xff','\x00','\x00'),\
			HEADER2: None,\
			NAME: 'VAX3',\
			DESC: "VAX 3.0 archive",\
			SUFFIX: None,\
			CHANCE: 2},
		VAX5:{ \
			HEADER1: ('\x3c','\x61','\x72','\x3e'),\
			HEADER2: None,\
			NAME: 'VAX5',\
			DESC: "VAX 5.0 archive",\
			SUFFIX: None,\
			CHANCE: 2},
		ARCHIVE:{ \
			HEADER1: ('=','<','a','r','>'),\
			HEADER2: None,\
			NAME: 'AR',\
			DESC: "archive",\
			SUFFIX: 'ar',\
			CHANCE: 2},
		ARCHIVEFILE:{ \
			HEADER1: ('21','3c','61','72'),\
			HEADER2: None,\
			NAME: 'ARfile',\
			DESC: "archive file",\
			SUFFIX: 'ar',\
			CHANCE: 2},
		HRB:{ \
			HEADER1: ('\xc0','H','R','B'),\
			HEADER2: None,\
			NAME: 'HRB',\
			DESC: "Harbour HRB file",\
			SUFFIX: 'hrb',\
			CHANCE: 2},
		RISCOS:{ \
			HEADER1: ('A','r','c','h','i','v','e'),\
			HEADER2: None,\
			NAME: 'RISCOS',\
			DESC: "RISC OS archive (ArcFS format)",\
			SUFFIX: None,\
			CHANCE: 2},
		HAP:{ \
			HEADER1: ('\x91','\x33','H','F'),\
			HEADER2: None,\
			NAME: 'HAP',\
			DESC: "HAP archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		LIM:{ \
			HEADER1: ('L','I','M','\x1a'),\
			HEADER2: None,\
			NAME: 'LIM',\
			DESC: "LIM archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		FREEZE:{ \
			HEADER1: ('\x1f','\x9f','\x4a','\x10','\x0a'),\
			HEADER2: None,\
			NAME: 'FREEZE',\
			DESC: "Freeze archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		ZOO:{ \
			HEADER1: ('\xfd','\xc4','\xa7','\xdc'),\
			HEADER2: None,\
			NAME: 'ZOO',\
			DESC: "Zoo archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		RAR:{ \
			HEADER1: ('R','a','r','!'),\
			HEADER2: None,\
			NAME: 'RAR',\
			DESC: "RAR archive data",\
			SUFFIX: 'rar',\
			CHANCE: 2},
		EET:{ \
			HEADER1: ('\x1e','\xe7','\xff','\x00'),\
			HEADER2: None,\
			NAME: 'EET',\
			DESC: "EET archive",\
			SUFFIX: None,\
			CHANCE: 2},
		RZIP:{ \
			HEADER1: ('R','Z','I','P'),\
			HEADER2: None,\
			NAME: 'RZIP',\
			DESC: "rzip compressed data",\
			SUFFIX: None,\
			CHANCE: 2},
		SQSH:{ \
			HEADER1: ('S','Q','S','H'),\
			HEADER2: None,\
			NAME: 'SQUISH',\
			DESC: "squished archive data (Acorn RISCOS)",\
			SUFFIX: None,\
			CHANCE: 2},
		ISC:{ \
			HEADER1: ('I','S','c','('),\
			HEADER2: None,\
			NAME: 'CAB',\
			DESC: "InstallShield CAB",\
			SUFFIX: None,\
			CHANCE: 2},
		NWFILE:{ \
			HEADER1: ('P','a','c','k','e','d','\\',' ','F','i','l','e','\\'),\
			HEADER2: None,\
			NAME: 'NETWARE',\
			DESC: "Personal NetWare Packed File",\
			SUFFIX: None,\
			CHANCE: 2},
		DSIGDCC:{ \
			HEADER1: ('D','S','I','G','D','C','C'),\
			HEADER2: None,\
			NAME: 'CROSSEPAC',\
			DESC: "CrossePAC archive data",\
			SUFFIX: None,\
			CHANCE: 2},
		ARJ:{ \
			HEADER1: ('\x60','\xea'),\
			HEADER2: None,\
			NAME: 'ARJ',\
			DESC: "ARJ",\
			SUFFIX: 'arj',\
			CHANCE: 2}
	},

	DOCS: { \
		PDF:{ \
			HEADER1: ('\x25','\x50','\x44','\x46','\x2e'),\
			HEADER2: None,\
			NAME: 'PDF',\
			DESC: "PDF - Portable Document Format",\
			SUFFIX: 'pdf',\
			CHANCE: 2},
		DOC:{ \
			HEADER1: ('\xd0','\xcf','\x11','\xe0','\xa1','\xb1','\x1a','\xe1'),\
			HEADER2: None,\
			NAME: 'DOC',\
			DESC: "DOC - Microsoft Document Format",\
			SUFFIX: 'doc',\
			CHANCE: 2},
		RTF:{ \
			HEADER1: ('{','\\','\\','r','t','f'),\
			HEADER2: None,\
			NAME: 'RTF',\
			DESC: "RTF - Rich Text Format data",\
			SUFFIX: 'rtf',\
			CHANCE: 2}
	},

	BOOT: { \
		UBOOT:{ \
			HEADER1: ('\x27','\x05','\x19','\x56'),\
			HEADER2: None,\
			NAME: 'UBOOT',\
			DESC: "UBOOT - PPCBoot Image - maybe bootloader",\
			SUFFIX: 'uboot',\
			CHANCE: 2}

},
	ASM: { \
		AVR:{ \
			HEADER1: ('a','v','a','o','b','j'),\
			HEADER2: None,\
			NAME: 'AVR',\
			DESC: "AVR assembler object code",\
			SUFFIX: 'avr',\
			CHANCE: 2}
},
	PICTURES: { \
		GIMPXCF:{ \
			HEADER1: ('g','i','m','p','\\',' ','x','c','f'),\
			HEADER2: None,\
			NAME: 'GIMP_XCF',\
			DESC: "GIMP XCF image data",\
			SUFFIX: 'xcf',\
			CHANCE: 2}
},

	DEVICES: { \
		LTRX1:{ \
			HEADER1: ('D','S','T','-','L','T','R','X'),\
			HEADER2: None,\
			NAME: 'LTRX1',\
			DESC: "LTRX1 - Lantronics Firmware Part detected",\
			SUFFIX: None,\
			CHANCE: 2},

		LTRX2:{ \
			HEADER1: ('L','T','R','X'),\
			HEADER2: None,\
			NAME: 'LTRX2',\
			DESC: "LTRX2 - Lantronics Firmware Part detected",\
			SUFFIX: None,\
			CHANCE: 2},

		WGR614BOOT:{ \
			HEADER1: ('*','#','$','^'),\
			HEADER2: None,\
			NAME: 'NETGEAR_BOOT',\
			DESC: "NETGEAR WGR614v9 Bootware - unknown bootloader maybe",\
			SUFFIX: None,\
			CHANCE: 2},

		WGR614:{ \
			HEADER1: ('@','U','1','2','H','0','9','4','T'),\
			HEADER2: None,\
			NAME: 'NETGEAR_FW',\
			DESC: "NETGEAR WGR614v9 Firmware",\
			SUFFIX: None,\
			CHANCE: 2}

	},

	CRYPTO: {
		DSAPRIV:{ \
			HEADER1: ('-----BEGIN DSA PRIVATE KEY-----'),\
			HEADER2: ('-----END DSA PRIVATE KEY-----'),\
			NAME: 'DSAPRIV',\
			DESC: "DSAPRIV - Private Key in DSA Format",\
			SUFFIX: None,\
			CHANCE: 2},

		RSAPRIV:{ \
			HEADER1: ('-----BEGIN RSA PRIVATE KEY-----'),\
			HEADER2: ('-----END RSA PRIVATE KEY-----'),\
			NAME: 'RSAPRIV',\
			DESC: "RSAPRIV - Private Key in RSA Format",\
			SUFFIX: None,\
			CHANCE: 2},

		SSHPUB:{ \
			HEADER1: ('ssh-dss'),\
			HEADER2: None,\
			NAME: 'SSHDSS',\
			DESC: "SSHDSS - Public ssh key",\
			SUFFIX: None,\
			CHANCE: 2},

		CACERT:{ \
			HEADER1: ('-----BEGIN CERTIFICATE-----'),\
			HEADER2: ('-----END CERTIFICATE-----'),\
			NAME: 'CACERT',\
			DESC: "CACERT - Certificate Format",\
			SUFFIX: None,\
			CHANCE: 2},

		CERTREQ:{ \
			HEADER1: ('-----BEGIN CERTIFICATE REQUEST-----'),\
			HEADER2: ('-----END CERTIFICATE REQUEST-----'),\
			NAME: 'CERTREQ',\
			DESC: "CERTREQ - Certificate Request Format",\
			SUFFIX: None,\
			CHANCE: 2},
			
		PGPMSG:{ \
			HEADER1: ('-----BEGIN PGP MESSAGE-----'),\
			HEADER2: ('-----END PGP MESSAGE-----'),\
			NAME: 'PGPMSG',\
			DESC: "PGPMSG - Pretty Good Privacy Message Format",\
			SUFFIX: None,\
			CHANCE: 2},
}
}

TYPES_DEF = {	'FS':FS,\
				'EXEC':EXEC,\
				'PACKERS':PACKERS,\
				'DOCS':DOCS,\
				'BOOT':BOOT,\
				'ASM':ASM,\
				'PICTURES':PICTURES,\
				'DEVICES':DEVICES,\
				'CRYPTO':CRYPTO
			}
