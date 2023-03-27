
print("please select the operation:")

print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

operation = input ()

num1= int (input ("Please enter the first number: "))
num2= int (input ("Please enter the first number: "))

if operation =="a":
 print(num1 + num2)
  #add
elif operation  =="b":
 print(num1 - num2)
  #subtract
elif operation =="c":
 print(num1 * num2)
  #multiply
elif operation =="d":
 print(num1 / num2)
  #divide
else:
 print("Invalid Entry")



    
