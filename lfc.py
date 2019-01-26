# imports
import json
import random

# vars
file = 'eng_esp.json'

# compile words list
word_list = json.loads(open(file).read())
keys = list(word_list.keys())
lang1 = keys[0].capitalize()
lang2 = word_list[keys[0]].capitalize()
del word_list[keys[0]]; del keys[0]
streak = 0

words = dict()
new_keys = list(keys)
for key in keys:
    words[key] = set()
    for item in word_list[key]:
        words[key].add(item)
        if item not in new_keys:
            new_keys.append(item)
            words[item] = {key}
        else: words[item].add(key)
keys = new_keys

# main program
print("Welcome to Language Flash Cards.")
print("Translate the words between {} and {}.".format(lang2, lang1))

while True:
    key = random.choice(keys)
    attempt = input(key + " - ")
    answer = key.capitalize() + ": "
    for item in words[key]: answer += item + ", "
    answer = answer[:-2]
    if attempt in words[key]:
        streak += 1
        print('Correct. {}. Streak: {}'.format(answer, streak))
    else:
        streak = 0
        print('Incorrect. {}.'.format(answer))
