#This a calaculator that takes a number of numbers to perform the average on

while True:
    try:
        total_number = int(input("Number of numbers to perform the average on : "))
    except ValueError:
        print("Invalid number of numbers")
    break

The_List = []
try:
    for i in range(total_number):
        num = int(input(f"Enter element {i + 1} : "))
        The_List.append(num)
except ValueError:
    print("Not a number")

#Checking if the numbers to calculate are more than 1
while True:
    if len(The_List) == 1:
        print("Invalid number \n Please enter a number more than 1") 
        break
    else:
     break
    
average = sum(The_List)/len(The_List)
print(f"The average is {average}")
