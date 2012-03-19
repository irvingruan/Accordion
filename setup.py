#!/usr/bin/env python

import sys
assert sys.version >= '2.3', "Requires Python v2.3 or above"
from distutils.core import setup, Extension

setup(
    name = "accordion",
    version = "0.5",
    author = "Irving Ruan",
    author_email = "irvingruan@gmail.com",
    url = "http://www.liquidx.net/pytagger/",
	description = "Python ID3 Tag Reader and Writer Module",
	long_description = "An ID3v1 and ID3v2 tag reader and writer module in pure Python. Supports all standards including ID3v1, ID3v1.1, ID3v2.2, ID3v2.3 and ID3v2.4",
	license = "BSD",
	py_modules = ["libacc", "libacc.id3v1", "libacc.id3v2", "libacc.exceptions",
				  "libacc.constants", "libacc.utility", "libacc.id3v2frame",
				  "libacc.encoding", "libacc.debug"],
    scripts = ["mp3check.py", "apic.py"]
)
