str = input("Enter Your String")
print(str)
countC = 0
countW = 1
for i in str:
    countC = countC + 1
    if i ==' ':
        countW = countW + 1
print("Number Of Characters Is ")
print(countC)
print("Number Of words Is ")
print(countW)