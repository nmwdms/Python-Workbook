from email.mime import image
from random import random, uniform
from turtle import color
from PIL import Image,ImageDraw,ImageFont
import random

try:
    head = Image.open("./head.jpg")
except IOError:
    print("unable to open")
    sys.exit(1)

#head.show()
print("size:%s",head.size[0])

head_draw = ImageDraw.Draw(head)
num = str(random.randint(1,99))
text = num

font_size = 35
font = ImageFont.truetype("arial.ttf",size=font_size)

pos_x = head.size[0] - font_size*1.5
pos_y = font_size/2
head_draw.text((pos_x,pos_y),text,font=font,fill="red")

head.show()