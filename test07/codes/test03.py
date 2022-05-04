import redis
# 读取文件中的激活码
with open("./test03/code_list.txt",'r') as f:
    code_list = []
    line = f.readline()
    while line:
        line_content = line.split(',')
        id = line_content[0]
        code = line_content[1].split('\n')[0]
        code_list.append({id:code})
        line = f.readline()

#保存到Redis中
#需在本地启动redis服务端
r = redis.StrictRedis(host='localhost',port=6379,db=0)
for codes in code_list:
    for id, code in codes.items(): 
        r.hset('code_list',id,code)