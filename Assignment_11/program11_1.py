def CheckPrime(Value):##
    if(Value%1 == 0 and Value%Value == 0 ):
        {
            print(f"{Value} is prime Number")
        }
    else:
        print(f"{value} is not a prime Number")

def main():
    No = int(input("Enter the Number to Check:"))
    CheckPrime(No)

if __name__ == "__main__":
    main()