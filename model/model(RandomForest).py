import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
import pickle
from sklearn.metrics import confusion_matrix

data = pd.read_csv("employeeData.csv")
data['Behavior'] = data['Behavior'].map({"Excellent": 5, "Good": 4, "Average": 3, "Below Average": 2, "Bad": 1})

X = data[["Allocated_Days", "Completed_In_Days", "isOnTime", "Appraisal_Cycles", "YearsInCompany", "Complaints_received", "average_monthly_hours"]]
Y = data["Behavior"]

Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size=0.2, random_state=0)

rfc = RandomForestClassifier()
#rfc.fit(Xtrain, Ytrain)
abc = AdaBoostClassifier(n_estimators=100,learning_rate=1, base_estimator=rfc)
abc.fit(Xtrain, Ytrain)
# Ypred = abc.predict(Xtest)
# accu = accuracy_score(Ypred, Ytest)
# report = classification_report(Ytest, Ypred, output_dict=True)
# precision = report['macro avg']['precision']
# recall = report['macro avg']['recall']
# confusion = confusion_matrix(Ytest, Ypred)
# print("Accuracy = ", accu)
# print(precision, recall)
# print(confusion)

pickle.dump(abc, open("model1.pkl", "wb"))

allocated_days = int(input("Enter allocated days: "))
completed_days = int(input("Enter completed in days: "))
isOnTime = int(input("Is employee on time?: "))
appraisal = int(input("How many appraisal?: "))
years_in_company = int(input("Years in company: "))
complaints = int(input("Complaints Received: "))
avgHours = int(input("Average Monthly Hours: "))
input_data = [[allocated_days, completed_days, isOnTime, appraisal, years_in_company, complaints, avgHours]]

Ypred = abc.predict(input_data)
print(Ypred)
print(abc.score(Xtest, Ytest))