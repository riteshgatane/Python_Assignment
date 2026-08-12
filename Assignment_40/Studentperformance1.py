from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

import pandas as pd 

def StudentPerf(Datapath):

    df = pd.read_csv(Datapath)

    df.dropna(inplace=True)

    X = ["StudyHours","Attendance","PreviousScore","AssignmentsCompleted","SleepHours"]
    Y = ["FinalResult"]

    Independent = df[X]
    Dependent = df[Y]

    X_train,X_test,Y_train,Y_test = train_test_split(Independent , Dependent , test_size=0.6 , random_state=40)

    model = DecisionTreeClassifier()

    model = model.fit(X_train ,Y_train)

    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy of the model is : ",Accuracy*100)

    Importance = pd.Series(model.feature_importances_ , index = X)

    print(Importance)


def main():
    StudentPerf("student_performance_ml.csv")

if __name__ == "__main__":
    main()