import sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
if sys.version_info[0] >= 3:
    raw_input = input
vectorizer = TfidfVectorizer(stop_words='english')
svm = LinearSVC()
train_texts = []
train_labels = []
with open('trainingdata.txt', 'r') as f:
    num_lines = int(f.readline().strip())
    for _ in range(num_lines):
        line = f.readline().strip()
        idx = line.find(' ')
        label = int(line[:idx])
        text = line[idx+1:]
        train_texts.append(text)
        train_labels.append(label)
train_features = vectorizer.fit_transform(train_texts)
X_train, X_val, y_train, y_val = train_test_split(train_features, train_labels, test_size=0.2, random_state=42)
svm.fit(X_train, y_train)
num_test_docs = int(raw_input().strip())
test_texts = [raw_input().strip() for _ in range(num_test_docs)]
test_features = vectorizer.transform(test_texts)
predicted_labels = svm.predict(test_features)
for label in predicted_labels:
    print(label)
