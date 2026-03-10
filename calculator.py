def myCalculator():
    print("Select Operation", "\n1. Add", "\n2. Subtract", "\n3. Multiply", "\n4. Divide")

    myCalculator = (input("\nSelect Operation (1,2,3,4): "))
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))

    opNum1 = num1 + num2
    opNum2 = num1 - num2
    opNum3 = num1 * num2
    opNum4 = num1 / num2

    if myCalculator == "1":
        print("\nSolution:", num1, "+", num2, "=", int(opNum1))
    elif myCalculator == "2":
        print("\nSolution:", num1, "-", num2, "=", int(opNum2))
    elif myCalculator == "3":
        print("\nSolution:", num1, "*", num2, "=", int(opNum3))
    else:
        print("\nSolution:", num1, "/", num2, "=", int(opNum4))
        
myCalculator()