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