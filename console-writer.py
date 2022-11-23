import os
import time
from pathlib import Path

import pygame

import custom_ascii_converter


abs_path = Path().absolute()  # absolute path for "multiplatform", relative paths don't work well on some systems
frames_path = abs_path / 'video-frames'
frame_names = 'frame'  # file names before their number, file name should be like "frame1002.jpg"
extension = '.jpg'
height_division_amt = 15
delay = 0.024  # delay between frames in ms, play with this value if there are "frame glitches"

pygame.init()
pygame.mixer.music.load(abs_path / 'bad_apple.mp3')

image_locations = None
for _, _, file_names in os.walk(frames_path):
    image_locations = file_names
    break

if image_locations is None:
    raise FileNotFoundError(f'There are no frames! Launch "video-to-frames.py" before running this script.')

indexed_images = map(lambda x: x[1],
                     sorted([(int(path.lstrip(frame_names).split(extension)[0]), path) for path in image_locations])
                     )

print("loading...")
pygame.mixer.music.play()
time.sleep(3)

for image_loc in indexed_images:
    print(custom_ascii_converter.generate_ascii_image(frames_path / image_loc, height_division_amt))
    time.sleep(delay)

print("VIDEO OVER. CLOSE THE CONSOLE, WEABOO")
