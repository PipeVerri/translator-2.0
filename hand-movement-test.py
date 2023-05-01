from tools import *

while True:
    img = next(inputs.read_image())
    print(inputs.get_landmarks(img))
