from sklearn.multiclass import OneVsRestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier
import pandas as pd
import numpy as np



data = pd.read_csv('/Users/ankit/Documents/SSPA Project/Data_Building_Codes/first_300.csv')
X_train = data.iloc[:, 0:26]
Y_train = data['label']


X_train, X_test, Y_train, Y_test = train_test_split(X_train, Y_train, test_size=0.05)

Y_pred_1 = OneVsOneClassifier(LinearSVC(random_state=0, max_iter = 500)).fit(X_train, Y_train).predict(X_test)

Y_pred_2 = OneVsRestClassifier(LinearSVC(random_state=0, max_iter = 500)).fit(X_train, Y_train).predict(X_test)


print(f1_score(Y_test, Y_pred_1, average='micro'))
print(f1_score(Y_test, Y_pred_1, average='macro'))
print(f1_score(Y_test, Y_pred_1, average='weighted'))
print(f1_score(Y_test, Y_pred_2, average='micro'))
print(f1_score(Y_test, Y_pred_2, average='macro'))
print(f1_score(Y_test, Y_pred_2, average='weighted'))


Y_pred_1 = OneVsOneClassifier(LogisticRegression(random_state=0, max_iter = 500)).fit(X_train, Y_train).predict(X_test)

Y_pred_2 = OneVsRestClassifier(LogisticRegression(random_state=0, max_iter = 500)).fit(X_train, Y_train).predict(X_test)


print(f1_score(Y_test, Y_pred_1, average='micro'))
print(f1_score(Y_test, Y_pred_1, average='macro'))
print(f1_score(Y_test, Y_pred_1, average='weighted'))
print(f1_score(Y_test, Y_pred_2, average='micro'))
print(f1_score(Y_test, Y_pred_2, average='macro'))
print(f1_score(Y_test, Y_pred_2, average='weighted'))


Y_pred_1 = OneVsOneClassifier(DecisionTreeClassifier(random_state=0, max_iter = 500)).fit(X_train, Y_train).predict(X_test)

Y_pred_2 = OneVsRestClassifier(DecisionTreeClassifier(random_state=0, max_iter = 500)).fit(X_train, Y_train).predict(X_test)


print(f1_score(Y_train, Y_pred_1, average='micro'))
print(f1_score(Y_train, Y_pred_1, average='macro'))
print(f1_score(Y_train, Y_pred_1, average='weighted'))
print(f1_score(Y_train, Y_pred_2, average='micro'))
print(f1_score(Y_train, Y_pred_2, average='macro'))
print(f1_score(Y_train, Y_pred_2, average='weighted'))
