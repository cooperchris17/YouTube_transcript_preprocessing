'''
this script iterates through all files in all directories
(from where the script is run)
it prints the filename and any word in square brackets (only .txt files)

After deleting [Music], [Applause], [Laughter], this will show where words
have been censored, as they are they only other words containing square brackets
in YouTube ASR transcripts the words can be checked by using the video id
contaiend in the filename to watch the video
'''

import glob, os, re

for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            f = open(file, "r")
            raw = f.readlines()

            for line in raw:
                if re.search('\[.*\]', line):
                    with open('___brackets_out.txt', 'a') as outf:
                        print(file, ': ', line, file=outf)
