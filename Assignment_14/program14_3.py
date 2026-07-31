def Max(No1 , No2):
    if(No1 > No2):
        return No1
    
    else:
        return No2

def main():
    Value1 = int(input("Enter the 1st Numbers:"))
    Value2 = int(input("Enter the 2nd Number"))

    Ret = Max(Value1 , Value2)
    print("Max of the Number is :", Ret)

if __name__ == "__main__":
    main()