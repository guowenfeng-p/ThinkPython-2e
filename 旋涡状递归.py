# -*- coding: utf-8 -*-# 
# FileName:旋涡状递归.py 
# Author:guowenfeng
# Date:2020/6/7
# Description: 
# -------------------------------------------------------------------------------


def main(n):
    """
        旋涡状递归实现阶乘
    """
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        recurse = main(n - 1)
        result = n * recurse
        return result


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    main(0)
    print(fibonacci(10))
