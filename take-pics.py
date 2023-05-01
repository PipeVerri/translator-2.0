import os
import re
import cv2

currentPic = ""
count = {}

for file in os.listdir("pictures"):
    res = re.search(r"(.+)_.+\..+", file)
    f_name = res.group(1)

    if not (f_name in count.keys()):
        count[f_name] = 1
    else:
        count[f_name] += 1

cap = cv2.VideoCapture(0)

while True:
    currentPic = input("Write the current pic you're taking(by default the last one):")
    ret, frame = cap.read()

    if not ret:
        print("No camera was detected, try again")
        continue

    name = f"pictures/{currentPic}_{count[currentPic]}.png"
    cv2.imwrite(name, frame)