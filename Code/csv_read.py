import csv
import re
no_of_items={}
dataset={}
feature_set={}
fh=open("predictiondata.csv","r")
count=0
for row in fh:
    if count==0:
        count+=1
        continue
    else:
        a=row
        a=re.split('[^a-zA-Z0-9\']',row)
        a.pop()
        print(a)
        print(a[6])
        no_of_items.setdefault(a[6],0)
        no_of_items[a[6]]+=1
        dataset.setdefault(a[6],{})
        for i in a:
            dataset[a[6]].setdefault(i.lower(),0)
            dataset[a[6]][i.lower()]+=1
            feature_set.setdefault(i.lower(),{})
            feature_set[i.lower()].setdefault(a[6],0)
            feature_set[i.lower()][a[6]]+=1
        
print("feature set is",feature_set)
print()
#print("no_of_items",no_of_items)
print()
#print("dataset is",dataset)

