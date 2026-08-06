import os 

def Display(FileName):
    fobj = open(FileName, "r")

    Line  = fobj.readline()

    Count = 0 
    for i in Line:
        Count = Count +1 
    
    return Count


def main():
    print("Enter the FileName")
    FileName = input()

    Ret = Display(FileName)
    print(f"Number of Words in the {FileName} is :",Ret)

if __name__ == "__main__":
    main()