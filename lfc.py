import json

file = 'eng_esp.json'

words = json.loads(open(file).read())

print(words)
