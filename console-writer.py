import os
import pywhatkit
import time

image_locations = None

for a, b, path in os.walk('video-frames'):
    image_locations = path

index_image = {}

for loc in image_locations:
    index_image.update({int(loc.split('e')[1].split('.')[0]):loc})

index_image = dict(sorted(index_image.items()))
sorted_image_location = index_image.values()

time.sleep(3)

for image_loc in sorted_image_location:
    full_path = 'video-frames/' + image_loc
    text_file_name = image_loc.split('.')[0]
    pywhatkit.image_to_ascii_art(full_path, text_file_name)
    
    contents = open(text_file_name + '.txt')
    
    for w in contents:
        print(w.strip('\n'))
    
    os.remove(text_file_name + '.txt')
    
    time.sleep(0.009)
    os.system('clear')