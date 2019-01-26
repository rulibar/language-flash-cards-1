# imports
import json
import random

# vars
file = 'eng_esp.json'

# compile words list
word_list = json.loads(open(file).read())
keys = list(word_list.keys())
lang1 = keys[0]; del keys[0]
lang2 = word_list[lang1]; del word_list[lang1]
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

print(words)

# main program
#print("Welcome to Language Flash Cards")
#print("Translate the words between " + lang2 + " and " + lang1)

#while True:
#    key = random.choice(keys); word = words[key]
#    pair = [key, word]; random.shuffle(pair)
#
#    ans = input(pair[0] + " - ")
#    if ans == pair[1]:
#        streak += 1
#        print('Correct. Streak: {}. Next word:'.format(streak))
#    else:
#        streak = 0
#        print('Sorry, the correct answer is "{}".'.format(pair[1]))
