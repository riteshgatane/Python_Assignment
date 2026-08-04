def LargestNumber( No1,No2,No3 ):
    if(No1 > No2 and No1 > No3):
        return No1
    elif(No2 > No3 and No2 > No1):
        return No2
    else:
        return No3

def main():
    Value1 = int(input("Enter the  First Numbers:"))
    Value2 = int(input("Enter the  Second  Numbers:"))
    Value3 = int(input("Enter the  Second  Numbers:"))

    Ret = LargestNumber(Value1,Value2 ,Value3)
    print(f"Largest Number From{Value1},{Value2},{Value3} is {Ret}")

if __name__ == "__main__":
    main()