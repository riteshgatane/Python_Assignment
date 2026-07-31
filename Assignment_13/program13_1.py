def Rectangle(Length , Width):
    iArea = 0 
    iArea = Length * Width
    return iArea

def main():
    Ret = 0 
    A = int(input("Enter the Length :"))
    B = int(input("Enter the Width : "))

    Ret = Rectangle(A , B)
    print("Area of Rectangle is : ",Ret)


if __name__ == "__main__":
    main()