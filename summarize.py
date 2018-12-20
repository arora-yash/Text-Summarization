from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import tokenize
import nltk
from itertools import chain

a=[]
t=[]
line=[]
f=open('sample.txt','r')
t=f.readlines()
l1=[]

for i in t:
    l1.append(i.strip())

l1=list(filter(lambda a:a!='',l1))
heading=l1[0]
l1=l1[1:]
for i in l1:
    a.append(tokenize.sent_tokenize(i))

a=list(chain.from_iterable(a))

k=[]
tfidf=TfidfVectorizer(stop_words='english')
t1=tfidf.fit_transform(a)
t1=t1.todense()
heading1=heading.split()

for i in range(0,t1.shape[0]):
    sent=0
    for j in range(0,t1.shape[1]):
        sent=sent+t1.item((i,j))
    ab=[]
    tk=nltk.word_tokenize(a[i])
    ab=nltk.pos_tag(tk)
    for v in heading1:
        if v in a[i]:
            sent+=5
    for v in range(0,len(ab)):
        if ab[v][1]=='NN' or ab[v][1]=='NNP':
            sent+=5
        try:
            float(ab[v][0])
            sent+=5
        except:
            pass
    line.append(sent)

n=(int)(len(a)/3)
for i in range(0,n):
    j=line.index(max(line))
    k.append(j)
    line[j]=0

k.sort()

fn=open("summarized.txt","w")
for p in range(0,len(k)):
    fn.write(a[p])
    fn.write('\n')

fn.close()

