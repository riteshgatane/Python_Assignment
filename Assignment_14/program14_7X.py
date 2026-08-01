Divisibleby5 = lambda No : No % 5 == 0

def main():
    Value1 = int(input("Enter the Numbers:"))

    Ret = Divisibleby5(Value1)

    if(Ret == 1 ):
        print(f"It is a divisible by 5")
    else:
        print("It is Not a divisible by 5 ")

if __name__ == "__main__":
    main()