from random import randint
from dictutil import *

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(len(review_options))]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    dico = dict()  # create empty dictionary
    for i,j in enumerate(strlist):  # for every (doc_id, document) pair
        for k in j.split():     # split the document into words and traverse
            if k in dico: dico[k].add(i)   # if word is key , add doc_id to its value set
            else: dico[k] = {i}   # otherwise create a key for new word and add doc_id
    return dico

    
## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    if query == []: return set()  
    else:
        S = set()    
        for x in query:  
            S.update(inverseIndex[x])
        return S


    
## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    if query == []: return set()
    else:
        S=set(inverseIndex[query[0]])
        for i in query[1:]: S=S.intersection(inverseIndex[i])
    return S

