''' Created a calculator
    using if, elif and else statement.
'''
#!/usr/bin/python3
# Ask the user which operation to carry out
operator = "0"
while operator != "7":
    operator = input("Press\n1 - Add\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Floor Division\n6 - Exponantion\n7 - Quit\n")
    if operator == "1":
        num_one = input("Enter First Digit: ")
        num_two = input("Enter Second Digit: ")
        result = int(num_one) + int(num_two)
        print(f"Addition of {num_one} and {num_two} is {result}")
    elif operator == '2':
        num_one = input("Enter First Digit: ")
        num_two = input("Enter Second Digit: ")
        result = int(num_one) - int(num_two)
        print(f"Subtraction of {num_one} and {num_two} is {result}")
    elif operator == '3':
        num_one = input("Enter First Digit: ")
        num_two = input("Enter Second Digit: ")
        result = int(num_one) * int(num_two)
        print(f"Multiplication of {num_one} and {num_two} is {result}")
    elif operator == '4':
        num_one = input("Enter First Digit: ")
        num_two = input("Enter Second Digit: ")
        result = int(num_one) / int(num_two)
        print(f"Division of {num_one} and {num_two} is {result}")
    elif operator == '5':
        num_one = input("Enter First Digit: ")
        num_two = input("Enter Second Digit: ")
        result = int(num_one) // int(num_two)
        rem = '0'
        option = input("Do you want  to see your remainder\n1 - Yes\n2 - No\n")
        if option == '1':
            rem = int(num_one) % int(num_two)
            print(f"Floor Division of {num_one} and {num_two} is {result} with {rem} as the remainder")
        else:
            print(f"Floor Division of {num_one} and {num_two} is {result}")
    elif operator == '6':
        num_one = input("Enter number: ")
        num_two = input("Enter base: ")
        result = int(num_one) ** int(num_two)
        print(f"Exponiantion of {num_one} base {num_two} is {result}")
print("You are now quiting")
