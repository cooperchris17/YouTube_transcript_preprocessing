'''
This script changes censored words '[ __ ]' to 'tamn'
Like the other scripts, it amends every file in the folder and subfolder
that the script is run from
'''

import re, os, glob

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                filedata = input.read()
                # re.sub follows this format
                filedata = re.sub('\[ __ \]', 'tamn', filedata)

                with open('temp.txt', 'w') as output:
                    output.write(filedata)

            # replace file with original name
            os.replace('temp.txt', file)
