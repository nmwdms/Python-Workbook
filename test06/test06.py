import os

path = "./test06/diarys"

# 获取最重要的词，返回该词和它的出现次数
def get_important_word(diary):
    word_num_dict = {} # 存储结果的字典
    max = 0
    max_word = ""

    with open(diary,'r', encoding='UTF-8') as f:
        line = f.readline()
        while line:
            words_line = line.split(" ")
            for word in words_line:
                if word in word_num_dict:
                    word_num_dict[word] = word_num_dict[word] + 1
                    if word_num_dict[word] > max and word != '':
                        max = word_num_dict[word]
                        max_word = word
                else:
                    word_num_dict[word] = 1
                    if max < 1 and word != '':
                        max = 1
                        max_word = word            
            line = f.readline()
    return max,max_word

if __name__ == '__main__':
    print(os.getcwd())
    diarys = os.listdir(path)
    for diary in diarys:
        diary_path = path + "/" + diary
        max,max_word = get_important_word(diary_path) #获取最重要的词
        print("日记%s中最重要的词为：%s,出现次数为%s" % (diary,max_word,max))
