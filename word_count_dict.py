
import json

with open("test.txt","r",encoding="utf-8") as f:
    text = f.read()

"hallo".replace()
# removing unwanted characters from text
words = text.replace('\n',' ').replace('.',' ').replace(',',' ').replace(';',' ').replace('!',' ').replace('?',' ').replace(':',' ')
 
# split the text into list of words, drop empty words
words = [word.lower() for word in words.split(" ") if word]
 
# print(words)

wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] = wordCount[word] + 1
    else:
        wordCount[word] = 1

maxcount = max(wordCount,key=wordCount.get)
print(maxcount,wordCount[maxcount])

# open file in write mode
with open('save.json','w',encoding="utf-8") as f:
    # dump data as str to filestream
    json.dump(wordCount,f,indent=4)

with open('save.json','r',encoding="utf-8") as f:
    newWordCount = json.load(f)

print(newWordCount)