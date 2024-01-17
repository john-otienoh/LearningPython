def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    my_name = format_name(first_name, last_name)
    print(my_name)

def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f"My name is {f_name} {l_name}"
main()