from collections import Counter
import numpy as np

#content = r"D:\bin\AIT-690\Assignments\IR\cran.all.1400"
content = r"C:\Users\alaga\Desktop\sem 2\AIT690\IR1\cran.all.1400"

#docfile
content=open(content)
content=content.read()
content = content.replace("\n", "")
content=content.replace(".I"," .I")
content=content.replace(".T"," .T ")
content=content.replace(".W"," .W ")
content=content.replace("-"," - ")



#temp=word_tokenize(content)

con_split=content.split()
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

temp= []
for w in con_split:
    if w not in stop_words:
        temp.append(w)
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

tfidf={}
wordvec={}
def tfidf(tokens,type):
    tfidfList=[]
    wordCounts = Counter(tokens)
    tf=wordCounts[token]/len(tokens)
    print(tf)

    count=0
    for doc in documents:
        if(token in doc):
            count+=1
    idf=1+np.log(len(documents)/(count))
    return(tf*idf)
'''
docs={}
for i in range(0,len(ids)):
    docs[i+1]=[title_split[i],body_split_docs[i]]
    #titleTokens=title_split[i].split()
    #titleTfIdf=tf(titleTokens,title_split)
    #bodyTokens=body_split[i].split()
    #bodyTfIdf=tf(bodyTokens,body_split)
    #tfidf[ids[i]]=[titleTfIdf,bodyTfIdf]
    

#query = r"D:\bin\AIT-690\Assignments\IR\cran.qry"

query = r"C:\Users\alaga\Desktop\sem 2\AIT690\IR1\cran.qry"
#content = r"C:\Users\alaga\Desktop\sem 2\AIT690\IR1\cran.all.1400"

#docfile
query=open(query)
query=query.read()
query = query.replace("\n", "")
query=query.replace(".I"," .I")
query=query.replace(".W"," .W ")
query=query.replace("-"," - ")

que_split=query.split()
temp= []
for w in que_split:
    if w not in stop_words:
        temp.append(w)
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





def termFrequency(term, document):
    normalizeDocument = document.lower().split()
    return normalizeDocument.count(term.lower()) / float(len(normalizeDocument))


def inverseDocumentFrequency(term, allDocuments):
    numDocumentsWithThisTerm = 0
    for doc in allDocuments:
        if term.lower() in allDocuments[doc][0].lower().split():
            numDocumentsWithThisTerm = numDocumentsWithThisTerm + 1

    if numDocumentsWithThisTerm > 0:
        return 1.0 + np.log(float(len(allDocuments)) / numDocumentsWithThisTerm)
    else:
        return 1.0


#document tf and idf
complete_tf=[]
complete_idf=[]
for i in range(1,1401):
    x=docs[i][0].split()
    tf = []
    idf=[]
    for j in x:
        tf.append(termFrequency(j, docs[i][0]))
        idf.append(inverseDocumentFrequency(j, docs))

    complete_tf.append(tf)
    complete_idf.append(idf)

#indexing
indexing_idf_word={}
for i in range(1,1401):
    x = docs[i][0].split()
    for j in x:
        if j not in indexing_idf_word:
            indexing_idf_word[j]=inverseDocumentFrequency(j, docs)

#doc_tf_idf
complete_doc_tf_idf=[]
for i in range(0,1400):
    a=complete_tf[i]
    b=complete_idf[i]
    complete_doc_tf_idf.append(np.multiply(a,b))


'''
complete_index=[]
for i in body_split:
    index_query = []
    for j in i.split():
        index_word = []
        for k in range(1,1401):

            if j in docs[k][0].split():
                d=docs[k][0].split().index(j)
                index_word.append(d)

            else:
                index_word.append(-1)

        index_query.append(index_word)
    complete_index.append(index_query)





for i in range(0,len(body_split)):
    for j in range(0,len(body_split[i].split())):
        for k in range(0,1400):
            if complete_index[i][j][k]!=-1:
                complete_index[i][j][k]=complete_doc_tf_idf[k][complete_index[i][j][k]]




'''
doc_query_tf=[]
doc_query_idf=[]
for i in body_split:
    doc_query_word_tf = []
    doc_query_word_idf = []
    for k in range(1, 1401):
        doc_query_word_doc_tf = []
        doc_query_word_doc_idf = []
        for j in i.split():
            if j in docs[k][0].split():
                doc_query_word_doc_tf.append(termFrequency(j, docs[k][0]))
            else:
                doc_query_word_doc_tf.append(0)

            if j in indexing_idf_word:
                doc_query_word_doc_idf.append(indexing_idf_word[j])
            else:
                doc_query_word_doc_idf.append(0)


        doc_query_word_tf.append(doc_query_word_doc_tf)
        doc_query_word_idf.append(doc_query_word_doc_idf)

    doc_query_tf.append(doc_query_word_tf)
    doc_query_idf.append(doc_query_word_idf)



complete_doc_query_tf_idf=[]
for i in range(0,len(body_split)):
    a=doc_query_tf[i]
    b=doc_query_idf[i]
    complete_doc_query_tf_idf.append(np.multiply(a,b))

#term frequency of queries
query_idf=[]
query_tf=[]
for i in body_split:
    query_word_tf=[]
    query_word_idf = []
    for j in i.split():
        query_word_tf.append(termFrequency(j, i))
        if j in indexing_idf_word:
            query_word_idf.append(indexing_idf_word[j])
        else:
            query_word_idf.append(0)

    query_idf.append(query_word_idf)
    query_tf.append(query_word_tf)


complete_query_tf_idf=[]
for i in range(0,len(body_split)):
    a=query_tf[i]
    b=query_idf[i]
    complete_query_tf_idf.append(np.multiply(a,b))


'''

complete_query_idf=[]
idf=[]
for i in range(0,len(body_split)):
    query_idf = []
    for j in range(0,len(body_split[i].split())):
        temp=[]
        for k in range(0,1400):
            if complete_index[i][j][k]!=0:
                idf=complete_index[i][j][k]
            else:
                idf=0
            temp.append(idf)
        query_idf.append(max(temp))
    complete_query_idf.append(query_idf)



complete_query_tf_idf=[]
for i in range(0,len(body_split)):
    a=np.array(complete_tf[i])
    b=np.array(complete_idf[i])

    complete_query_tf_idf.append(a*b)
'''



def square(list):
    return map(lambda x: x ** 2, list)


def cosineSimilarity(query, doc):
    up = float(np.dot(query, doc))
    modQuery = np.sqrt(sum(square(query)))
    docQuery = np.sqrt(sum(square(doc)))
    down = float(modQuery * docQuery)
    if(down==0):
        down=1
    return (up / down)



complete_list=[]
for i in range(0,len(body_split)):
    list = []
    for k in range(0, 1400):
        x=cosineSimilarity(complete_query_tf_idf[i],complete_doc_query_tf_idf[i][k])
        list.append(x)
    complete_list.append(list)


final_list=[]
for i in range(0,len(complete_list)):
    temp = np.argsort(complete_list[i])
    temp = temp[::-1]
    sub_final_list=[]
    for j in range(0,len(temp)):
        if complete_list[i][temp[j]]!=0:
            sub_final_list.append(temp[j]+1)
    final_list.append(sub_final_list)

output=[]
for i in range(0,len(final_list)):
    for j in final_list[i]:
        output.append(str(i+1)+' '+str(j))


with open('your_file.txt', 'w') as f:
    for item in output:
        f.write("%s\n" % item)

'''
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

 '''
------------------------------------------


#indexing
indexing_idf_word={}
for i in range(1,1401):
    x = docs[i][1].split()
    for j in x:
        if j not in indexing_idf_word:
            indexing_idf_word[j]=inverseDocumentFrequency(j, docs)

doc_query_tf=[]
doc_query_idf=[]
for i in body_split:
    doc_query_word_tf = []
    doc_query_word_idf = []
    for k in range(1, 1401):
        doc_query_word_doc_tf = []
        doc_query_word_doc_idf = []
        for j in i.split():
            if j in docs[k][1].split():
                doc_query_word_doc_tf.append(termFrequency(j, docs[k][1]))
            else:
                doc_query_word_doc_tf.append(0)

            if j in indexing_idf_word:
                doc_query_word_doc_idf.append(indexing_idf_word[j])
            else:
                doc_query_word_doc_idf.append(0)


        doc_query_word_tf.append(doc_query_word_doc_tf)
        doc_query_word_idf.append(doc_query_word_doc_idf)

    doc_query_tf.append(doc_query_word_tf)
    doc_query_idf.append(doc_query_word_idf)



complete_doc_query_tf_idf=[]
for i in range(0,len(body_split)):
    a=doc_query_tf[i]
    b=doc_query_idf[i]
    complete_doc_query_tf_idf.append(np.multiply(a,b))

#term frequency of queries
query_idf=[]
query_tf=[]
for i in body_split:
    query_word_tf=[]
    query_word_idf = []
    for j in i.split():
        query_word_tf.append(termFrequency(j, i))
        if j in indexing_idf_word:
            query_word_idf.append(indexing_idf_word[j])
        else:
            query_word_idf.append(0)

    query_idf.append(query_word_idf)
    query_tf.append(query_word_tf)


complete_query_tf_idf=[]
for i in range(0,len(body_split)):
    a=query_tf[i]
    b=query_idf[i]
    complete_query_tf_idf.append(np.multiply(a,b))


def square(list):
    return map(lambda x: x ** 2, list)


def cosineSimilarity(query, doc):
    up = float(np.dot(query, doc))
    modQuery = np.sqrt(sum(square(query)))
    docQuery = np.sqrt(sum(square(doc)))
    down = float(modQuery * docQuery)
    if(down==0):
        down=1
    return (up / down)


complete_list=[]
for i in range(0,len(body_split)):
    list = []
    for k in range(0, 1400):
        x=cosineSimilarity(complete_query_tf_idf[i],complete_doc_query_tf_idf[i][k])
        list.append(x)
    complete_list.append(list)


final_list=[]
for i in range(0,len(complete_list)):
    temp = np.argsort(complete_list[i])
    temp = temp[::-1]
    sub_final_list=[]
    for j in range(0,len(temp)):
        if complete_list[i][temp[j]]!=0:
            sub_final_list.append(temp[j]+1)
    final_list.append(sub_final_list)

output=[]
for i in range(0,len(final_list)):
    for j in final_list[i]:
        output.append(str(i+1)+' '+str(j))


with open('your_file2.txt', 'w') as f:
    for item in output:
        f.write("%s\n" % item)

