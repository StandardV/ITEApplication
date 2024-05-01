"""Training a model for Hyperlink clasification"""
import csv
import os
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score


current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "hyperlinkclassification.pkl")
# Load your dataset
# Assuming your dataset is in a CSV file named 'data.csv'
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(current_dir,"DatasetCompany.csv")

with open(csv_path, 'r', newline='') as file:
    reader = csv.reader(file)
    Lines = list(reader)
#next manual change at 800

data = pd.read_csv(csv_path)


# Use only the first 1000 rows
data_subset = data[:1200]#1102

print(data_subset.isnull().sum())
data_subset = data_subset.dropna()

# Separating hyperlinks and labels
X = data_subset['Hyperlink']
y = data_subset['Labels']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12, random_state=42)

# Data preprocessing
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

k = 11 
knn_classifier = KNeighborsClassifier(n_neighbors=k)
knn_classifier.fit(X_train_tfidf, y_train)

# Predict labels for the test set
y_pred = knn_classifier.predict(X_test_tfidf)

# Evaluate the performance of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# Print classification report
print(classification_report(y_test, y_pred))

training_set = [knn_classifier, tfidf_vectorizer]

with open(model_path, "wb") as f:
    joblib.dump(training_set, f)
  
    
# for i in range(1200,1310):
#     new_samples  = data.iloc[i]['Hyperlink']
#     new_samples_tfidf  = tfidf_vectorizer.transform([new_samples ])
#     new_labels  = knn_classifier.predict(new_samples_tfidf )

#     if len(Lines[i+1]) == 1:
#         Lines[i+1].append(new_labels[0])
#     else:    
#         Lines[i+1][1] = new_labels[0]#need to fix bug here, write in a cell that column haven't been made yet
    
#     with open(csv_path, 'w', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerows(Lines)

#     print("Predicted label:", new_labels)