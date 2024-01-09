def main():
    greet(input("Enter your name: "), input("Enter your location: "))

def greet(name='', location=''):
    print(f"I am {name} from {location} and i love Python")

main()