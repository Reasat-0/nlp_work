import numpy as np
import pandas as pd

dataset  = pd.read_csv('Katty2.csv')

#____-To check whther there is any missing values or not

dataset.isnull().sum() #if all output are 0 then there is no missing values there

#checking the unique values and numbr of unique values

dataset['label'].unique()

dataset['label'].value_counts() 

from sklearn.model_selection import train_test_split

x = dataset[['Length']]

y = dataset['Label']

xTrain , xTest , yTrain , yTest = train_test_split(x,y,test_size = 0.3, random_state = 0 )
                        
#_________Model_with_logistic_regression model

from sklearn.linear_model import LogisticRegression

lr_regressor = LogisticRegression()

lr_regressor.fit(xTrain,yTrain)


prediction = lr_regressor.predict(xTest)

# Checking the confusion matrix

from sklearn import metrics
confusion_matrix = metrics.confusion_matrix(yTest,prediction)

#classification report
print(metrics.classification_report(yTest,prediction))

print(metrics.accuracy_score(yTest,prediction))


#______Model with Naive Bayes

from sklearn.naive_bayes import MultinomialNB

nb_regressor = MultinomialNB()

nb_regressor.fit(xTrain,yTrain)

nb_pred = nb_regressor.predict(xTest)
print(nb_pred)

#classification report
print(metrics.classification_report(yTest,prediction))

#print(metrics.accuracy_score(yTest,nb_pred))
#confusion matrix fo Naive

dt = pd.DataFrame(metrics.confusion_matrix(yTest,nb_pred), index = ['ham','spam'] , columns = ['ham','spam'])
dt

#___________Model with SVM

from sklearn.svm import SVC
svc_regressor = SVC(gamma = 'auto' )
svc_regressor.fit(xTrain,yTrain)
svc_pred = svc_regressor.predict(xTest)
