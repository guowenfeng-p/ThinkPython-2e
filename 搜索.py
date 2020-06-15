# -*- coding: utf-8 -*-# 
# FileName:搜索.py 
# Author:guowenfeng
# Date:2020/6/11
# Description: 
# 它接受一个 字符并找到该字符所在的索引。如果没有找到该字符，函数返回 -1。-------------------------------------------------------------------------------


def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


if __name__ == '__main__':
    word = 'guowenfeng'
    d = 'e'
    print(find(word, d))
