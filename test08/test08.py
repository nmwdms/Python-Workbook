import os

html_path = "./test08/html_test.html" #html文件路径
save_path = "./test08/result.html" #保存的文件路径

if __name__ == "__main__":
    body = ""
    body_flag = False #设置一个标志位，用于识别是否是在body中
    with open(html_path,'r',encoding='UTF-8') as f:
        line = f.readline()
        while line:
            # 如果是body的结尾，标志位置为False
            if line.find("</body>") != -1:
                body_flag = False
                body = body + line
            # 如果标志位为True，说明是body内部
            elif body_flag == True:  
                body = body + line
            # 如果是body的开头，标志置位置为True
            elif line.find("<body") != -1:
                body_flag = True
                body = body + line     
            line = f.readline()
    
    # 保存结果
    with open(save_path,'w',encoding="UTF-8") as f:
        f.write(body)
            
