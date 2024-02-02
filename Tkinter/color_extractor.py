import colorgram

rgb_colors = []
image = input("Enter your image: ")
colors = colorgram.extract(image, 30)
for color in colors:
    rgb_colors.append(color.rgb)
print(rgb_colors)