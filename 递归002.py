# 创建递归函数1
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n - 1)


# 创建递归函数2
def print_n(s, n):
    if n <= 0:
        # 满足条件后跳出函数
        return
    print(s)
    print_n(s, n - 1)


# 调用函数1
# countdown(3)

# 调用函数2、
s = "哈哈哈"
n = 5
print_n(s, n)
