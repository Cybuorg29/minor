Python has a built-in zipfile module which provides support for reading and writing zip archives in native Python code. The module provides a ZipFile object with methods to read and extract contents of the archive, as well as a class representing individual entries such as files and directories.

For example, to extract an archive using the ZipFile object, you can do the following:

import zipfile

with zipfile.ZipFile("path/to/archive.zip", "r") as zf:
 zf.extractall("path/to/destination/directory")