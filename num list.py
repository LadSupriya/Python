NumList = []
Number = int(input("Please enter how many numbers do you want to enter "))
for i in range(1, Number + 1):
 value = int(input("Please enter the Value of %d Element : " %i))
 NumList.append(value)
print("The Minimum number in this List is : ", min(NumList))
print("The maximum number in this List is : ", max(NumList))