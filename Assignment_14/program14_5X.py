Even = lambda No1 : No1%2 == 0

def main():
    Value1 = int(input("Enter the Numbers:"))

    Ret = Even(Value1)

    if(Ret == 0 ):
        print("It is Not a Even Number")
    else:
        print("Even of the Number is :" ,Ret)


if __name__ == "__main__":
    main()