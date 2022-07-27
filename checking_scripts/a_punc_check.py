'''
This script will export any lines of text that contain punctuation to a
plain text file, along with the filenames containing the text

Looking at punctuation like this is useful to see what kind of sentence
punctuation is in texts (none in YouTube ASR texts from 2021)
- also it can be useful to check how other punctuation is used, like hyphens,
if there are any question marks, etc.
'''

import glob, os, re

# read all the txt files in the directory (and in other directories in that path)
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            f = open(file, "r")
            lines = f.readlines()

            # define punctuation
            punc = r'[.?\-",]+'

            # print out all the lines with punctuation
            # output format is filename + line of text with punctuation
            for line in lines:
                if re.search(punc, line):
                    with open('___punc_check_out.txt', 'a') as outf:
                        print(file, ': ', line, file=outf)
