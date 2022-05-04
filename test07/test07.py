import os
print(os.getcwd())
path = "./test07/codes"

# 统计单个文件的行数
def get_lines_file(path):
    line_sum = 0
    line_empty = 0
    line_notes = 0

    with open(path,"r",encoding="UTF-8") as f:
        line = f.readline()
        #去除首尾空格
        line = line.strip()
        while line:
            #去除首尾空格
            line = line.strip()
            # 总行+1
            line_sum = line_sum + 1
            # 判断是否是空行
            if line == "":
                line_empty = line_empty +1
            # 判断是否是注释行
            elif line.startswith("#"):
                line_notes = line_notes + 1

            line = f.readline()

    return line_sum, line_empty, line_notes

def get_lines(path):
    line_sum = 0
    line_empty = 0
    line_notes = 0

    codes = os.listdir(path)
    # 分别统计每一个文件的行数
    for code in codes:
        code_path = path + "/" + code
        line_sum_file,line_empty_file,line_notes_file =  get_lines_file(code_path)

        line_sum = line_sum + line_sum_file # 总行数
        line_empty = line_empty + line_empty_file # 空行数
        line_notes = line_notes + line_notes_file # 注释行数

    print("路径%s下，共%s行代码，其中空行共%s行，注释共%s行" % (path, line_sum, line_empty, line_notes))

if __name__ == "__main__":
    get_lines(path)