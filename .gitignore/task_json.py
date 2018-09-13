# JSON
from pprint import pprint
import json
with open("newsafr.json") as datafile:
  json_data = json.load(datafile)

data = list()
for item in json_data["rss"]["channel"]["items"]:
  data += item["description"].split(" ")

words_list = list() # список различных слов в тексте
for word in data: 
  if len(word) >= 6:
    if word not in words_list:
      words_list +=[word]

words_count = list() # подсчет количества слов в тексте
for word in words_list:
  words_count.append([word, data.count(word)])

words_sorted = sorted(words_count, key=lambda word: word[1])

top_10_words = words_sorted[-10:-1]

for word in top_10_words:
  print(word[0], word[1])