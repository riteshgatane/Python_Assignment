import pandas as pd 


def StudentPerfo():
    Border = "-"*30
    #step 1 : read Dataset 

    print(Border)
    print("Step 1 : Read Dataset" )
    print(Border)

    df = pd.read_csv("student_performance_ml.csv")

    print("UPPER DATA OF DATASET")
    print(df.head(10))
    print("\n")

    print("UPPER DATA OF DATASET")
    print(df.tail())

    #TELLS THE TOTOL ROWS AND COLUMNS 
    print(df.shape) 

    print("\n")
    print("List of Columns Names : ",df.columns)

    print("\n")
    print(df.dtypes) #For check the datatype of Each Columns


    #2
    print("Total Number of Students: ",df.shape[0])

    countp = 0 
    countf = 0 
    x = df["FinalResult"]
    for i in x: 
        if(i == 1):
            countp = countp + 1
        if(i == 0 ):
            countf = countf + 1 

    print("Number of Pass Students:",countp)
    print("Number of Fail Students :",countf)

    





        
        




    







    






def main():
    StudentPerfo()

if __name__ =="__main__":
    main()