import string
from PIL import Image,ImageDraw,ImageFont,ImageFilter

import random

# 生成随机颜色
def randcolor():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))

# 生成随机大小写字母
def randletter():
    return random.choice(string.ascii_letters)

# 生成字母验证码
def generate_verify_code(width,height):
    # 创建image对象
    image = Image.new('RGB',(width,height))
    # 创建draw对象，对image进行操作
    draw = ImageDraw.Draw(image)
    
    # 对每个像素点进行着色
    for x in range(width):
        for y in range(height):
            draw.point((x,y), fill=randcolor())
    
    font = ImageFont.truetype('arial.ttf', 36)
    # 放上字母
    for i in range(4):
        draw.text((60*i+10,10), randletter(), fill=randcolor(), font=font)

    # 对图片进行模糊处理
    image = image.filter(ImageFilter.BLUR)
    # 保存图片
    image.save('./test10/verify_code.jpg')

if __name__ == '__main__':
    width = 60 * 4
    height = 60
    generate_verify_code(width, height)