##*****Assignemnt # 3 ************
###Question 1: Write a program which takes 5 inputs from user for different subject's marks, total it and generate mark sheed using grades?
val1 = input("ENter first DIgit  ")
val = input("Enter Operator  ")
val2=input("Enter Second Digit  ")
val1=int(val1)
val2=int(val2)
if val == '+':
    val=val1+val2
    print(val,'is Answer')
elif val =='-':
    val = val1 - val2
    print(val,'is Answer')
elif val =='*':
    val = val1 * val2
    print(val,'is Answer')
elif val =='/':
    val = val1 / val2
    print(val,'is Answer')
else:
    print("Wrong operator")


#Q 2. Write a program to check if there is any numeric value in list using for loop'''
mylist=["sfss",34,"3432","sdf",343,389,234,"3243wer"]
for checkelement in mylist:
    if(type(checkelement)==int):
        print("Number: "+str(checkelement))
    else:
        print("String: "+checkelement)


#Q3. Write a Python script to add a key to a dictionary'''

dict={'strkey':'strvalue','numkey':34343,'numkey':32432}
dict['addnumkey']=8093

#Q 4. Write a Python program to sum all the numeric items in a dictionary'''

mylist=["sfss",34,"3432","sdf",333,389,234,"3243wer"]
sum=0
for checkelement in mylist:
    if(type(checkelement)==int):
        sum=sum+checkelement
print("Sum Result: "+str(sum))


#Q 5. Write a Python script to check if a given key already exists in a dictionary'''

dict={2:34,13:34,45:34,2:34,76:34,3:34,7:34,4:34,3:34,4:34,2:34,}
def isKeyPresent(key):
    if key in dict:
        print("Present: "+str(key))
    else:
        print("Not Present: "+str(key))
isKeyPresent(2)
isKeyPresent(42)
isKeyPresent(7)
isKeyPresent(543)


