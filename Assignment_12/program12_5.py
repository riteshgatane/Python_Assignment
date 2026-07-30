def Display(Value):
    i= 0 
    for i in range(Value ,0, -1):
        print(i)
    

def main():
    iRet = 0 
    A = int(input("Enter the First NUmber :"))

    Display(A)
    
    


if __name__ == "__main__":
    main()