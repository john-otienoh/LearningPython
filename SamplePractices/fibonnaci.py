#!/usr/bin/python3
a, b, = 0, 1
fibo = input("Enter a range for fibonacci: ")
while b <= int(fibo):
    print(b, end=', ')
    a, b = b, a + b
