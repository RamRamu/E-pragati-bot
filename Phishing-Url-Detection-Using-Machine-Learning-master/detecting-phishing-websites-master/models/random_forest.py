import numpy as np
#import feature_extraction
from sklearn.ensemble import RandomForestClassifier as rfc
#from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression as lr
#from flask import jsonify
import pickle


#Seperating training features, testing features, training labels & testing labels
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
loaded_model =  pickle.load(open('final_models/rf_final.sav','rb'))

prediction = loaded_model.predict(X_new)



if prediction == -1:
    print("Phishing Url")
else:
    print("Legitimate Url")

#Logistic Regression
"""classifier = lr(random_state = 0)
classifier.fit(X_train, y_train)

#predicting the tests set result
y_pred = classifier.predict(X_test)
res = classifier.score(X_test,y_test)
print("Accuracy is")
res
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)"""
