def Processing_words(filename):
    file1 = open(filename,encoding="utf-8")
    data = file1.read()
#     print(type(data))
#     print(data)
    file1.close()
    data = data.replace("\n", " ").replace("、", " ").replace("  ", " ").replace("，", " ")
#     print(type(data))
#     print(data)
    data = data.split(" ")
    data = data[:-1]
#     print(type(data))
#     print(data)
#     for i in data:
#         print(len(i))
    with open("./语料库/2.txt", "w") as f:
        for i in data:
            if len(i)==4:
                f.write(i)
                f.write("\n")
                f.flush()
            else:
                pass

Processing_words("./语料库/1.txt")

########################################################################################################################
def get_url(filename):
    file1 = open(filename, encoding="ANSI")
    data = file1.read()
    file1.close()
    data = data.split("\n")
    data = data[:-1]
    print(data)

    url_list = []
    for i in data:
        url = "https://hanyu.baidu.com/zici/s?wd=" + i + "&query=四字词语&srcid=28204&from=kg0"
        url_list.append(url)
    print(url_list)
    return url_list


url_list = get_url("./语料库/2.txt")

########################################################################################################################
import requests
from lxml import etree


def get_mean_and_words(page_url):
    mean = []  # 解释
    similar_words = []  # 近反义词
    words_in_this_page = []  # 同一页的单词
    words = []
    for every in page_url:
        print(every)
        res = requests.get(every)
        #         res.encoding = 'gbk'
        #         print(res.text)
        res_xpath = etree.HTML(res.text)
        print(res_xpath)
        mean_1 = res_xpath.xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/dl/dd/p/text()')  # 解释

        count = 0
        for i in mean_1:
            i = i.replace(" ", "").replace("\n", "").replace("\n                    ", "").replace(
                "\n                                    ", "").replace("                ", "")
            mean_1[count] = i
            count += 1
        print("=======")
        print(mean_1)
        mean.append(mean_1)

        similar1 = res_xpath.xpath('/html/body/div[3]/div/div[2]/div[2]/div[9]/div/div/div/a/text()')  # 近反义词
        similar_words.append(similar1)
        print(similar1)
        for i in similar1:
            if len(i) == 4:
                words.append(i)

        jielong_word1 = res_xpath.xpath('/html/body/div[3]/div/div[2]/div[2]/div[11]/div[1]/a/text()')
        print("=======")
        print(jielong_word1)
        words_in_this_page.append(jielong_word1)
        for i in jielong_word1:
            if len(i) == 4:
                words.append(i)

    return mean, words


mean, words = get_mean_and_words(url_list)

########################################################################################################################
def get_url(filename, mean):
    file1 = open(filename, encoding="ANSI")
    data = file1.read()
    file1.close()
    data = data.split("\n")
    words = data[:-1]

    import jieba
    count = 0
    file = open("./语料库/3.txt", "w")
    for i in mean:
        one_line = ""
        one_line = words[count] + " "
        for j in i:
            j = jieba.cut(j, cut_all=True)
            #             print(j)
            for k in j:
                one_line = one_line + k + " "
        #             print(j)
        print(one_line)
        file.write(one_line)
        file.write("\n")
        file.flush()
        count += 1
    file.close()


url_list = get_url("./语料库/2.txt", mean)
print(len(mean))

########################################################################################################################
def get_url_2(words):
    url_list = []
    for i in words:
        url = "https://hanyu.baidu.com/zici/s?wd="+i+"&query=四字词语&srcid=28204&from=kg0"
        url_list.append(url)
    print(url_list)
    return url_list

url_list_2 = get_url_2(words)

########################################################################################################################
def get_mean(page_url, words):
    import jieba
    mean = []  # 解释
    words_ = []

    count_num = 0
    for every in words:
        every = "https://hanyu.baidu.com/zici/s?wd=" + every + "&query=四字词语&srcid=28204&from=kg0"
        try:
            print(every)
            res = requests.get(every)

            res_xpath = etree.HTML(res.text)
            print(res_xpath)
            mean_1 = res_xpath.xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div[1]/dl/dd/p/text()')  # 解释

            count = 0
            qiehao = words[count_num] + " "
            for i in mean_1:
                i = i.replace(" ", "").replace("\n", "").replace("\n                    ", "").replace(
                    "\n                                    ", "").replace("                ", "")
                mean_1[count] = i
                q = list(jieba.cut(i, cut_all=True))
                for j in q:
                    qiehao = qiehao + j + " "

                count += 1
            count = 0
            mean.append(mean_1)
            words_.append(words[count_num])
            print(words[count_num])
            print(mean_1)
            print(qiehao)
            file = open("./语料库/4.txt", "a", encoding="utf-8")
            file.write(qiehao)
            file.write("\n")
            file.flush()
            file.close()
            count_num += 1

            print("=======================================")
        except:
            print("该词无法访问，已去除该词")

    return mean, words_


mean2, words = get_mean(url_list_2, words)