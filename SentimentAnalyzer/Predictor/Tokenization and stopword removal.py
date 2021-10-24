import pandas as p
import csv
from nltk.tokenize import word_tokenize

def tokens_to_sentence(ls):
    s = ''
    for token in ls:
        s = s + token + ' '
    return s



    #####  INCLUDING REVIEW FILE #####
    
Reviews_DataSet= p.read_excel("dataset.xlsx")

    #####  INCLUDING STOPWORDS FILE #####

Stopwords_File= p.read_csv("stopwords.txt",header=None)

    #####  SELECTING REVIEW COLUMN FROM DATASET #####

Reviews=Reviews_DataSet["Review"]


    #####  SELECTING POLARITY COLUMN FROM DATASET #####

Polarities=Reviews_DataSet["Polarity"]
PolarityList=[]

for pi in Polarities:
    PolarityList.append(pi)
    #####  TOKENIZATION #####

Tokenized_List=[]

   

   #####  StopWords Removal #####

Without_StopWords_List=[]
for sentence in Reviews:
    tokens=word_tokenize(sentence)
    temp_tokens = [x.lower() for x in tokens]
    #Tokenized_List.append(tokens)
    for word in Stopwords_File[0]:
        while word.lower() in temp_tokens:
            temp_tokens.remove(word.lower())
    temp = tokens_to_sentence(temp_tokens) 
    Without_StopWords_List.append(temp)
    

    #####  Creating file containig comments without stopwords #####
heading=['Reviews','Sentiments']


Without_StopWords_without_specialChar_List = []
for sentence in Without_StopWords_List:
    temp = ''
    for ch in sentence:
        if( ch.isalnum() or ch == ' '):
            temp = temp + ch
    Without_StopWords_without_specialChar_List.append(temp)

req = {'Reviews' : Without_StopWords_without_specialChar_List,
       'Sentiments' : Polarities
       }


new_dataSet = p.DataFrame(req,columns=heading)


new_dataSet.to_csv('without stopping words file.csv',index=False)
