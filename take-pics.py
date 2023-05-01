from tools import *
import os
import re
import cv2

oldCurrentPic = ""
count = {}

for file in os.listdir("pictures"):
    res = re.search(r"(.+)_.+\..+", file)
    f_name = res.group(1)

    if not (f_name in count.keys()):
        count[f_name] = 1
    else:
        count[f_name] += 1

while True:
    currentPic = input("Write the current pic you're taking(by default the last one):")
    if currentPic == "":
        currentPic = oldCurrentPic
    else:
        oldCurrentPic = currentPic

    img = next(inputs.read_image())
    if img is None:
        print("There was an error detecting the camera")
        continue

    if inputs.get_landmarks(img) is None:
        print("There was an error analyzing the image, check the lighting")
        continue

    if not (currentPic in count.keys()):
        count[currentPic] = 1

    name = f"pictures/{currentPic}_{count[currentPic]}.png"
    cv2.imwrite(name, img)

    count[currentPic] += 1