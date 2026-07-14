def Even(No):
    EvenNumbers = []
    for i in range(0,No+1,2):
        EvenNumbers.append(i)

    return EvenNumbers        
        
    
    


def main():
    Value = int(input("Enter the NUmber :"))

    Ret = Even(Value)
    print(f"Even Number till {Value} are ")
    for no in Ret:
        print(no)

    



if  __name__ =="__main__":
    main()