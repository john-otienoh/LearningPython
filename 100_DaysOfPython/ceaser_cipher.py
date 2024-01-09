def main():
    print("""
     _____     ____
    |  ___|   |    
    | |       |===
    | |___    |
    |_____|   |____
    """)
    option = int(input("Press\n1-Encode to encrypt\n2-Decode to decrypt\n"))
    message = input("Type your message: ").lower()
    shift_by = int(input("Type the shift number: "))
    if option == 1:
        Encrypt(text=message, shift_num=shift_by)
    elif option == 2:
        Decrypt(text=message, shift_num=shift_by)
    else:
        print("You have selected a wrong choice")

def Encrypt(text, shift_num):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_text = ''
    for letter in text:
        letter_position = alphabet.index(letter)
        new_letter_position = shift_num + letter_position
        if new_letter_position > len(alphabet):
            new_letter = alphabet[shift_num - 1]
        else:
            new_letter = alphabet[new_letter_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")
def Decrypt(text, shift_num):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded_text = ''
    for letter in text:
        letter_position = alphabet.index(letter)
        new_letter_position = letter_position - shift_num
        decoded_text += alphabet[new_letter_position]
    print(f"The decoded text is {decoded_text}")
main()