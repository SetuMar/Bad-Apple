from pathlib import Path
import os

import cv2


abs_path = Path().absolute()

video = cv2.VideoCapture(str(abs_path / 'bad_apple.mp4'))
current_frame = 0

if not os.path.exists('video-frames'):
    os.makedirs('video-frames')

frames_path = abs_path / 'video-frames'
print("It's a long process...")

while True:
    try:
        success, frame = video.read()
        cv2.imshow("Output", frame)
        cv2.imwrite(str(frames_path / f'frame{current_frame}.jpg'), frame)
        current_frame += 1
    except Exception:
        break
