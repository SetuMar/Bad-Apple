import PIL.Image as pillow
import copy

def generate_ascii_image(path, height_division_amt):
    image = pillow.open(path)

    height_division_amt = height_division_amt
    width_division_amt = height_division_amt/2

    sized_image = image.resize((int(image.width/width_division_amt), int(image.height/height_division_amt)))

    img_data = sized_image.getdata()

    character = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    output = ""

    for p in img_data:
        output += character[p[0]//25]
        
    image_width = sized_image.width

    last = 0

    for index, char in enumerate(copy.copy(output)):
        if index % image_width == 0:
            print(output[last:index])
            last = index