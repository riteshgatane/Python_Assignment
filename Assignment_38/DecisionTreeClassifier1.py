from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from sklearn.metrics import accuracy_score,confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt 


def StudentPerFomannce(Datapath):

    # Step 1: Load data 
    df = pd.read_csv(Datapath)

    # Step 2: Clean data 
    df.dropna(inplace=True)

    # Step 3:Data Analysis 
    X = ["StudyHours", "Attendance", "PreviousScore", "AssignmentsCompleted", "SleepHours"]
    Y = ["FinalResult"]

    Independent = df[X]
    Dependent = df[Y]


    #Dependent and Independent data 
    X_train, X_test, Y_train, Y_test = train_test_split(Independent, Dependent, test_size=0.6, random_state=40)

    # Initialize and train the model
    model = DecisionTreeClassifier()
    model = model.fit(X_train, Y_train)

    #Test and predict
    Y_pred = model.predict(X_test)

    Accuracy = accuracy_score(Y_test,Y_pred)
    print("Accuracy Score is :",Accuracy*100)

    #step 4 :Visualization 
    con = confusion_matrix(Y_test , Y_pred)
    print(con)

    
    display = ConfusionMatrixDisplay(confusion_matrix=con ,  display_labels=["Pass" , "Fail"])

    display.plot()
    plt.show()

    #######################################################
    #OVERFITTING(Training more) &  UNDERFITTING (Testing more) 
    #######################################################
    Y_pred_test = model.predict(X_test)
    test_accuracy = accuracy_score(Y_test , Y_pred_test)

    Y_pred_train = model.predict(X_train)
    train_accuracy = accuracy_score(Y_train , Y_pred_train)

    print("Testing Accuracy :",test_accuracy*100)
    print("Training Accuracy is : ",train_accuracy*100)

    #MODEL IS OVERFITTING


    ########################################
    #Test with Decision tree max depth 
    ########################################

    new_student = pd.DataFrame([{
        "StudyHours": 5,
        "Attendance": 85,
        "PreviousScore": 66,
        "AssignmentsCompleted": 7,
        "SleepHours": 2
    }])

    prediction = model.predict(new_student)

    print(prediction[0]*100)


def main():
    StudentPerFomannce("student_performance_ml.csv")

if __name__ == "__main__":
    main()
