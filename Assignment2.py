##Question # 1
print("*** Marksheet ***")
English= int(input("Enter your marks of English out of 100 = "))
Urdu= int(input("Enter your marks of Urdu out of 100 = "))
Chemistry= int(input("Enter your marks of Chemistry out of 100 = "))
Physics= int(input("Enter your marks of Physics out of 100 = "))
Maths= int(input("Enter your marks of Maths out of 100 = "))
Pakistan_Studies= int(input("Enter your marks of Pakistan Studies out of 100 = "))
Islamiat= int(input("Enter your marks of Islamiat out of 100 = "))
Total_marks= English+Urdu+Chemistry+Physics+Maths+Pakistan_Studies+Islamiat
Percentage= (Total_marks/700)*100
print("Your Total Marks are " + str(Total_marks))
print("Your Percentage is" + " " + str(Percentage))
if Percentage >= 90 and Percentage <=100:
 print("Congratulations! You have secured Grade A")
elif Percentage <90 and Percentage >=80:
 print("Congratulations! You have secured Grade B")
elif Percentage <80 and Percentage >=70:
 print("Congratulations You have secured Grade C")
elif Percentage <70 and Percentage >=60:
 print("Congratulations You have secured Grade D")
else:
 print("You have failed in examinations")




##Question # 2

num = int(input("Enter Number to check wheater Num is Odd or Even= "))
if (num % 2)==0:
    print("{0} is Even".format(num))
else :
    print("{0} is ODD".format(num))




#

n = int(input("Enter number of elements : "))
# Below line read inputs from user using map() function
a = list(map(int, input("\nEnter the numbers : ").strip().split()))[:n]

print("\nList is - ", a)

# 3 Write a program which print the length of the list?
print("length of list is ", len(a))

#5. Write a Python program to get the largest number from a numeric list.
print("Largest number is ", max(a))

#4. Write a Python program to sum all the numeric items in a list?
print("Sum of list is", sum(a))

#6 Take a list, say for example this one:
##a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
##and write a program that prints out all the elements of the list that are
##less than 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

new_list = []

for item in a:
    if item<5:
        new_list.append(item)
print(new_list)
