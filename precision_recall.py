
# precision
# key=r"D:\bin\AIT-690\Assignments\IR\cranqrel"
# my_output=r"D:\bin\AIT-690\Assignments\IR\your_file1.txt"
import sys
import numpy as np

my_output=sys.argv[1]
key=sys.argv[2]

key = open(key)
key = key.read()
my_output = open(my_output)
my_output = my_output.read()

key = key.split()
my_output = my_output.split()

key_dic = {}
my_dict = {}
for i in range(0, len(key), 3):
    if key[i] not in key_dic:
        key_dic[key[i]] = []
        my_dict[key[i]] = []

for j in range(1, len(key), 3):
    key_dic[key[j - 1]].append(key[j])

for j in range(1, len(my_output), 2):
    my_dict[my_output[j - 1]].append(my_output[j])

relevant_documents = []
total_documents_returned = []
documents_collection = []
i = 1
while (i != len(key_dic) + 1):
    cnt = 0
    for j in (my_dict[str(i)]):
        if j in key_dic[str(i)]:
            cnt += 1
    relevant_documents.append(cnt)
    if (len(my_dict[str(i)]) == 0):
        total_documents_returned.append(1)
    else:
        total_documents_returned.append(len(my_dict[str(i)]))
    documents_collection.append(len(key_dic[str(i)]))

    i += 1

precision = np.mean(np.divide(relevant_documents, total_documents_returned))
recall = np.mean(np.divide(relevant_documents, documents_collection))

# Mean Average Precision
mean_average_pre = []
i = 1
while (i != len(key_dic) + 1):
    temp = []
    for k in range(0, len(key_dic[str(i)])):
        for j in range(0, len(my_dict[str(i)])):
            if my_dict[str(i)][j] == key_dic[str(i)][k] and j >= k:
                a = (k + 1) / (j + 1)
                temp.append(a)
    if (len(temp) == 0):
        mean_average_pre.append(0)
    else:
        mean_average_pre.append(np.mean(temp))
    i += 1

print("Precision score : ",precision)
print("Recall Score : ",recall)
print("Mean Average Precision : ",np.mean(mean_average_pre))


with open('mylogfile.txt', 'w') as f:
        f.write("Precision score : " +str(precision)+'\n')
        f.write("Recall Score : "+str(recall)+'\n')
        f.write("Mean Average Precision : "+str(np.mean(mean_average_pre))+'\n')