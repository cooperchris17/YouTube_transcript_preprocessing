'''
IMPORTANT: before running this script, create a new folder called 'short_texts'
in the directory that you run this script from, otherwise the files will be lost
(this might not be a big problem if you are deleting the files anyway)

This script will move all the short files in the previously created
'short_texts.txt' file to the new folder 'short_texts'
from there, you can do what you want with the texts
'''


import os, shutil, glob

# create a subfolder called 'short_texts' in the directory you are running the script from
destination = './short_texts'

# read the files from the text file 'short_texts.txt' and add them to a list
short_texts = []
with open('short_texts.txt') as f:
    lines = f.readlines()
    for line in lines:
        short_texts.append(line.strip())

# iterate through the directory and move files from the list to the new directory '/short_texts'
for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            if file in short_texts:
                shutil.move(file, destination)
