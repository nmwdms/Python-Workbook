word_num_dict = {} # 存储结果的字典
with open("./test04/book.txt",'r') as f:
    line = f.readline()
    while line:
        # 对当前行通过空格进行分割
        words_line = line.split(" ")
        for word in words_line:
            if word in word_num_dict:
                word_num_dict[word] = word_num_dict[word] + 1
            else:
                word_num_dict[word] = 1
        line = f.readline()
print(word_num_dict)