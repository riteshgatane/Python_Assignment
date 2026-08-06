import os 

def Display(FileName1 ,FileName2 , Word1):
    fobj = open(FileName1, "r")
    pobj = open(FileName2 , "r")

    Line1  = fobj.readline()
    Line2  = fobj.readline()
   
    if Word1 in fobj.read():
        print("Word Found ")

            


def main():
    print("Enter the FileName to Copy the Contents")
    FileName1 = input()

    print("Enter the FileName to Paste the Contents")
    FileName2 = input()

    print("Enter the Word to Find ")
    Word = input()

    Display(FileName1,FileName2,Word)

if __name__ == "__main__":
    main()