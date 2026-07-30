def Addition(Value1,Value2):
    Sum = 0 
    Sum = Value1 + Value2
    return Sum 

def Subtraction(Value1,Value2):
    Sub = 0 
    Sub = Value1 - Value2
    return Sub

def Division(Value1,Value2):
    Div = 0 
    Div = Value1 / Value2
    return Div

def Multiplication(Value1 , Value2):
    Mult = 0 
    Mult = Value1*Value2
    return Mult

def main():
    iRet = 0 
    A = int(input("Enter the First NUmber :"))
    B = int(input("Enter the second Number :"))

    iRet = Addition(A,B) 
    print("Addition is :",iRet)

    iRet = Subtraction(A,B)
    print("Subtraction is :",iRet)

    iRet = Multiplication(A,B)
    print("Multiplication is :",iRet)

    iRet = Division(A,B)
    print("Division is :",iRet)




if __name__ == "__main__":
    main()