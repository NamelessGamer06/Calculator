import CalulatorLib


Task = input("Please enter the calculation type you want to run.\nAcceptable Inputs Inclued, +, -, *, /\n")
num1 = int(input("Please enter the first number.\n"))
num2 = int(input("Please enter the second number.\n"))


if Task != "+" and Task != "-" and Task != "*" and Task != "/":
    print(Task)
    print("That Is Not A Valid Calculation Type!")
        
elif Task == "+":

    CalulatorLib.Adding(num1, num2)

elif Task == "-":
    
    CalulatorLib.Subtracting(num1, num2)

elif Task == "*":
    
    CalulatorLib.Multiply(num1, num2)

elif Task == "/":
    
    CalulatorLib.Dividing(num1, num2)
  
else: 
    print("An Unexpected Error Has Occurred. Error Code 100")