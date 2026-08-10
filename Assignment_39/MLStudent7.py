import pandas as pd 
import matplotlib.pyplot as plt

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

    #3
    StudyHours = df["StudyHours"]
    sum = 0 
    count = 0 
    Average = 0 

    for i in StudyHours:
        sum = sum + i 
        count = count + 1

    Average = sum / count
    print("Average StudyHours of Students :" , Average)

    print(Border)
    AvgAttendance = df["Attendance"].mean()
    print("Average Attendance of the Students is : ",AvgAttendance)
    print(Border)

    print(Border)
    #Maximum Score 
    MaxPrevScore = df["PreviousScore"].max()
    print("Maximum Number of Loop:",MaxPrevScore)
    print(Border)

    print(Border)
    #Minimum SleepHours 
    MiniSleepHours = df["SleepHours"].min()
    print("Minimum SleepHours of Students : ",MiniSleepHours)
    print(Border)

    #4
    print(Border)
    FinalResults = df["FinalResult"].value_counts(normalize= True)

    print("Percentage of the Students Pass(1): ",FinalResults[1]*100)
    print("Percentage  of the Students Fail(0): ",FinalResults[0]*100)
    print(Border)

    #5
    #StudyHours = df["StudyHours"].value_counts(normalize= True)
    #print(StudyHours)


    #6
    plt.hist(
        StudyHours,
        bins=5,
        edgecolor="blue",
        alpha=1,
        rwidth=0.9
    )
    plt.title("Historgram of Study Hours")
    plt.xlabel("Marks")
    plt.ylabel("Hours")
    plt.show()


    #7
    plt.scatter(
        df.index,
        df["StudyHours"],
        color = "orange",
        marker='o',
        edgecolor="red",
        alpha=1
    )
    plt.scatter(
            df.index,
            df["PreviousScore"],
            color = "green",
            marker='^',
            edgecolor="Blue",
            alpha=0.8
        )

    plt.title("Historgram of Study Hours")
    plt.xlabel("StudyHours")####
    plt.ylabel("Previous Score")
    plt.grid(True)
    plt.show()


    #8
    plt.boxplot(
    df["PreviousScore"], 
    vert=False,         # Makes it horizontal
    notch=True,         # Adds a confidence interval notch
    patch_artist=True,  # Enables box fill color
    labels=['Attendance']      # Labels the dataset axis
    )


def main():
    StudentPerfo()

if __name__ =="__main__":
    main()