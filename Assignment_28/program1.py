import os 

def Display(FileName):
    fobj = open(FileName, "r")

    Line  = fobj.readlines()

    for i in Line:
        print(i)
def main():
    print("Enter the FileName")
    FileName = input()

    Display(FileName)

if __name__ == "__main__":
    main()
