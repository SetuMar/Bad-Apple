from PIL import Image


characters = '@#S%?*+;:,.'
# to invert colors, just reverse characters:
# character = '.,:;+*?%S#@'

def generate_ascii_image(path, height_division_amt):
    image = Image.open(path)
    width_division_amt = height_division_amt / 2
    image = image.resize((int(image.width / width_division_amt), int(image.height / height_division_amt)))
    image_width = image.width

    # O(n) concatenated list of characters, its better then "str += str",
    # https://peps.python.org/pep-0008/#programming-recommendations
    output = ''.join([characters[p[0] // 25] for p in image.getdata()])

    # '\n'.join([]) instead of print every line of frame separately
    # It makes a list of strings, each lenght string is equal to the width of the frame
    output = '\n'.join([output[i:i + image_width] for i in range(0, len(output), image_width)])
    return output
