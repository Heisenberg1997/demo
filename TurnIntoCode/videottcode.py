#coding = gbk

import cv2 
import os
file_name = "draw.txt"
video_name = ".mp3"
show_h = 30
show_w = 80

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

char_len = len(ascii_char)

output_list = []
if os.path.exists(file_name):
    with open(file_name,'r') as file:
        text = ""
        for line in file.readlines():
            if line =='\n':
                output_list.append(text)
                text = ""
            else:
                text +=line
else:
    vc = cv2.VideoCapture(video_name)
    if vc.isOpened():
        rval,frame = vc.read()
    else:
        rval = False
    frame_count =0
    while rval:
        gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
        gray = cv2.resize(gray,(show_w,show_h))
        text = ""
        for pix_line in gray:
            for pix in pix_line:
                text +=ascii_char[int(pix/256 *char_len)]
            text +='\n'
        output_list.append(text)
        frame_count = frame_count+1
        if frame_count %100 ==0:
            
        rval,frame_count = vc.read()
        with open(file_name,'w') as file:
            for frame in output_list:
                file.write(frame +"\n");
for frame in output_list:
    os.system("cls")
    print(frame)