LargestNumber1 = lambda No1,No2,No3 : No1 > No2 and No1 > No3
LargestNumber2 =lambda No1,No2,No3 :  No2 > No3 and No2 > No1
LargestNumber3 =lambda No1,No2,No3 :  No3 > No2 and No3 > No1      

def main():
    Value1 = int(input("Enter the  First Numbers:"))
    Value2 = int(input("Enter the  Second  Numbers:"))
    Value3 = int(input("Enter the  Third  Numbers:"))

    Ret1 = LargestNumber1(Value1,Value2 ,Value3)
    Ret2= LargestNumber2(Value1,Value2 ,Value3)
    Ret3= LargestNumber3(Value1,Value2 ,Value3)

    print(f"Largest Number from {Value1},{Value2},{Value3} is ")
    if(Ret1 == True):
        print(Value1)

    if(Ret2 == True):
        print(Value2)

    if(Ret3 == True):
        print(Value3)


if __name__ == "__main__":
    main()