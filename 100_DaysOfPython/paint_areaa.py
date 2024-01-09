def main():
    test_h = int(input("Height of the wall: "))
    test_w = int(input("Width of the wall: "))
    coverage = 5
    PaintArea(height=test_h, width=test_w, cover=coverage)

def PaintArea(height, width, cover):
    can_numbers = (height * width) / cover
    print(f"You'll need {round(can_numbers)} of paint cans")
main()