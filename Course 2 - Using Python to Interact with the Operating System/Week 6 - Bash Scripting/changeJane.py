#!/usr/bin/env python3

import sys
import subprocess

file = open(sys.argv[1])
for line in file:
        source = line.strip()
        dest = line.replace("jane", "jdoe")
        subprocess.run(['mv', ''+source, ''+dest])
file.close()


# Please note: for some reason this code appends a question mark at end of file name after it has been replaced. 
# You still pass the 'Qwiklabs Assessment: Editing Files Using Substrings' even though the output is not quite as expected 

