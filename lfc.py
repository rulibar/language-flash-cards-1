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
correct = 0
incorrect = 0
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
    total = correct + incorrect + 1
    key = random.choice(keys)
    attempt = input(key + " - ").lower()
    answer = key.capitalize() + ": "
    for item in words[key]: answer += item + ", "
    answer = answer[:-2]
    if attempt == "exit()":
        total -= 1
        if total != 0:
            rate = round(100 * correct / total, 2)
            print("Total translations: " + str(total))
            print("Success rate: {}%".format(str(rate)))
        print("Exiting Language Flash Cards...")
        exit()
    if attempt in words[key]:
        streak += 1; correct += 1
        print('Correct. Total translations: {}. Streak: {}'.format(total, streak))
        print('{}.'.format(answer))
    else:
        streak = 0; incorrect += 1
        print('Incorrect. Total translations: {}.'.format(total))
        print('{}.'.format(answer))
