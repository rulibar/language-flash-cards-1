# imports
import json
import random

# vars
file = 'eng_esp.json'

# main
words = json.loads(open(file).read())
keys = list(words.keys())
lang1 = keys[0]; del keys[0]
lang2 = words[lang1]; del words[lang1]
streak = 0

print("Welcome to lang Flash Cards")
print("Translate the words between " + lang1 + " and " + lang2)

#while True:    
