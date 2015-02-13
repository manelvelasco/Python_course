#!/bin/bash
export LD_LIBRARY_PATH=/usr/local/lib/
~/bin/evince --editor="synctex edit -o %p:%x:%y:%o -x 'gvim +%%{line} %%{input}'" $1.pdf
