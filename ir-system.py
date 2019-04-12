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



#temp=word_tokenize(content)

temp=content.split()
cnt=0
id=[]
title=[]
body=[]
flag=-1
flag1=-1
for i in range(0,len(temp)):
    if '.I'in temp[i]:
        flag=0
    elif(flag==0):

        id.append(temp[i])
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
body_split=body_split.split('**')



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

