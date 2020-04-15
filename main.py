from __future__ import print_function
import random

def pgen():
	with open('words_alpha.txt') as f:
		word = f.readlines()
		passwordlist = []
		for _ in range(4): passwordlist.append(random.choice(word))
		pw = []
		for p in passwordlist: pw.append(p.strip())
		print(" ".join(pw))

pgen()
