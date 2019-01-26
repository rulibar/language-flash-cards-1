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

print("Welcome to Language Flash Cards")
print("Translate the words between " + lang1 + " and " + lang2)

while True:
    key = random.choice(keys); word = words[key]
    pair = [key, word]; random.shuffle(pair)

    ans = input(pair[0] + " - ")
    if ans == pair[1]:
        streak += 1
        print('Correct. Streak: {}. Next word:'.format(streak))
    else:
        streak = 0
        print('Sorry, the correct answer is "{}".'.format(pair[1]))
