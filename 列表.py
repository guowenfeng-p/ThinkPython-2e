# -*- coding: utf-8 -*-# 
# FileName:列表.py 
# Author:guowenfeng
# Date:2020/6/14
# Description: 
# -------------------------------------------------------------------------------


def main():
    """
        主函数
    """
    t = ['a', 'A', 'V', 'b']

    res=capitalize_all(t)
    print(res)


# capitalize方法将字符串第一个字母变成大写，其他字母变成小写

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


if __name__ == '__main__':
    main()
