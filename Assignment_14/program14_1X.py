Square = lambda Side : (Side*Side)

def main():
    A = int(input("Enter the Number for doing the Square:"))
    Ret = Square(A)
    print("Square of the Number is :", Ret)

if __name__ == "__main__":
    main()