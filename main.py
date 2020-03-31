from __future__ import print_function
from random_word import RandomWords

r = RandomWords()

passwordlist = []

for x in range(4):
    passwordlist.append(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb", minLength=5))

passwordlist = [element.lower() for element in passwordlist] ; passwordlist
print(*passwordlist, sep=" ")
