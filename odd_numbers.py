while True:
    start = int(input("The start of the range"))
    end = int(input("The end of the range"))
    
    if(start > end):
        print("Enter a start range lower than the end")
    else:
        break
for i in range(start,end):
    if int((i%2) == 0):
        print("i")


        