import json
import os
from PIL import Image

# 获取宽度设置
def get_i5_w(data):
    return data['resolution']['iPhone5']['w']

# 获取高度设置
def get_i5_h(data):
    return data['resolution']['iPhone5']['h']

if __name__ == '__main__':
    path = "./test05/"
    path_config = path + "config.json" # 配置路径，配置了iPhone5的分辨率
    path_photos = path + "photos" # 照片路径
    with open(path_config,'r') as f:
        data = json.load(f)

    w = get_i5_w(data)
    h = get_i5_h(data)
    
    # 获取所有图片文件名
    photos = os.listdir(path_photos)
    # 读取每张图片并设置分辨率
    for photo in photos:
        # 生成图片路径
        photo_path = path_photos + "/" + photo
        
        img = Image.open(photo_path)
        img = img.resize((w,h))
        img.save(photo_path)
