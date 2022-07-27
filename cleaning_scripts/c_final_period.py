'''
This script deletes the periods that are at the end of a line
they always followed a number and were not sentence boundaries
'''

import glob, os, re

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            # replace 'period space' with 'space'
            with open(file, 'r') as input:
                filedata = input.read()
                # use re to read the period as a period
                # re.sub follows this format
                filedata = re.sub('\.\n', '\n', filedata)

                with open('temp.txt', 'w') as output:
                    output.write(filedata)

            # replace file with original name
            os.replace('temp.txt', file)
