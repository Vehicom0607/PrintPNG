import cv2
img = cv2.imread('./image.png')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

charlist = "$@B%8&WM#oahkbdpqwmZO0QLCJUYXzcvunxrjf/\|(){}[]?-_+<>i!lI:,^`'. "

for row in gray_img:
    string = ""
    for pixel in row:
        string += charlist[int(pixel/4)]
    string += '\n'
    print(string)

