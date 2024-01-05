'''Tip calculator
    total_bill = Total Amount Consumed
'''
#!/usr/bin/python3
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip would you like to give? 10, 12 or 15 "))
total_people = int(input("How many people to split the bill? "))
total_payable = (tip_percent / 100 + 1) * total_bill
total_divided = total_payable / total_people
print("Each person should pay: ${:.2f}".format(total_divided))