def main():
    n = int(input("Enter a number you want to check: "))
    result = PrimeNumberChecker(n)
    if result:
        print("It is a prime number")
    else:
        print("It is not a prime number")
        
def PrimeNumberChecker(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
main()