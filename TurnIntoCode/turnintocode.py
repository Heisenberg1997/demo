
#print '\x42\x65\x20\x77\x69\x74\x68\x20\x6D\x65'
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

show_h = 60
show_w = 120

codeLib = list("@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,^`'.") 
char_len = len(codeLib)

pic = plt.imread("/home/heisenberg/pic/baoxiao.jpeg")

pic_h,pic_w,a = pic.shape
#pic_h =pic.shape.height
#pic_w =pic.shape.weight
#将图像转换成灰度图
gray = 0.2126 * pic[:,:,0] + 0.7152 * pic[:,:,1] +0.0722 * pic[:,:,2]

for i in range(show_h):
    y = int (i * pic_h / show_h)
    text = ""
    for j in range(show_w):
        x=int(j* pic_w/show_w)
        text += codeLib[int(gray[y][x]/256 *char_len)]
    print(text)
