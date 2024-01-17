''' Created a calculator
    using if, elif and else statement.
'''
#!/usr/bin/python3
def main():
    operator = "0"
    while operator != "7":
        operator = input("Press\n1 - Add\n2 - Subtraction\n3 - Multiplication\n4 - Division\n5 - Floor Division\n6 - Exponantion\n7 - Quit\n")
        if operator != "7":
            digit_one = int(input("Enter First Digit: "))
            digit_two = int(input("Enter Second Digit: "))
            if operator == "1":
                print(f"Addition of {digit_one} and {digit_two} = {addition(digit_one, digit_two)}")
            elif operator == "2":
                print(f"Subtraction of {digit_one} from {digit_two} = {subtraction(digit_one, digit_two)}")
            elif operator == "3":
                print(f"Multiplication of {digit_one} and {digit_two} = {multiplication(digit_one, digit_two)}")
            elif operator == "4":
                print(f"Division of {digit_one} from {digit_two} = {division(digit_one, digit_two)}")
            elif operator == "5":
                print(f"Floor Division of {digit_one} from {digit_two} = {FloorDivision(digit_one, digit_two)}")
            elif operator == "6":
                print(f"{digit_one} raised to power {digit_two} = {exponantion(digit_one, digit_two)}") 
        else:
            print("You are now quitting")

def addition(num_one, num_two):
    return num_one + num_two
def subtraction(num_one, num_two):
    return num_one - num_two
def multiplication(num_one, num_two):
    return num_one * num_two
def division(num_one, num_two):
    return num_one / num_two
def FloorDivision(num_one, num_two):
    return num_one // num_two
def exponantion(num_one, num_two):
    return num_one ** num_two
main()