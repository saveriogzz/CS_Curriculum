import collections
from nltk.corpus import stopwords

file = open('shakespeare.txt', encoding="utf8")

stopwords = set(stopwords.words('english'))

wordcount={}

for word in file.read().lower().split():
    word = word.replace(".","")
    word = word.replace(",","")
    word = word.replace("\"","")
    word = word.replace("“","")
    word = word.replace("?","")
    word = word.replace(";","")
    word = word.replace("!","")
    if word not in stopwords:
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

c = collections.Counter(wordcount).most_common(20)

#print(c.most_common(20))
for word, count in c:
    print(word, ": ", count)