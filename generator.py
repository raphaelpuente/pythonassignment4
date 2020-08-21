"""
Filename: generator.py
Author: Raphael Puente
Student ID: 301075627
File description: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.
"""



import random


#generated the getwords method
def getWords(filename):
    source = open(filename)
    temporary = list()
    for line in source:
        line = line.strip()
        temporary.append(line)

    words = tuple(temporary)
    source.close()

    return words

#importing information from txt files
articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
prepositions = getWords("prepositions.txt")
verbs = getWords("verbs.txt")



def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()

def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)

def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()

def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()

def main():
    """Allows the user to input the number of sentences
    to generate."""
    print(random.choice(articles))
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
main()