def CountDigits(Value):
    iDigit = 0 
    count = 0 
    while(Value != 0 ):
        Value = Value // 10 
        count = count+1
    return count
        
def main():
    No = int(input("Enter the Number to Check:"))
    Ret = CountDigits(No)
    print("Digits in the Number are:",Ret)

if __name__ == "__main__":
    main()