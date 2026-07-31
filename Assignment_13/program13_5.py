def Grade(Marks):
    if(Marks >= 75):
        print("Distinction")
    
    elif(Marks >= 60):
        print("First Class")

    elif(Marks >= 50):
        print("Second Class")
    else:
        print("fail")


def main():
    Ret = 0 
    A = int(input("Enter Marks :"))
    Grade(A)


if __name__ == "__main__":
    main()