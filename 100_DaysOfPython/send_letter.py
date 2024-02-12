with  open('names.txt') as friends:
    my_friends = friends.readlines()

with open('letter.docx') as letter:
    my_letter = letter.read()
    for f in my_friends:
        f = f.strip()
        new_letter = my_letter.replace('[name]', f)
        with open(f"{f}.txt", mode='w') as friend_letter:
            friend_letter.write(new_letter)