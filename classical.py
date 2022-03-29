from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.svm import LinearSVC


X_train = X_train.astype(np.float)
Y_train = Y_train.astype(np.float)


rf = RandomForestClassifier()
knn = KNeighborsClassifier()
dtc = DecisionTreeClassifier()
lr = LogisticRegression()
rc = RidgeClassifier()
svm = LinearSVC(multi_class='crammer_singer')

test_size = [0.05, 0.1, 0.15, 0.20, 0.25, 0.5]


randomForest = []
KNN = []
decisionTree = []
logisticRegression = []
ridgeClassifer = []
supportVectorMachine = []

#if you wish to split test sizes then use a loop at this point and typesongs
#for i in test_size
#and split your data accordingly between train and test
#this is not required for dreaddit since we already have it split
#this is just FYI

yPredR = rf.fit(X_train,Y_train).predict(X_test)
yPredK = knn.fit(X_train, Y_train).predict(X_test)
yPredDT = dtc.fit(X_train, Y_train).predict(X_test)
yPredLR = lr.fit(X_train, Y_train).predict(X_test)
yPredRC = rc.fit(X_train, Y_train).predict(X_test)
yPredSVM = svm.fit(X_train, Y_train).predict(X_test)



randomForest.append(1-((yPredR!=Y_test).sum())/np.shape(Y_test)[0])
KNN.append(1-(yPredK!=Y_test).sum()/np.shape(Y_test)[0])
decisionTree.append(1-(yPredDT!=Y_test).sum()/np.shape(Y_test)[0])
logisticRegression.append(1-(yPredLR!=Y_test).sum()/np.shape(Y_test)[0])
ridgeClassifer.append(1-(yPredRC!=Y_test).sum()/np.shape(Y_test)[0])
supportVectorMachine.append(1-(yPredSVM!=Y_test).sum()/np.shape(Y_test)[0])






print('Random Forest', randomForest)
print('KNN', KNN)
print('Decistion Tree', decisionTree)
print('Logistic Regression', logisticRegression)
print('Ridge Classifier', ridgeClassifer)
print('Support Vector Machine', supportVectorMachine)
