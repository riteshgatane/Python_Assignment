odd = lambda No : No % 2 == 1

def main():
    Value1 = int(input("Enter the Numbers:"))

    Ret = odd(Value1)

    if(Ret == 1 ):
        print("It is a odd Number ")
    else:
        print("It is Not a odd Number")

if __name__ == "__main__":
    main()