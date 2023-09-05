numb1=int(input("enter the number:"))#this is called type casting
numb2=float(input("enter the number:"))
numb3=bool(input("enter the number:"))
numb4=input("enter the number:")
print (type(numb1))
print (type(numb2))
print (type(numb3))
print (type(numb4))
#if else checking 
#eliif can also be user to increase number of if conditions
if numb1<22:
    print("value is smaller than 22")
else:
    print("you can proceed")

# calculator


calculate_operation = input ("enter the operaatin to perform :")
if calculate_operation == "+":
    output=numb1+numb2
elif calculate_operation == "*":
    output=numb1*numb2
elif calculate_operation == "/":
    output=numb1/numb2
else:
    output=numb1-numb2
print("your answer is :",output)


    