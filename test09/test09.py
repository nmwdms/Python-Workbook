import os

html_path = "./test09/html_test.html" #html文件路径
save_path = "./test09/result.html" #保存的文件路径

if __name__ == "__main__":
    link = ""
    link_flag = False #设置一个标志位，用于识别是否是在link中
    with open(html_path,'r',encoding='UTF-8') as f:
        line = f.readline()
        while line:
            if link_flag == True:
                # 如果是link的结尾，标志位置为False
                if line.find("</a>") != -1:
                    link_flag = False
                    link = link + line
                # 如果标志位为True，说明是link内部
                else:
                    link = link + line
                # 如果是link的开头，标志置位置为True
            elif line.find("<a") != -1: 
                link_flag = True
                link = link + line
                if line.find("</a>") != -1:
                    link_flag = False      
            line = f.readline()
    
    # 保存结果
    with open(save_path,'w',encoding="UTF-8") as f:
        f.write(link)