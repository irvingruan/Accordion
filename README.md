Accordion
==========================

About
-----
Accordion is a ID3[1] tag reader and writer implemented purely in
Python. It supports all the current ID3 tag implementations including
ID3v1, ID3v1.1, ID3v2.2, ID3v2.3 and ID3v2.4.

Forked from [pytagger](http://www.liquidx.net/pytagger/).

Usage
-----
To extract the tag info from a MP3 using the tool, simply run:

`./accordion.py path/to/file.mp3`

As a library, just add inside whichever Python file you are using Accordion:
`import accordion`

There are two simple classes, ID3v2 and ID3v1. They both take a MP3
file as constructors:

`id3file = ID3v2('Song.mp3')`

Once the file is parsed, you can access the internal structures as:

* ID3v2.tag <-- Properties of the ID3v2 tag
  
* ID3v2.frames <-- A list of frames objects present in the tag
   
* ID3v2Frame.fid <-- frame ID, either 3 or 4 character string
   
* ID3v2Frame.fields <-- a tuple of frames

You can directly remove/edit/replace the frames and tag information
in the class and then commit to disk by executing:

`id3file.commit()`


Features
-----

* Reads ID3v1 and ID3v1.1 using the pyid3.ID3v1 class
* Reads ID3v2.2 to ID3v2.4 using the pyid3.ID3v2 class
* Decodes all text, url, comments, attachments frames
* Write to ID3v2.2 to ID3v2.4 frames
* Able to add ID3 tags from scratch to existing MP3s
* Only works on MP3s

Example Scripts
-----

* mp3check.py - Checks MP3s for ID3v2 and ID3v1 tags
* mp3conv.py  - Converts MP3 tags from one encoding to another,
			  also attempts to fill in missing ID3v2 tags with
			  information from ID3v1 tags, if they exists
* mp3stat.py  - Polls recursively a directory and outputs a list of
			  statistics about the files, including what version of
			  ID3v2 tags are in use and what frame types are present

Quirks
-----

**iTunes**

- iTunes uses SyncSafe encoding for the length/size field in the ID3v2
    Header, but doesn't use it for the ID3v2 Frame Headers.

**libid3tag**
  
- There seems to be a bug with libid3tag not setting the Restrictions
    bit in the ID3v2.4 Extensions Header, but attaching an extra byte
	for the field.

- Even when setting Unicode encoding, libid3tag does not set the
    encoding value for each text field to anything non-zero.


To Do
-----

 * Split classes into their own files.
 * FIX FIXMEs, especially regarding missing frame encoders/decoders
 * Properly use flags in ID3v2
 * Implement write feature for ID3v1
 * Strict checking for fields in ID3v2
 * Able to cross convert ID3 tags between 2.2, 2.3 and 2.4
 * Able to synchronise with ID3v1 tags (can be done externally)

References
-----
[1] [http://www.id3.org/id3v2.4.0-structure.txt](http://www.id3.org/id3v2.4.0-structure.txt)


Maintainers
-----

Irving Y. Ruan <irvingruan@gmail.com>


Legal
-----
Accordion is Copyright (c) 2012 Alastair Tse & Irving Ruan and is BSD licensed. The full text of the license can be found in LICENSE.
