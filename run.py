# -*- coding: utf-8 -*-
from nltk import RegexpTagger
from pythainlp.tokenize import word_tokenize
def open_dict(name):
    with open(name+".dict","r") as f:
        return [i.strip() for i in f.readlines()]
dict_word={
    "NUM":open_dict("NUM"),
    "PART":open_dict("part"),
    "DET":open_dict("det"),
    "PROPN":open_dict("PROPN"),
    "ADJ":open_dict("ADJ"),
    "NOUN":open_dict("NOUN"),
    "NOTKNOW":[".*"]
}

regexp_tagger = RegexpTagger([('('+'|'.join(dict_word[a])+')$',a) for a in dict_word])
while True:
    text=input("input : ")
    if text == "exit":
        break
    print(regexp_tagger.tag(word_tokenize(text)))
    print("\n")
"""
https://stackoverflow.com/questions/14802442/how-to-use-a-regex-backoff-tagger-in-python-nltk-to-override-nns
"""

#print('Regexp accuracy %4.1f%%' % (100.0 * regexp_tagger.evaluate(brown_test)))