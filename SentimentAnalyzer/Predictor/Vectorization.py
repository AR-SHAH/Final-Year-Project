import pandas as p
#import csv
from nltk.tokenize import word_tokenize
#import nltk as nl
from nltk.util import ngrams

dsc = p.read_excel('dataset.xlsx')

score = dsc['score']


Reviews_DataSet= p.read_csv("without stopping words file.csv")
comments=Reviews_DataSet["Reviews"]

UG= p.read_csv("Unigrams.csv")
Unigrams=UG["Unigrams"]


uu = Unigrams.copy()
uu = list(uu)

BG= p.read_csv("Bigrams.csv")
Bigrams=BG["Bigrams"]
vectors_u=[]
vectors_b=[]

cc  = list(comments)

for tokens in cc:
    temp=word_tokenize(tokens)                       
    rr = [0] * len(uu)
    for t in temp:
       if t in uu:
            rr[uu.index(t)] = 1
        
    vectors_u.append(rr)

bb = Bigrams.copy()
bb = list(bb)

for tokens in cc:
    temp_bi = word_tokenize(tokens)
    temp_bi = list(ngrams(temp_bi, 2)) 
    rr = [0] * len(bb)
    for t in temp_bi:
        tt = t[0] + ' ' + t[1]
        if tt in bb:
            rr[bb.index(tt)] = 1

    vectors_b.append(rr)

final_vec = []

ee = zip(vectors_u,vectors_b)





for i,j in ee:
    final_vec.append(i+j)

new_score = []

for i in score:
    if i == 1:
        new_score.append([1,0,0,0,0])
    elif i == 2:
        new_score.append([0,1,0,0,0])
    elif i == 3:
        new_score.append([0,0,1,0,0])
    elif i == 4:
        new_score.append([0,0,0,1,0])
    elif i == 5:
        new_score.append([0,0,0,0,1])
        
        
        
for i in range(0,len(final_vec)):
    final_vec[i] = final_vec[i] + new_score[i]


f_d = p.DataFrame(final_vec)


f_d.to_csv('dataset for training.csv',index=False,header=False)






