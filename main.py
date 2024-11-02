
summa = 0

def exit2():
    input("........")

def even_numb():
    global summa
    print("\n\t\tEVEN NUMBERS\n")
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        print(f'\nEven numbers from range {start} -- to {end} is :')
        for number in range(start, end + 1):
            if number % 2 == 0:
                print(number, end=",")
                summa +=number

        print("\nSum of even numbers --- ",summa) 
    except ValueError:
        print("Invalid input! Please enter integers.")
    user = input("Click to the enter button, in order to go back!!.....")
    menu()

def addition():
    print("\n\t\tADDITION\n")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a + b)
    except ValueError:
        print("Invalid input! Please enter numbers.") 
    user = input("Click to the enter button, in order to go back!!.....")
    menu()

def substraction():
    print("\n\t\tSUBSTRACTION\n")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a - b)
    except ValueError:
        print("Invalid input! Please enter numbers.")
    user = input("Click to the enter button, in order to go back!!.....")
    menu()

def mult():
    print("\n\t\tMULTIPLICATION\n")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result:", a * b)
    except ValueError:
        print("Invalid input! Please enter numbers.")
    user = input("Click to the enter button, in order to go back!!.....")
    menu()

def divis():
    print("\n\t\tDIVISION\n")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Division by zero is not allowed.")
        else:
            print("Result:", a / b)
    except ValueError:
        print("Invalid input! Please enter numbers.")
    user = input("Click to the enter button, in order to go back!!.....")
    menu()
    
def modulos():
    print("\n\t\tMODULOS\n")
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b == 0:
            print("Error: Modulus by zero is not allowed.")
        else:
            print("Result:", a % b)
    except ValueError:
        print("Invalid input! Please enter numbers.")
    user = input("Click to the enter button, in order to go back!!.....")
    menu()


def menu():
    print("""

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝


    [1] - Addition.             [4] - Division.
    [2] - Substraction.         [5] - Modulos.
    [3] - Multiplication.       [6] - Even numbers.
                                        (from range!)

                    [0] - EXIT

                                            
""")
    while True:
        user = input("SELECT OPTION -- ")
        if user == "1":
            addition()
            break
        elif user == "2":
            substraction()
            break
        elif user =="3":
            mult()
            break
        elif user == "4":
            divis()
            break
        elif user == "5":
            modulos()
            break
        elif user == "6":
            even_numb()
            break
        elif user == "0":
            exit2()
            break
        else:
            print("Please choose the correct option!!!")





menu()