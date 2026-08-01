Min = lambda No1,No2 : No1 < No2 

def main():
    Value1 = int(input("Enter the 1st Number :"))
    Value2 = int(input("Enter the 2nd Number : "))

    Ret = Min(Value1 , Value2)

    if(Ret == True):
        print("Min of the Number is :",Value1)
    else:
        print("Min of the Number is :",Value2)

if __name__ == "__main__":
    main()