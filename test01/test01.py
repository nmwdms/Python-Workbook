import random

num = 200 #要生成的激活码个数
code_list = [] # 保存激活码的列表
# 生成激活码并保存
for i in range(num):
    code = "0000"
    # 如果有重复的激活码，则重新生成
    while code in code_list or code == "0000":
        code_int = random.randint(1,9999) # 从1~9999中生成一个激活码
        code = str(code_int) #将int类型的激活码转为str类型
        codelist = list(code) 
    # 判断激活码长度是否为4，小于4则在左侧补0
    while len(codelist) != 4:
        codelist.insert(0,"0")
    code = "".join(codelist)
    # 保存激活码
    code_list.append({str(i+1):code})
print("激活码个数：",len(code_list))
print("激活码：\n",code_list)

# 保存激活码到文件code_list.txt中
with open("./Python-Workbook/test01/code_list.txt",'w') as f:
    for i in range(len(code_list)):
        for id, code in code_list[i].items():
            f.write(id + "," + code + "\r")