import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

data = pd.read_excel('data/data_analisis3.xlsx')
df = pd.DataFrame(data)

x = df['Tweet_clean']
y = df['Sentiment']

vactorizer = TfidfVectorizer(max_features=2500)
model_g = GaussianNB()

v_data = vactorizer.fit_transform(x).toarray()

X_train, X_test, y_train, y_test = train_test_split(v_data, y, test_size=0.2, random_state=0)
model_g.fit(X_train, y_train)

y_preds = model_g.predict(X_test)

print(confusion_matrix(y_test, y_preds))
print(classification_report(y_test, y_preds))
print('nilai akurasinya adalah ', accuracy_score(y_test, y_preds))