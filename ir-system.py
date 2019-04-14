import re
from collections import Counter
from nltk.tokenize import word_tokenize
import numpy as np

content = r"D:\bin\AIT-690\Assignments\IR\cran.all.1400"
#content = r"C:\Users\alaga\Desktop\sem 2\AIT690\IR1\cran.all.1400"

#docfile
content=open(content)
content=content.read()
content = content.replace("\n", "")
content=content.replace(".I"," .I")
content=content.replace(".T"," .T ")
content=content.replace(".W"," .W ")



#temp=word_tokenize(content)

temp=content.split()
cnt=0
ids=[]
title=[]
body=[]
flag=-1
flag1=-1
for i in range(0,len(temp)):
    if '.I'in temp[i]:
        flag=0
    elif(flag==0):

        ids.append(temp[i])
        flag=1
    elif(flag==1):
        if('.T' in temp[i]):
            title.append(temp[i])
            flag1=0
        elif(flag1==0 and '.A' not in temp[i]):
            title.append(temp[i])
        elif('.A' in temp[i]):
            flag=2
    elif temp[i]=='.W' and flag==2:
        flag=3
        body.append("**")
    elif(flag==3):
        body.append(temp[i])




del title[0]
title_split=' '
title_split=title_split.join(title)
title_split=title_split.split('.T')

del body[0]
body_split=' '
body_split=body_split.join(body)
body_split_docs=body_split.split('**')
'''
tfidf={}
wordvec={}
def tf(tokens,documents):
    tfidfList=[]
    #wordCounts = list(Counter(tokens).values)
    tf=[i/len(tokens) for i in wordCounts]
    for index,token in enumerate(wordCounts):
        count=1        
        for doc in documents:
            if(tokens[index] in doc):
                count+=1
        idf=np.log(len(documents)/(count))
        tfidfList.append(tf[index]*idf)
    return(tfidfList)
'''
tfidf={}
wordvec={}
def tfidf(tokens,documents,token):
    tfidfList=[]
    wordCounts = Counter(tokens)
    tf=wordCounts[token]/len(tokens)  
    count=0
    for doc in documents:
        if(token in doc):
            count+=1
    idf=1+np.log(len(documents)/(count))
    return(tf*idf)
    
docs={}
for i in range(0,len(ids)):
    docs[i+1]=[title_split[i],body_split_docs[i]]
    #titleTokens=title_split[i].split()
    #titleTfIdf=tf(titleTokens,title_split)
    #bodyTokens=body_split[i].split()
    #bodyTfIdf=tf(bodyTokens,body_split)
    #tfidf[ids[i]]=[titleTfIdf,bodyTfIdf]
    

query = r"D:\bin\AIT-690\Assignments\IR\cran.qry"
#content = r"C:\Users\alaga\Desktop\sem 2\AIT690\IR1\cran.all.1400"

#docfile
query=open(query)
query=query.read()
query = query.replace("\n", "")
query=query.replace(".I"," .I")
query=query.replace(".W"," .W ")

temp=query.split()
cnt=0
ids=[]
title=[]
body=[]
flag=-1
flag1=-1
for i in range(0,len(temp)):
    if '.I'in temp[i]:
        flag=0
    elif(flag==0):
        ids.append(temp[i])
        flag=1
    elif temp[i]=='.W' and flag==1:
        flag=3
        body.append("**")
    elif(flag==3):
        body.append(temp[i])

del body[0]
body_split=' '
body_split=body_split.join(body)
body_split=body_split.split('**')

def square(list):
    return map(lambda x: x ** 2, list)

def cosineSimilarity(query,doc):
    up=np.dot(query,doc)
    modQuery=np.sqrt(sum(square(query)))
    docQuery=np.sqrt(sum(square(doc)))
    down=modQuery*docQuery
    return(up/down)
    
    
    
queries={}
queryTfIdf={}
counterrr=0
queryResults=[]
for i in range(0,len(ids)):
    results=[]
    queries[i]=[body_split[i]]
    queryTokens=body_split[i].split()
    #bodyTfIdf=tf(queryTokens,body_split)
    for ID,doc in enumerate(docs.values()):
        queryTfIdfValList=[]
        docTfIdfValList=[]
        flag=0
        for indexVal,token in enumerate(queryTokens):
            if(token in doc[0].split()):
                flag=1
                queryTfIdfVal=tfidf(queryTokens,body_split,token)
                queryTfIdfValList.append(queryTfIdfVal)
                docTfIdfVal=tfidf(doc[0],body_split_docs,token)
                docTfIdfValList.append(docTfIdfVal)
                #print(queryTfIdfVal,docTfIdfVal)
        if(flag==1):
            results.append((ID,cosineSimilarity(queryTfIdfValList,docTfIdfValList)))
    queryResults.append(results)

                
    
