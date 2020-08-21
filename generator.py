"""
Filename: generator.py
Author: Raphael Puente
Student ID: 301075627
File description: Generates and displays sentences using simple grammar and vocabulary. Words are chosen at random.
"""

#importing information from txt files


import random
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL",)
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")

def getWords(filename):
    source = open(filename)
    temporary = list()
    for line in source:
        line = line.strip()
        temporary.append(line)

    words = tuple(temporary)
    source.close()

    return words

articles = getWords("articles.txt")
nouns = getWords("nouns.txt")
prepostions = getWords("prepositions.txt")
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
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())
        
main()