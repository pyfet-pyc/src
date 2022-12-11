from __future__ import print_function

import os
import shutil
import sys

EXT_VIDEO_LIST = ["FLV", "WMV", "MOV", "MP4", "MPEG", "3GP", "MKV", "AVI"]
EXT_IMAGE_LIST = ["JPG", "JPEG", "GIF", "PNG", "SVG"]
EXT_DOCUMENT_LIST = [
    "DOC",
    "DOCX",
    "PPT",
    "PPTX",
    "PAGES",
    "PDF",
    "ODT",
    "ODP",
    "XLSX",
    "XLS",
    "ODS",
    "TXT",
    "IN",
    "OUT",
    "MD",
]
EXT_MUSIC_LIST = ["MP3", "WAV", "WMA", "MKA", "AAC", "MID", "RA", "RAM", "RM", "OGG"]
EXT_CODE_LIST = ["CPP", "RB", "PY", "HTML", "CSS", "JS"]
EXT_EXECUTABLE_LIST = ["LNK", "DEB", "EXE", "SH", "BUNDLE"]
EXT_COMPRESSED_LIST = [
    "RAR",
    "JAR",
    "ZIP",
    "TAR",
    "MAR",
    "ISO",
    "LZ",
    "7ZIP",
    "TGZ",
    "GZ",
    "BZ2",
]

# Taking the location of the Folder to Arrange
try:
    destLocation = str(sys.argv[1])
except IndexError:
    destLocation = str(input("Enter the Path of directory: "))
