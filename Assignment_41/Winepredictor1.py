import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def WinePredictor(Datapath):

    #Step 1 : Load the Data 
    border = "-"*30
    df = pd.read_csv(Datapath)
    border = "-"*30


    print(df.head())

    #step 2:  Data
    #Check and Deletes the Null Data
    df.dropna()

    #Delete the Duplicate Rows 
    df.drop_duplicates()

    print(border)
    print("Data is :\n",df)
    print(border)

    #Step 3 : Seprating the Feature and Labels for the Data
    feature_col = ["Alcohol","Malic acid","Ash","Alcalinity of ash","Magnesium","Total phenols","Flavanoids",
                   "Nonflavanoid phenols","Proanthocyanins","Color intensity","Hue","OD280/OD315 of diluted wines","Proline"]

    #features
    X = df[feature_col]

    #Labels
    Y = df["Class"]


    #Train & Test the Data
    #Spliting the 
    #Step 4 : Spliting the data For Traing and test 
    X_train , X_test , Y_train , Y_test = train_test_split(X,Y,test_size= 0.6 , random_state=42)

    #Step 5 : Data training through DecisionTreeClassifier
    model = DecisionTreeClassifier()


    model = model.fit(X_train ,Y_train)
    
    Y_pred = model.predict(X_test)

    #Step 6: Claculating the Accuracy 
    Accuracy = accuracy_score(Y_test,Y_pred)

    print("Accuracy  is : " , Accuracy)


def main():
    WinePredictor("WinePredictor.csv")

if __name__ == "__main__":
    main()