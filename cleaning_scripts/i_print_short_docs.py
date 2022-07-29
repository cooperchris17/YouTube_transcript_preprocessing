'''
export list of all files shorter than 75 tokens to a text file 'short_texts.txt'
'''

import os
from nltk.corpus import PlaintextCorpusReader

# specify root directory, in this case, current directoty
corpus_root = './'
# get PlaintextCorpusReader to read all of the text files in the directory
corpus = PlaintextCorpusReader(corpus_root, '.*\.txt') # doctest: +SKIP
# loop through the files and delete files shorter than the set length

file_names = []
for doc in corpus.fileids():
    # specify the file length by changing the number here
    if len(corpus.words(doc)) <= 75:
        file_names.append(doc)
        with open('short_texts.txt', 'w') as output:
            print('\n'.join(file_names), file=output)
