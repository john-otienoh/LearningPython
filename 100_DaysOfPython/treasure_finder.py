line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure\n(ALPHABET&NUMBER): ").upper()
column, row = position[0], int(position[1]) - 1
if column == 'A':
  column = 0
elif column == 'B':
  column = 1
elif column == 'C':
  column = 2
map[row][column] = 'X'
print(f"{line1}\n{line2}\n{line3}")