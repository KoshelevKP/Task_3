# XML
import xml.etree.ElementTree as ET
tree = ET.parse("newsafr.xml")
root = tree.getroot()
xml_items = root.findall("channel/item")
descriptions=[]
for item in xml_items:
  description = item.find("description")
  descriptions += description.text.split(" ") #текст из файла

words_list = list() # список различных слов в тексте
for word in descriptions: 
  if len(word) >= 6:
    if word not in words_list:
      words_list +=[word]

words_count = list() # подсчет количества слов в тексте
for word in words_list:
  words_count.append([word, descriptions.count(word)])

words_sorted = sorted(words_count, key=lambda word: word[1])

top_10_words = words_sorted[-10:-1]

for word in top_10_words:
  print(word[0], word[1])
