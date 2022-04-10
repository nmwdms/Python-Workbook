import pymysql
# 读取文件中的激活码
with open("./Python-Workbook/test02/code_list.txt",'r') as f:
    code_list = []
    line = f.readline()
    while line:
        line_content = line.split(',')
        id = line_content[0]
        code = line_content[1].split('\n')[0]
        code_list.append({id:code})
        line = f.readline()

#保存到MySQL中
#前提是已经在MySQL中创建了对应的表结构
db = pymysql.connect(host='localhost',user='root',password='1234',database='test02')
cursor = db.cursor()
cursor.execute("select VERSION()")
for codes in code_list:
    for id, code in codes.items(): 
        print("将第%s个激活码:%s插入" % (id,code))
        sql = "insert into code(id,code) values('%s','%s')" % (id,code) #要执行的sql语句
        try:
            cursor.execute(sql)
            db.commit() # 提交到数据库执行
        except Exception as e:
            db.rollback() # 发生错误时回滚
            print(e)
db.close()
