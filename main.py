"""
Practice: Python-100-Days/Day01-15/07.字符串和常用数据结构.md
Topic: 练习2：设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。

"""
import random


def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def gencode(m=4):
    array = []  # initial array
    res_array = []
    lower_boundary = ord("A")  # Get ASCII code
    upper_boundary = ord("z")
    for i in range(lower_boundary, upper_boundary + 1):
        array += chr(i)  # transfer ASCII to character
    # print(array)
    for j in range(0, 10):
        array += [j]
    for i in range(m):
        temp = random.randint(0, len(array) - 1)  # give random number which is the position of the array
        res_array += [array[temp]]

    return res_array


def max2array(array=None):
    if array is None:
        array = []  # initial function

    k = 0
    for i in range(len(array)):
        if k < array[i]:
            k = array[i]
    return k

import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    """
    #D7_P2
    x = gencode()
    print("The result:")
    print(x)

    #D7_P3
    w = get_suffix('README.txt')
    print(w)

    # D7_P4
    arr = [];
    for i in range(4):
        arr += [random.random()]
    maxnum = max2array(arr)
    print(arr)
    print(maxnum)

    # D7_L2
    Pos = []
    for i in range(1, 31):
        Pos += [i]

    count = 0
    i = 0
    j = 0
    while count < 15:
        if Pos[j] != 0:
            i += 1
            if i % 9 == 0:
                Pos[j] = 0
                count += 1
                print("Pos = ", Pos)
        j += 1
        j = j % 30

    """




if __name__ == '__main__':
    main()
