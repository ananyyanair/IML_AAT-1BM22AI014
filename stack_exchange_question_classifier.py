import json, sys
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import HashingVectorizer
if sys.version_info[0]>=3: 
    raw_input=input
trans=HashingVectorizer(stop_words='english')
train=[]
train_label=[]
f=open('training.json')
for i in range(int(f.readline())):
    h=json.loads(f.readline())
    train.append(h['question']+"\r\n"+h['excerpt'])
    train_label.append(h['topic'])
f.close()
train = trans.fit_transform(train)
svm=LinearSVC()
svm.fit(train, train_label)
test=[]
for i in range(int(raw_input())):
    h=json.loads(raw_input())
    test.append(h['question']+"\r\n"+h['excerpt'])
test = trans.transform(test)
test_label=svm.predict(test)
for e in test_label: 
    print(e)
