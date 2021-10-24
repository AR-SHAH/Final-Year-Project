import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import keras

def tokens_to_sentence(ls):
    s = ''
    for token in ls:
        s = s + token + ' '
        return s
# =============================================================================
#######################Tokenizaton+Stopword Removal############################
# =============================================================================
def score_calculator(comment):
    #test_comment=input("Enter the comment you want to test\n")
    test_comment=list(comment.lower().split(" "))
    
    Stopwords_File= pd.read_csv("Predictor/stopwords.txt",header=None)    
    stopwords=Stopwords_File.values.tolist()
    
    without_stopwords=[]
    
    Stopwords_list = list(Stopwords_File[0])
    
    
    req_com = ''
    for c in test_comment:
        if c.lower() not in Stopwords_list:
            req_com += c.lower() + ' '
        
    
    model = keras.models.load_model('Predictor/77.09497206703911')
    
    
    # =============================================================================
    # ##############################Vectorization##################################
    # =============================================================================
    
    
    
    Reviews_DataSet= pd.Series(without_stopwords)
    
    UG= pd.read_csv("Predictor/Unigrams.csv")
    Unigrams=UG["Unigrams"]
    
    
    uu = Unigrams.copy()
    uu = list(uu.str.lower())
    
    BG= pd.read_csv("Predictor/Bigrams.csv")
    Bigrams=BG["Bigrams"]
    vectors_u=[]
    vectors_b=[]
    
    
    
    
    
    
    temp = req_com.split()                     
    rr = [0] * len(uu)
    for t in temp:
       if t in uu:
            rr[uu.index(t)] = 1
        
    vectors_u.append(rr)
    
    bb = Bigrams.copy()
    bb = list(bb.str.lower())
    
    
    temp_bi = list(ngrams(temp, 2)) 
    rr = [0] * len(bb)
    for t in temp_bi:
        tt = t[0] + ' ' + t[1]
        if tt in bb:
            rr[bb.index(tt)] = 1
    
    vectors_b.append(rr)
    
    
    final_com = vectors_u[0] + vectors_b[0]
    
    
    com_pd = pd.DataFrame([final_com])
    
    
    result = model.predict(com_pd)
    
    
    
    result = (result > 0.5)
    
    fi_res = []
    
    
    zx = result[0]
    
    for i in range(0,len(zx)):
        if zx[i]:
            fi_res.append(1)
        else:
            fi_res.append(0)
            
    if fi_res==[1,0,0,0,0]:
        return ('positive',1)
    elif fi_res==[0,1,0,0,0]:
        return ('positive',2)
    elif fi_res==[0,0,1,0,0]:
        return ('neutral',3)
    elif fi_res==[0,0,0,1,0]:
        return ('negative',4)
    elif fi_res==[0,0,0,0,1]:
        return ('negative',5)
      
    
        
      


