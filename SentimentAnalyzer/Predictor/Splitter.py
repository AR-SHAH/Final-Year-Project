import pandas as c
x=c.read_excel("SentimentalWords.xlsx")
col=x["Sentimental Words"]
col=list(col)

r = []
s = []
for i in range(0,len(col)):
    if ' ' in col[i].lstrip() and ' ' in col[i].rstrip():
        r.append(col[i])
    else:
        s.append(col[i])

d = {'Bigrams':r}
Bigrams = c.DataFrame(d)
Bigrams.to_csv('Bigrams.csv',index=False)

s = {'Unigrams':s}
Unigrams = c.DataFrame(s)
Unigrams.to_csv('Unigrams.csv',index=False)