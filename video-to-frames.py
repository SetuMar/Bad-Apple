import cv2
import os

video = cv2.VideoCapture('bad_apple.mp4')
current_frame = 0

if not os.path.exists('video-frames'):
    os.makedirs('video-frames')

while True:
    try:
        success, frame = video.read()
        cv2.imshow("Output", frame)
        cv2.imwrite('video-frames/frame' + str(current_frame) + '.jpg', frame)
        current_frame += 1
    except:
        break