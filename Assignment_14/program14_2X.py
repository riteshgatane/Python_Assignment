Cube= lambda Side : Side*Side*Side

def main():
    A = int(input("Enter the Number for doing the Cube:"))
    Ret = Cube(A)
    print("Cube of the Number is :", Ret)

if __name__ == "__main__":
    main()