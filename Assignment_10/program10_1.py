def Multiplication(No):

    for i in range(1,11):
        Mult = (No * i)
        print(Mult)
        
    


def main():
    Value = int(input("Enter the NUmber :"))

    Ret = Multiplication(Value)



if  __name__ =="__main__":
    main()