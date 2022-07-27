'''
This script will output lines of text that contain upper case letters,
along with the filename, to a plain text file
'''

import glob, os, re

# read all the txt files in the directory (and in other directories in that path)
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            f = open(file, "r")
            lines = f.readlines()

            # define punctuation
            punc = r'\w*[A-Z]\w*'

            # print out all the lines with punctuation
            # output format is filename + line of text with punctuation
            for line in lines:
                if re.search(punc, line):
                    with open('upper_check_out.txt', 'a') as outf:
                        print(file, ': ', line, file=outf)
