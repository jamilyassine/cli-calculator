print("Welcome to the CLI Calculator! You can perform +, -, *, /")

while(True):
    try:
        first_number=float(input("Enter the first number : \n"))
        break
    except ValueError:
        print("Invalid Number. Try again !  ",end="")
while(True):
    try:
        second_number=float(input("Enter the second number : \n"))
        break
    except ValueError:
        print("Invalid Number. Try again ! ",end="")

operation=input("Enter the operation ")
while(operation.strip() not in ["+","-","*","/"]):
    operation=input("Please enter one of the following valid operations + , - , * , / \n")

if(operation.strip()=="+"):
    print(f"{first_number}  +  {second_number}  =  {first_number+second_number}")
elif(operation.strip()=="-"):
        print(f"{first_number}  -  {second_number}  = {first_number-second_number}")
elif(operation.strip()=="/"):
        try:
            print(f"{first_number}  /  {second_number}  = {first_number/second_number}")
        except ZeroDivisionError:
            print("Zero Division Error : You can not divide by zero\n")
            while(True):
                try:
                    second_number=float(input("Enter a valid second number : \n"))
                    print(f"{first_number}  /  {second_number}  = {first_number/second_number}")
                    break
                except ZeroDivisionError:
                    print("Invalid Number. Try again ! ",end="")
                except ValueError:
                    print("Error: Please enter a valid number.",end="")
        
    
elif(operation.strip()=="*"):
    print(f"{first_number} *   {second_number}  = {first_number*second_number}")


