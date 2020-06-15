# -*- coding: utf-8 -*-# 
# FileName:元组.py 
# Author:guowenfeng
# Date:2020/6/15
# Description: 
# -------------------------------------------------------------------------------
def printall(*args):
    '''
        汇集形参
    '''
    print(args)


def main():
    """
        主函数
    """
    addr = 'monty@python.org'
    (uname, domain) = addr.split('@')
    print(uname, domain)
    # 汇集形参
    printall(1, 23, 4, 5)


if __name__ == '__main__':
    main()
