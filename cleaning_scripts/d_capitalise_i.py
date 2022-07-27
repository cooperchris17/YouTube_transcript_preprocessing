'''
This script capitalises all occurences of lower case 'i'
If 'I' is not capitalised it can cause problems for some taggers

e.g. the MAT Tagger, which is built on the Stanford tagger,
consistently tagged 'i' as a foreign word
'''


import glob, os, re

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            # replace 'i' with 'I'
            with open(file, 'r') as input:
                filedata = input.read()
                # re.sub follows this format
                filedata = re.sub(r'\bi\b', 'I', filedata)

                with open('temp.txt', 'w') as output:
                    output.write(filedata)

            # replace file with original name
            os.replace('temp.txt', file)
