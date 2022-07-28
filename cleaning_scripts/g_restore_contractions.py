'''
This script restores contractions that were split with the previous script
('capitalise_caseless.py'), e.g. ca n't -> can't, gon na -> gonna
'''


import re, os, glob

# https://stackoverflow.com/questions/15175142/how-can-i-do-multiple-substitutions-using-regex

def multiple_replace(dict, text):
  # Create a regular expression  from the dictionary keys
  regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))

  # For each match, look-up corresponding value in dictionary
  return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)

if __name__ == "__main__":
    # keys =  how the word is written in the text, values = how it should be amended
    dict = {
            " \'s" : "\'s",
            " n\'t" : "n\'t",
            " \'m" : "\'m",
            " \'ll" : "\'ll",
            " \'ve" : "\'ve",
            " \'re" : "\'re",
            " \'d" : "\'d",
            "gon na" : "gonna",
            "wan na" : "wanna",
            "gim me" : "gimme",
            "got ta" : "gotta",
        }


for file in glob.iglob('**', recursive=True):
    if os.path.isfile(file): # filter dirs
        if file.endswith('.txt'): # avoid editing .py files, etc
            with open(file, 'r') as input:
                filedata = input.read()
                new_text = multiple_replace(dict, filedata)
                with open("temp.txt", "w") as output:
                    output.write(new_text)

            # replace file with original name
            os.replace('temp.txt', file)


'''
After checking my two sample corpuses using AntConc,
these contractions were separated (in addition to apostrophe contractions):

gonna = gon na
wanna = wan na
gimme = gim me
gotta = got ta

'''
# https://en.wikipedia.org/wiki/Wikipedia:List_of_English_contractions

# these are all of the non-standard (e.g. 's 'll) contractions that I found
# in my sample corpuses

# after apostrophe
# 'all (y'all), 'am (ma'am)

# in random trigrams corpus
# - check if they are split after proper noun treatment
# gonna, kinda, wanna, woulda, coulda, shoulda, cuppa, finna (fixing to),
# gimme, gotta, howdy, imma, lon (I don't), gotcha

# in frequent trigrams
# innit

# not in corpus
# dunno, helluva, methinks, whatcha
# ma'am (can't search for it)
