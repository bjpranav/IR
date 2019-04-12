import re
from nltk.tokenize import word_tokenize

#fname = r"D:\bin\AIT-690\Assignments\IR\cran.all.1400"
content = r"C:\Users\alaga\Desktop\sem 2\AIT690\IR1\cran.all.1400"
#docfile
content=open(content)
content=content.read()
content = content.replace("\n", "")
content=content.replace(".I"," .I")
content=content.replace(".T"," .T ")
content=content.replace(".W"," .W ")
#content=content.replace(".W",".W ")


#temp=word_tokenize(content)

temp=content.split()

id=[]
title=[]
body=[]
flag=-1
flag1=-1
cnt=0

for i in range(0,len(temp)):
    if '.I'in temp[i]:
        body.append("*")
        flag=0
    elif(flag==0):
        id.append(temp[i])
        flag=1
    elif(flag==1):
        if('.T' in temp[i]):
            title.append(temp[i])
            flag=2
        elif(flag==2 and '.A' not in temp[i]):
            title.append(temp[i])

    elif temp[i]=='.W':
        flag=3
    elif(flag==3):
        body.append(temp[i])



title_split=[]
for i in title:
    if i=='*':
        temp=" ".join(temp)
        title_split.append(temp)
        temp=[]

    else:
        temp.append(i)

'''
docs={}
prevPointer=None
topic=None
with open(fname) as f:
    for line in f:
        line=line.replace('\n','')
        index=re.findall(r'.I ([0-9]+)',line)
        #print(line)
        if(prevPointer=='.T'):
            topic=line
        if(prevPointer=='.A'):
            author=line
        if(prevPointer=='.B'):
            publication=line
        if(prevPointer=='.W'):
            text=line

        prevPointer=str(line)
'''
cnt=0
for i in range(0,len(id)):
    if i+1==int(id[i]):
        cnt+=1
print(cnt)
