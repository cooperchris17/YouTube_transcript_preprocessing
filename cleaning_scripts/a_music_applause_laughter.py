'''
This script deletes all of the lines with '[Music]', '[Laughter]' or '[Applause]' in them
In YouTube ASR transcripts, these only appear in a line with no other text
It's a good idea to make a copy of the folder (and subfolders) containing the transcripts
Then run the script in the new folder
This script will amend every plain text file in the folder (and in any subfolders) from where it is run
'''

import glob, os
# this will iterate through all files in the directory and any subfolders
for file in glob.iglob('**', recursive=True):
    # if the file is a file (not a directory)
    if os.path.isfile(file):
        # avoid editing .py files, etc
        if file.endswith('.txt'):
            # remove '[Music]' lines
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    # iterate all lines from file
                    for line in input:
                        # if text matches then don't write it
                        if line.strip('\n') != '[Music]':
                            output.write(line)

            # replace file with original name
            os.replace('temp.txt', file)

            # remove '[Applause]' lines
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    for line in input:
                        if line.strip('\n') != '[Applause]':
                            output.write(line)

            os.replace('temp.txt', file)

            # remove '[Laughter]' lines
            with open(file, 'r') as input:
                with open('temp.txt', 'w') as output:
                    for line in input:
                        if line.strip('\n') != '[Laughter]':
                            output.write(line)

            os.replace('temp.txt', file)
