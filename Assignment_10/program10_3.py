def Factorial(No):
    Fact = 1 
    for i in range(1,No+1):
        
        Fact  = Fact * i 
        
    return Fact
    


def main():
    Value = int(input("Enter the NUmber :"))

    Ret = Factorial(Value)

    print(f"Factorial of number is:{Ret}")



if  __name__ =="__main__":
    main()