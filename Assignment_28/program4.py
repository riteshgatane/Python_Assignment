import os 

def Display(FileName1 ,FileName2):
    fobj = open(FileName1 , "r")
    pobj = open(FileName2 , "w")

    Line  = fobj.readlines()

    for i in Line:
        pobj.write(i)

    

def main():
    print("Enter the FileName to Copy the Contents")
    FileName1 = input()

    print("Enter the FileName to Paste the Contents")
    FileName2 = input()

    Display(FileName1,FileName2)

if __name__ == "__main__":
    main()