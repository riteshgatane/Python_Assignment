def SumDigits(Value):
    iDigit = 0 
    count = 0 
    Sum = 0 
    while(Value != 0 ):
        iDigit = Value % 10
        Sum = Sum + iDigit 
        Value = Value // 10 
    return Sum
        
def main():
    No = int(input("Enter the Number to Check:"))
    Ret = SumDigits(No)
    print("Sum of Digits of the Number :",Ret)

if __name__ == "__main__":
    main()