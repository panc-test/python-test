"""
闭包：
1、在一个函数（外函数）中定义了另一个函数（内函数）
2、外函数返回值是内函数
3、内函数引用了外函数的自由变量（外部参数，局部变量）


"""


# 一个简单的闭包
def outer(a):  # 外函数

    def inner(b):  # 内函数
        print(a, b)  # 内函数引用了外函数的自由变量

    return inner  # 外函数返回值是内函数


outer(1)(2)
