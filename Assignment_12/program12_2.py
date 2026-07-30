Number = int(input("Enter the Number "))

NewNum = 0 
i = 1
if(Number % 2 == 0 ):
    for i in range(1 , Number + 1):
        if Number % i == 0:
            NewNum = Number // i
            print(i)
        
