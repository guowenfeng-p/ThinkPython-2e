# -*- coding: utf-8 -*-# 
# FileName:字典.py 
# Author:guowenfeng
# Date:2020/6/14
# Description: 
# -------------------------------------------------------------------------------


def histogram(s):
    '''
        计数器集合的实现
    '''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# def histogram2(s):
#     '''
#         使用get方法进行改进
#     '''
#     d = dict()
#     for c in s:
#         d[c] = d.get(c, 0) + 1
#     return d

def reverse_lookup(d, v):
    """
        接受一个值并返回映射到该值的第一个键
    """
    for k in d:
        if d[k] == v:
            return k
    raise LookupError()

def invert_dict(d):
    '''
        #倒转字典
    '''
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

def main():
    """
        主函数
    """
    h = histogram('brontosaurus')
    print(h)
    key = reverse_lookup(h, 2)
    print(key)
    inverse=invert_dict(h)
    print(inverse)
    # h2 = histogram2('brontosaurus')
    # print(h2)


if __name__ == '__main__':
    main()
