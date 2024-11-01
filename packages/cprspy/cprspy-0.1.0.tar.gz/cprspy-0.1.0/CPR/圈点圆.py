import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append('./圈点圆.py')

'''this is a circle source
这是圈的注释
'''
# 基础工具(Basic_Tools)

'''
圈(圆s)
'''


def 圆(圆心, 半径, 颜色='b'):
    角 = np.linspace(0, 2*np.pi, 1000)
    x = 圆心[0] + 半径 * np.cos(角)
    y = 圆心[1] + 半径 * np.sin(角)
    plt.axis('equal')
    plt.plot(x, y, color=颜色)


def 圆_p(圆心, 点, 颜色='b'):
    # 计算圆的半径
    半径 = np.sqrt((点[0] - 圆心[0])
                 ** 2 + (点[1] - 圆心[1]) ** 2)
    # 生成圆上的点
    旋转角 = np.linspace(0, 2 * np.pi, 100)
    x = 圆心[0] + 半径 * np.cos(旋转角)
    y = 圆心[1] + 半径 * np.sin(旋转角)
    # 绘制图形
    plt.axis('equal')
    plt.plot(x, y, color=颜色)

# 同心圆
# 等差
# 双向


def 同心圆s(圆心, n, d, 半径, 颜色='b'):
    plt.plot(圆心[0], 圆心[1], marker='o', color=颜色)
    for i in range(n):
        圆(圆心, 半径-i*d, 颜色)
        圆(圆心, 半径+i*d, 颜色)
    圆(圆心, 半径, 颜色)

# 向外


def 同心圆s_向外(圆心, n, d, 半径, 颜色='b'):
    plt.plot(圆心[0], 圆心[1], marker='o', color=颜色)
    for i in range(n):
        圆(圆心, 半径+d*i, 颜色)
    圆(圆心, 半径, 颜色)

# 向内


def 同心圆s_向内(圆心, n, d, 半径, 颜色='b'):
    plt.plot(圆心[0], 圆心[1], marker='o', color=颜色)
    for i in range(n):
        圆(圆心, 半径-d*i, 颜色)
    圆(圆心, 半径, 颜色)

# 等比数列
# 双向


def 同心圆s_等比(圆心, n, q, 半径, 颜色='b'):
    plt.plot(圆心[0], 圆心[1], marker='o', color=颜色)
    for i in range(n):
        圆(圆心, 半径/(q**i), 颜色)
        圆(圆心, 半径*(q**i), 颜色)
    圆(圆心, 半径, 颜色)

# 向外


def 同心圆s_等比_向外(圆心, n, q, 半径, 颜色='b'):
    plt.plot(圆心[0], 圆心[1], marker='o', color=颜色)
    for i in range(n):
        圆(圆心, 半径*(q**i), 颜色)
    圆(圆心, 半径, 颜色)

# 向内


def 同心圆s_等比_向内(圆心, n, q, 半径, 颜色='b'):
    plt.plot(圆心[0], 圆心[1], marker='o', color=颜色)
    for i in range(n):
        圆(圆心, 半径/(q**i), 颜色)
    圆(圆心, 半径, 颜色)


'''
波(波s)
'''
# 圈上波

# 等差

# 向外


def 波_圆_等差_向外(振幅, 频率, 相位, 颜色, 旋转角=0, 主半径=1):
    同心圆s_向外((0, 0), 频率, 振幅, 主半径, 'g')
    for i in range(相位+1):
        同心圆s_向外((np.cos(i*2*np.pi/相位+np.pi/2+旋转角),
                np.sin(i*2*np.pi/相位+np.pi/2+旋转角)), 频率, 振幅, 主半径,  颜色)
# 向内


def 波_圆_等差_向内(振幅, 频率, 相位, 颜色, 旋转角=0, 主半径=1):
    同心圆s_向内((0, 0), 频率, 振幅, 主半径, 'g')
    for i in range(相位+1):
        同心圆s_向内((np.cos(i*2*np.pi/相位+np.pi/2+旋转角),
                np.sin(i*2*np.pi/相位+np.pi/2+旋转角)), 频率, 振幅, 主半径,  颜色)

# 双向


def 波_圆_等差(振幅, 频率, 相位, 颜色, 旋转角=0, 主半径=1):
    同心圆s((0, 0), 频率, 振幅, 主半径, 'g')
    for i in range(相位+1):
        同心圆s((np.cos(i*2*np.pi/相位+np.pi/2+旋转角),
              np.sin(i*2*np.pi/相位+np.pi/2+旋转角)), 频率, 振幅, 主半径,  颜色)


# 等比


# 向外
def 波_圆_等比_向外(振幅, 频率, 相位, 颜色, 旋转角=0, 主半径=1):
    同心圆s_等比_向外((0, 0), 频率, np.sqrt(振幅), 主半径, 颜色)
    for i in range(相位+1):
        同心圆s_等比_向外(
            ((np.cos(i*2*np.pi/相位+np.pi/2+旋转角)), np.sin(i*2*np.pi/相位+np.pi/2+旋转角)), 频率, np.sqrt(振幅), 主半径, 颜色)


# 向内
def 波_圆_等比_向内(振幅, 频率, 相位, 颜色, 旋转角=0, 主半径=1):
    同心圆s_等比_向内((0, 0), 频率, np.sqrt(振幅), 主半径, 颜色)
    for i in range(相位+1):
        同心圆s_等比_向内(
            ((np.cos(i*2*np.pi/相位+np.pi/2+旋转角)), np.sin(i*2*np.pi/相位+np.pi/2+旋转角)), 频率, np.sqrt(振幅), 主半径, 颜色)
# 双向


def 波_圆_等比(振幅, 频率, 相位, 颜色, 旋转角=0, 主半径=1):
    同心圆s_等比((0, 0), 频率, np.sqrt(振幅), 主半径, 颜色)
    for i in range(相位+1):
        同心圆s_等比(
            ((np.cos(i*2*np.pi/相位+np.pi/2+旋转角)), np.sin(i*2*np.pi/相位+np.pi/2+旋转角)), 频率, np.sqrt(振幅), 主半径, 颜色)


'''弧(弧s)
'''
""""""
# 从点1到点2的圆弧
""""""

# 顺时针


def 弧(圆心, 点1, 点2, 颜色='b'):
    # 计算端点到圆心的向量
    vector1 = np.array(点1) - np.array(圆心)
    vector2 = np.array(点2) - np.array(圆心)

    # 计算向量的模长
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # 计算向量之间的夹角
    旋转角1 = np.arctan2(vector1[1], vector1[0])
    旋转角2 = np.arctan2(vector2[1], vector2[0])

    # 确保 旋转角2 > 旋转角1
    if 旋转角1 < 旋转角2:
        旋转角1 += 2 * np.pi

    # 计算圆弧上的点
    t = np.linspace(旋转角1, 旋转角2, 100)
    x = 圆心[0] + r1 * np.cos(t)
    y = 圆心[1] + r1 * np.sin(t)

    # X,Y轴等长
    plt.axis('equal')

    # 绘制圆弧
    plt.plot(x, y, color=颜色)

# 逆时针


def 弧_反(圆心, 点1, 点2, 颜色='b'):
    # 计算端点到圆心的向量
    vector1 = np.array(点1) - np.array(圆心)
    vector2 = np.array(点2) - np.array(圆心)

    # 计算向量的模长
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # 计算向量之间的夹角
    旋转角1 = np.arctan2(vector1[1], vector1[0])
    旋转角2 = np.arctan2(vector2[1], vector2[0])

    # 确保 旋转角2 > 旋转角1
    if 旋转角2 < 旋转角1:
        旋转角2 += 2 * np.pi

    # 计算圆弧上的点
    t = np.linspace(旋转角1, 旋转角2, 100)
    x = 圆心[0] + r1 * np.cos(t)
    y = 圆心[1] + r1 * np.sin(t)

    # X,Y轴等长
    plt.axis('equal')
    # 绘制圆弧
    plt.plot(x, y, color=颜色)


"""通过角度画圆弧
"""


def 弧_角度(圆心, 半径, 角1, 角2, 颜色='b'):
    if 角1 < 角2:
        角 = np.linspace(角1, 角2, 1000)
        x = 圆心[0] + 半径 * np.cos(角)
        y = 圆心[1] + 半径 * np.sin(角)
        plt.axis('equal')
        plt.plot(x, y, color=颜色)


def 弧_角度_反(圆心, 半径, 角1, 角2, 颜色='b'):
    角 = np.linspace(角2-2*np.pi, 角1, 1000)
    x = 圆心[0] + 半径 * np.cos(角)
    y = 圆心[1] + 半径 * np.sin(角)
    plt.axis('equal')
    plt.plot(x, y, color=颜色)


"""通过角度画圆弧
"""


def 花_弧_角度(圆心, 半径, 角1, 角2, 颜色='b'):
    if 角1 < 角2:
        角 = np.linspace(角1, 角2, 1000)
        x = 圆心[0] + 半径 * np.cos(角)
        y = 圆心[1] + 半径 * np.sin(角)
        plt.axis('equal')
        plt.plot(x, y, color=颜色)


def 花_弧_角度_反(圆心, 半径, 角1, 角2, 颜色='b'):
    角 = np.linspace(角2-2*np.pi, 角1, 1000)
    x = 圆心[0] + 半径 * np.cos(角)
    y = 圆心[1] + 半径 * np.sin(角)
    plt.axis('equal')
    plt.plot(x, y, color=颜色)


'''带填充的弧(弧s With Fills)
'''
# 顺时针


def 弧_点(圆心, 点1, 点2):
    # 计算端点到圆心的向量
    vector1 = np.array(点1) - np.array(圆心)
    vector2 = np.array(点2) - np.array(圆心)

    # 计算向量的模长
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # 计算向量之间的夹角
    旋转角1 = np.arctan2(vector1[1], vector1[0])
    旋转角2 = np.arctan2(vector2[1], vector2[0])

    # 确保 旋转角2 > 旋转角1
    if 旋转角1 < 旋转角2:
        旋转角1 += 2 * np.pi

    # 计算圆弧上的点
    t = np.linspace(旋转角1, 旋转角2, 100)
    x = 圆心[0] + r1 * np.cos(t)
    y = 圆心[1] + r1 * np.sin(t)

    return [x, y]

# 逆时针


def 弧_反_点(圆心, 点1, 点2):
    # 计算端点到圆心的向量
    vector1 = np.array(点1) - np.array(圆心)
    vector2 = np.array(点2) - np.array(圆心)

    # 计算向量的模长
    r1 = np.linalg.norm(vector1)
    r2 = np.linalg.norm(vector2)

    # 计算向量之间的夹角
    旋转角1 = np.arctan2(vector1[1], vector1[0])
    旋转角2 = np.arctan2(vector2[1], vector2[0])

    # 确保 旋转角2 > 旋转角1
    if 旋转角2 < 旋转角1:
        旋转角2 += 2 * np.pi

    # 计算圆弧上的点
    t = np.linspace(旋转角1, 旋转角2, 100)
    x = 圆心[0] + r1 * np.cos(t)
    y = 圆心[1] + r1 * np.sin(t)

    return [x, y]


"""通过角度画圆弧
"""


def 弧_角度_p(圆心, 半径, 角1, 角2):
    if 角1 < 角2:
        角 = np.linspace(角1, 角2, 1000)
        x = 圆心[0] + 半径 * np.cos(角)
        y = 圆心[1] + 半径 * np.sin(角)
    return [x, y]


def 弧_角度_p_反(圆心, 半径, 角1, 角2):
    角 = np.linspace(角2-2*np.pi, 角1, 1000)
    x = 圆心[0] + 半径 * np.cos(角)
    y = 圆心[1] + 半径 * np.sin(角)
    return [x, y]


'''
画花算法(花 Drawing Algorithm)
'''

"""_summary_: 画空心花(Draw Hollow 花s)
"""
# 花瓣


def n_花_花瓣(圆心, 主半径, r, n, 旋转角=0, 颜色='b'):
    alpha = 2*np.pi/n
    a = 主半径*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    旋转角_弧 = np.pi/2-np.pi/n+np.arccos((a)/r)
    旋转角_花瓣 = 2*旋转角_弧
    # 圆((0, 0), 主半径, 'g')
    # 圆((0, 0), 主半径/2, 'g')
    圆心1 = (np.cos(旋转角+alpha/2)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2)*主半径+圆心[1])
    圆心2 = (np.cos(旋转角+alpha/2-2*np.pi/n)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2-2*np.pi/n)*主半径+圆心[1])
    if abs(r - a) < 1e-12:
        花_弧_角度(圆心1, r, np.pi+alpha/2+旋转角,
               np.pi+alpha/2+旋转角+旋转角_弧, 颜色)
        花_弧_角度(圆心2, r, np.pi/2+旋转角,
               np.pi/2+旋转角+旋转角_弧, 颜色)
        # if r == 主半径:
        #     print("r=", r, ",a=", a)
        #     print('r=a,r=主半径形成睡莲花瓣。')
        # elif r > 主半径:
        #     print("r=", r, ",a=", a)
        #     print('r=a,r>主半径形成荷花花瓣。')
        # elif r < 主半径:
        #     print("r=", r, ",a=", a)
        #     print('r=a,r<主半径形成特殊曼陀罗花瓣。')
    elif r > a:
        花_弧_角度(圆心1, r, np.pi+alpha/2+旋转角,
               np.pi+alpha/2+旋转角+旋转角_弧, 颜色)
        花_弧_角度(圆心2, r, np.pi/2-beta+旋转角,
               np.pi/2-beta+旋转角+旋转角_弧, 颜色)
        # if r == 主半径:
        #     print("r=", r, ",a=", a)
        #     print('r>a,r=主半径形成睡莲花瓣。')
        # elif r > 主半径:
        #     print("r=", r, ",a=", a)
        #     print('r>a,r>主半径形成荷花花瓣。')
        # elif r < 主半colcolcolor
        #     print("r=", r, ",a=", a)
        #     print('r>a,r<主半径形成普通曼陀罗花瓣。')
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(圆心1[0], 圆心1[1], marker='o', color='r')
    # plt.plot(圆心2[0], 圆心2[1], marker='o', color='b')
# 花弧


def n_花_弧(圆心, 主半径, r, n, 旋转角=0, 颜色='b'):
    alpha = 2*np.pi/n
    a = 主半径*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    旋转角_弧 = np.pi/2-np.pi/n+np.arccos((a)/r)
    旋转角_花瓣 = 2*旋转角_弧
    # 圆((0, 0), 主半径, 'g')
    # 圆((0, 0), 主半径/2, 'g')
    圆心1 = (np.cos(旋转角+alpha/2)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2)*主半径+圆心[1])
    圆心2 = (np.cos(旋转角+alpha/2-2*np.pi/n)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2-2*np.pi/n)*主半径+圆心[1])
    if abs(r - a) < 1e-12:
        花_弧_角度(圆心1, r, np.pi/2+alpha+旋转角,
               np.pi/2+alpha+旋转角+旋转角_花瓣, 颜色)
        花_弧_角度(圆心2, r, np.pi/2+旋转角,
               np.pi/2+旋转角+旋转角_花瓣, 颜色)
        if r == 主半径:
            print("r=", r, ",a=", a)
            print('r=a,r=主半径形成睡莲花弧。')
        elif r > 主半径:
            print("r=", r, ",a=", a)
            print('r=a,r>主半径形成荷花花弧。')
        elif r < 主半径:
            print("r=", r, ",a=", a)
            print('r=a,r<主半径形成特殊曼陀罗花弧。')
    elif r > a:
        花_弧_角度(圆心1, r, np.pi/2+alpha-beta+旋转角,
               np.pi/2+alpha-beta+旋转角+旋转角_花瓣, 颜色)
        花_弧_角度(圆心2, r, np.pi/2-beta+旋转角,
               np.pi/2-beta+旋转角+旋转角_花瓣, 颜色)
        if r == 主半径:
            print("r=", r, ",a=", a)
            print('r>a,r=主半径形成睡莲花弧。')
        elif r > 主半径:
            print("r=", r, ",a=", a)
            print('r>a,r>主半径形成荷花花弧。')
        elif r < 主半径:
            print("r=", r, ",a=", a)
            print('r>a,r<主半径形成普通曼陀罗花弧。')
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(圆心1[0], 圆心1[1], marker='o', colcolcolor='r')
    # plt.plot(圆心2[0], 圆心2[1], marker='o', colcolcolor='b')

# 带场花弧


def n_花s_花_弧_带_场(圆心, 主半径, r, n, 旋转角=0, 颜色='b', 颜色场='#ff0'):
    alpha = 2*np.pi/n
    a = 主半径*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    旋转角_弧 = np.pi/2-np.pi/n+np.arccos((a)/r)
    旋转角_花瓣 = 2*旋转角_弧
    # 圆((0, 0), 主半径, 'g')
    # 圆((0, 0), 主半径/2, 'g')
    圆心1 = (np.cos(旋转角+alpha/2)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2)*主半径+圆心[1])
    圆心2 = (np.cos(旋转角+alpha/2-2*np.pi/n)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2-2*np.pi/n)*主半径+圆心[1])
    if abs(r - a) < 1e-12:
        花_弧_角度(圆心1, r, np.pi/2+alpha+旋转角,
               np.pi/2+alpha+旋转角+旋转角_花瓣, 颜色)
        花_弧_角度_反(圆心1, r, np.pi/2+alpha+旋转角,
                 np.pi/2+alpha+旋转角+旋转角_花瓣, 颜色场)
        花_弧_角度(圆心2, r, np.pi/2+旋转角,
               np.pi/2+旋转角+旋转角_花瓣, 颜色)
        花_弧_角度_反(圆心2, r, np.pi/2+旋转角,
                 np.pi/2+旋转角+旋转角_花瓣, 颜色场)
    elif r > a:
        花_弧_角度(圆心1, r, np.pi/2+alpha-beta+旋转角,
               np.pi/2+alpha-beta+旋转角+旋转角_花瓣, 颜色)
        花_弧_角度_反(圆心1, r, np.pi/2+alpha-beta+旋转角,
                 np.pi/2+alpha-beta+旋转角+旋转角_花瓣, 颜色场)
        花_弧_角度(圆心2, r, np.pi/2-beta+旋转角,
               np.pi/2-beta+旋转角+旋转角_花瓣, 颜色)
        花_弧_角度_反(圆心2, r, np.pi/2-beta+旋转角,
                 np.pi/2-beta+旋转角+旋转角_花瓣, 颜色场)
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(圆心1[0], 圆心1[1], marker='o', colcolcolor='r')
    # plt.plot(圆心2[0], 圆心2[1], marker='o', colcolcolor='b')

# 一朵向上花瓣


def one_花_花瓣(圆心, 主半径, r, n, 旋转角=0, 颜色='b'):
    n_花_花瓣(圆心, 主半径, r, n, 旋转角+np.pi/2, 颜色)

# 一朵向上花弧


def one_花_弧(圆心, 主半径, r, n, 旋转角=0, 颜色='b'):
    n_花_弧(圆心, 主半径, r, n, 旋转角+np.pi/2, 颜色)

# 一朵向上花瓣场


def one_花_花_弧_带_场(圆心, 主半径, r, n, 旋转角=0, 颜色='b', 颜色场='#ff0'):
    n_花s_花_弧_带_场(圆心, 主半径, r, n, 旋转角 +
                 np.pi/2, 颜色, 颜色场)

# 花瓣形成的单层花


def 花s_花_by_花瓣(圆心, 主半径, r, N, n, 旋转角, 颜色='b'):
    for i in range(0, N):
        one_花_花瓣(圆心, 主半径, r, n, 2*i*np.pi/N+旋转角, 颜色)


# 花弧形成的单层花


def 花s_花_by_弧(圆心, 主半径, r, N, n, 旋转角, 颜色='b'):
    for i in range(0, N):
        one_花_弧(圆心, 主半径, r, n, 2*i*np.pi/N+旋转角, 颜色)

# 单层花带场


def 花s_花_by_花_弧_带_场(圆心, 主半径, r, N, n, 旋转角, 颜色='b', 颜色场='#ff0'):
    for i in range(0, N):
        one_花_花_弧_带_场(
            圆心, 主半径, r, n, 2*i*np.pi/N+旋转角, 颜色)

# 花瓣形成的多层花


def 花s_花_by_花瓣_多重(圆心, 主半径, r, n, ratio, M, N, 旋转角, 颜色='b'):
    for j in range(1, M+1):
        for i in range(0, N):
            one_花_花瓣(圆心, 主半径*(ratio**(j-1)), r*(ratio**(j-1)),
                     n, 2*i*np.pi/N+(j-1)*np.pi/N+旋转角, 颜色)


"""_summary_: 画带上色花(Draw 颜色ed 花s)
"""
########################
########################
########################
########################
########################
########################
########################
########################


# def one弧_莲花_n(圆心, r, n, 旋转角, 颜色='b'):
#     # (n-2)/n个圆弧
#     弧_角度(圆心, r, 旋转角, 旋转角+2*np.pi*(n-2)/n,颜色)


# def one弧_莲花_n_反(圆心, r, n, 旋转角, 颜色='b'):
#     # (n-2)/n个圆弧
#     弧_角度_反(圆心, r, 旋转角, 旋转角+2*np.pi*(n-2)/n,颜色)


def n_莲花_花瓣_填充(圆心, r, n, 旋转角, 颜色f='b', 颜色='r', alpha=0.1):
    alpha = np.pi/n
    beta = np.pi-np.pi/n
    圆心1 = (np.cos(旋转角+alpha)*r +
           圆心[0], np.sin(旋转角+alpha)*r+圆心[1])
    圆心2 = (np.cos(旋转角+alpha-2*np.pi/n)*r +
           圆心[0], np.sin(旋转角+alpha-2*np.pi/n)*r+圆心[1])
    # 圆心
    # plt.plot(圆心1[0], 圆心1[1], marker='o', colcolcolor='r')
    # plt.plot(圆心2[0], 圆心2[1], marker='o', colcolcolor='b')
    弧 = 弧_角度_p(圆心1, r, alpha+np.pi+旋转角,
               alpha+np.pi+旋转角+np.pi*(n-2)/n)
    弧_反 = 弧_角度_p_反(圆心2, r, beta+旋转角,
                   beta+旋转角+np.pi*(n+2)/n)
    x = 弧[0]
    y = 弧[1]
    x1 = 弧_反[0]
    y1 = 弧_反[1]
    # X,Y轴等长
    plt.axis('equal')
    plt.fill(x, y, 颜色f)
    plt.fill(x1, y1, 颜色f)
    plt.plot(x, y, 颜色, alpha)
    plt.plot(x1, y1, 颜色, alpha)


def n_花s_花瓣_填充(圆心, 主半径, r, n, 旋转角=0, 颜色f='b', 颜色='r', alpha=0.1):
    alpha = 2*np.pi/n
    a = 主半径*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    旋转角_弧 = np.pi/2-np.pi/n+np.arccos((a)/r)
    旋转角_花瓣 = 2*旋转角_弧
    # 圆((0, 0), 主半径, 'g')
    # 圆((0, 0), 主半径/2, 'g')
    圆心1 = (np.cos(旋转角+alpha/2)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2)*主半径+圆心[1])
    圆心2 = (np.cos(旋转角+alpha/2-2*np.pi/n)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2-2*np.pi/n)*主半径+圆心[1])
    if abs(r - a) < 1e-12:
        弧 = 弧_角度_p(圆心1, r, np.pi+alpha/2+旋转角,
                   np.pi+alpha/2+旋转角+旋转角_弧)
        弧_反 = 弧_角度_p(圆心2, r, np.pi/2+旋转角,
                     np.pi/2+旋转角+旋转角_弧)
    elif r > a:
        弧 = 弧_角度_p(圆心1, r, np.pi+alpha/2+旋转角,
                   np.pi+alpha/2+旋转角+旋转角_弧)
        弧_反 = 弧_角度_p(圆心2, r, np.pi/2-beta+旋转角,
                     np.pi/2-beta+旋转角+旋转角_弧)
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(圆心1[0], 圆心1[1], marker='o', colcolcolor='r')
    # plt.plot(圆心2[0], 圆心2[1], marker='o', colcolcolor='b')
    x1 = 弧[0]
    y1 = 弧[1]
    x2 = 弧_反[0]
    y2 = 弧_反[1]
    merged_x = np.concatenate((x1, x2))
    merged_y = np.concatenate((y1, y2))
    plt.axis('equal')

    plt.fill(merged_x, merged_y, 颜色f)
    # plt.fill(x1, y1, 颜色f)
    # plt.fill(x2, y2, 颜色f)
    plt.plot(x1, y1, 颜色, alpha)
    plt.plot(x2, y2, 颜色, alpha)

# 带填充的花瓣形成的花


def one_花瓣_填充(圆心, r, n, 旋转角, 颜色f='r', 颜色='b'):
    n_莲花_花瓣_填充(圆心, r, n, 旋转角+np.pi/2, 颜色f, 颜色)


def one_layer_花_by_花瓣_填充(圆心, 主半径, n, 旋转角, 颜色f='r', 颜色='b'):
    for i in range(0, n):
        one_花瓣_填充(圆心, 主半径, n, 2 * i * np.pi /
                  n + 旋转角, 颜色f, 颜色)


# one_layer_花_by_花瓣_fill((0, 0), 1, 1, 0, '#0f0', 'b')


def 花_by_花瓣_填充(圆心, r, M, N, n, 旋转角, 颜色f='r', 颜色='b'):
    for j in range(1, M+1):
        for i in range(0, N):
            one_花瓣_填充(圆心, (np.sqrt(2*np.cos(np.pi/n))**(2*j-1)*r),
                      n, 2*i*np.pi/N+(j-1)*np.pi/N+旋转角, 颜色f, 颜色)

# 一朵向上花瓣带填充


def one_花_花瓣_填充(圆心, 主半径, r, n, 旋转角=0, 颜色f='r', 颜色='b', alpha=0.5):
    n_花s_花瓣_填充(圆心, 主半径, r, n, 旋转角+np.pi/2, 颜色f, 颜色, alpha)

# 花瓣形成的单层花带填充


def 花s_花_by_花瓣_填充(圆心, 主半径, r, N, n, 旋转角, 颜色f='r', 颜色='b', alpha=0.5):
    for i in range(0, N):
        one_花_花瓣_填充(圆心, 主半径, r, n, 2*i *
                    np.pi/N+旋转角, 颜色f, 颜色, alpha)

# 花弧


def n_花s_弧_p(圆心, 主半径, r, n, 旋转角=0):
    alpha = 2*np.pi/n
    a = 主半径*np.sin(np.pi/n)
    beta = np.arccos((a)/r)
    旋转角_弧 = np.pi/2-np.pi/n+np.arccos((a)/r)
    旋转角_花瓣 = 2*旋转角_弧
    # 圆((0, 0), 主半径, 'g')
    # 圆((0, 0), 主半径/2, 'g')
    圆心1 = (np.cos(旋转角+alpha/2)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2)*主半径+圆心[1])
    圆心2 = (np.cos(旋转角+alpha/2-2*np.pi/n)*主半径 +
           圆心[0], np.sin(旋转角+alpha/2-2*np.pi/n)*主半径+圆心[1])
    if abs(r - a) < 1e-12:
        弧 = 弧_角度_p(圆心1, r, np.pi/2+alpha+旋转角,
                   np.pi/2+alpha+旋转角+旋转角_花瓣)
        弧_反 = 弧_角度_p(圆心2, r, np.pi/2+旋转角,
                     np.pi/2+旋转角+旋转角_花瓣)
    elif r > a:
        弧 = 弧_角度_p(圆心1, r, np.pi/2+alpha-beta+旋转角,
                   np.pi/2+alpha-beta+旋转角+旋转角_花瓣)
        弧_反 = 弧_角度_p(圆心2, r, np.pi/2-beta+旋转角,
                     np.pi/2-beta+旋转角+旋转角_花瓣)
    elif r < a:
        print("r=", r, ",a=", a)
        print('r<a,不能形成花瓣。')
    # plt.plot(圆心1[0], 圆心1[1], marker='o', colcolcolor='r')
    # plt.plot(圆心2[0], 圆心2[1], marker='o', colcolcolor='b')
    x1 = 弧[0]
    y1 = 弧[1]
    x2 = 弧_反[0]
    y2 = 弧_反[1]
    merged_x = np.concatenate((x1, x2))
    merged_y = np.concatenate((y1, y2))
    # plt.fill(merged_x, merged_y, colcolcolorf)
    # # plt.fill(x1, y1, colcolcolorf)
    # # plt.fill(x2, y2, colcolcolorf)
    # plt.plot(x1, y1, colcolcolor, alpha)
    # plt.plot(x2, y2, colcolcolor, alpha)
    # plt.axis('equal')
    return [merged_x, merged_y]
############################################################
# 一朵向上花弧


# def one_花s_弧_p(圆心, 主半径, r, n, 旋转角=0):
#     点s = n_花s_弧_p(圆心, 主半径, r, n, 旋转角+np.pi/2)
#     return 点s
# # 花弧形成的单层花


# def 花s_花_by_弧_p(圆心, 主半径, r, N, n, 旋转角):
#     点s = [0, 0]
#     for i in range(0, N):
#         点s[0] += one_花s_弧_p(圆心, 主半径, r, n, 2*i*np.pi/N+旋转角)[0]
#         点s[1] += one_花s_弧_p(圆心, 主半径, r, n, 2*i*np.pi/N+旋转角)[1]
#     return [点s[0], 点s[1]]


# def n_花s_弧_fill(圆心, 主半径, r, n, N, 旋转角=0, 颜色f='b', 颜色='r', alpha=0.1):
#     点s = 花s_花_by_弧_p(圆心, 主半径, r, N, n, 旋转角)
#     # print(点s)
#     plt.fill(点s[0], 点s[1], 颜色f)
#     # plt.fill(x1, y1, 颜色f)
#     # plt.fill(x2, y2, 颜色f)
#     plt.plot(点s[0], 点s[1], colcolcolor, alpha)
#     plt.scatter(点s[0][0], 点s[1][0], s=1, 颜色='r')
#     plt.axis('equal')
############################################################


"""
罗丹线圈注释
this is a rose curve 源
"""


def 罗丹线圈(主半径, r, n, 颜色='b', 旋转角=0):
    for i in range(0, n):
        圆((主半径*np.cos(i*2*np.pi/n+旋转角), 主半径 *
           np.sin(i*2*np.pi/n+旋转角)), r, 颜色)


def 罗丹线圈_彩色(主半径, r, n, 颜色s, 旋转角=0):
    for i in range(0, n):
        圆((主半径*np.cos(i*2*np.pi/n+旋转角), 主半径 *
           np.sin(i*2*np.pi/n+旋转角)), r, 颜色s[i])


"""
螺旋线注释
this is a 螺旋 源
"""


def log螺旋(n, a, b, cyc, 颜色='b', 旋转角=0):
    t = np.linspace(-cyc * 2 * np.pi, cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+旋转角)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+旋转角)
    plt.plot(x, y, color=颜色)
    # plt.axis('equal')


def log螺旋_向外(n, a, b, cyc, 颜色='b', 旋转角=0):
    t = np.linspace(0, cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+旋转角)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+旋转角)
    plt.plot(x, y, color=颜色)


def log螺旋_向内(n, a, b, cyc, 颜色='b', 旋转角=0):
    t = np.linspace(0, -cyc * 2 * np.pi, 100)
    x = a*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.cos(t+旋转角)
    y = b*(np.cos(np.pi/n)) ** (-n*t / np.pi) * np.sin(t+旋转角)
    plt.plot(x, y, color=颜色)


def n_螺旋(n, cyc, 颜色, 旋转角=0):
    for i in range(n):
        log螺旋(n, 1, 1, cyc, 颜色, 旋转角+i*2*np.pi/n)
        log螺旋(n, -1, 1, cyc, 颜色, 旋转角+i*2*np.pi/n)


def n_螺旋_旋转(n, cyc, 颜色, alpha=0, 旋转角=0):
    for i in range(n):
        log螺旋(n, 1, 1, cyc, 颜色, alpha+旋转角+i*2*np.pi/n)
        log螺旋(n, -1, 1, cyc, 颜色, alpha-旋转角+i*2*np.pi/n)


def n_螺旋_旋转_向外(n, cyc, 颜色, 旋转角=0):
    for i in range(n):
        log螺旋_向外(n, 1, 1, cyc, 颜色, 旋转角+i*2*np.pi/n)
        log螺旋_向外(n, -1, 1, cyc, 颜色, -旋转角+i*2*np.pi/n)


def n_螺旋_旋转_向内(n, cyc, 颜色, 旋转角=0):
    for i in range(n):
        log螺旋_向内(n, 1, 1, cyc, 颜色, 旋转角+i*2*np.pi/n)
        log螺旋_向内(n, -1, 1, cyc, 颜色, -旋转角+i*2*np.pi/n)


def 菊花_花瓣(n, cyc, 旋转角, 颜色='b'):
    log螺旋(n, 1, 1, cyc*1.25, 颜色, 旋转角)
    log螺旋(n, -1, 1, cyc*1.25, 颜色, -旋转角)


def 菊花_by_花瓣(n, cyc, N, 旋转角, 颜色s):
    for i in range(N):
        菊花_花瓣(n, cyc, 旋转角+i*2*np.pi/N, 颜色s[i])


"""
this is a  点 源
这是点的注释
"""
# 生成半径主半径圆上均匀N等分点


def n_点s(N, 主半径, 旋转角=0):
    return [[主半径*np.cos(i*2 * np.pi/N+np.pi/2+旋转角), 主半径*np.sin(i*2 * np.pi/N+np.pi/2+旋转角)] for i in range(N)]

# 画出点


def draw_点s(点s, 颜色p='b', size=100):
    for i in range(len(点s)):
        plt.scatter(点s[i][0], 点s[i][1], s=size, color=颜色p)

# 双向生成点阵


def n_点阵(n, m, 旋转角=0):
    点s = []
    for i in range(m):
        点s += n_点s(n, (np.cos(np.pi/n))**i, i*(np.pi/n+旋转角))
        点s += n_点s(n, (np.cos(np.pi/n))
                   ** (-i), i*(np.pi/n-旋转角))
    return 点s


# 向内生成点阵
def n_点阵_向内(n, m, 旋转角=0):
    点s = []
    for i in range(m):
        点s += n_点s(n, (np.cos(np.pi/n))
                   ** i, i*(np.pi/n+旋转角))
    return 点s


# 向外生成点阵
def n_点阵_向外(n, m, 旋转角=0):
    点s = []
    for i in range(m):
        点s += n_点s(n, (np.cos(np.pi/n))
                   ** (-i), i*(np.pi/n+旋转角))
    return 点s


def n_点阵_向外_旋转(n, m, alpha=0, 旋转角=0):
    点s = []
    for i in range(m):
        点s += n_点s(n, (np.cos(np.pi/n))
                   ** (-i), alpha+i*(np.pi/n+旋转角))
    return 点s


def n_点阵_向内_旋转(n, m, alpha=0, 旋转角=0):
    点s = []
    for i in range(m):
        点s += n_点s(n, (np.cos(np.pi/n))
                   ** (i), alpha+i*(np.pi/n+旋转角))
    return 点s
# 画N边形点阵
# n:边数
# m: 阵列层数


def draw_n_点阵(n, m, 旋转角=0, 颜色='b', size=100):
    for i in range(m):
        draw_点s(
            n_点s(n, (np.cos(np.pi/n))**i, i*(np.pi/n+旋转角)), 颜色, size)
        draw_点s(
            n_点s(n, (np.cos(np.pi/n))**(-i), i*(np.pi/n-旋转角)), 颜色, size)

# 向外画点阵


def draw_n_点阵_向外(n, m, 旋转角=0, 颜色='b', size=100):
    for i in range(m):
        draw_点s(
            n_点s(n, (np.cos(np.pi/n))**(-i), i*(np.pi/n+旋转角)), 颜色, size)

# 向内画点阵


def draw_n_点阵_向内(n, m, 旋转角=0, 颜色='b', size=100):
    for i in range(m):
        draw_点s(
            n_点s(n, (np.cos(np.pi/n))**(i), i*(np.pi/n-旋转角)), 颜色, size)


def swastika(N, 主半径=1, 旋转角=0):
    点s = [(主半径*np.sqrt(2)**i*np.cos(i*np.pi/4+旋转角), 主半径*np.sqrt(2)
           ** i*np.sin(i*np.pi/4+旋转角)) for i in range(N)]
    return 点s


"""
这是线的注释
this is a  line 源
"""
# 生成半径主半径圆上N等分点


def n_点s(N, 主半径, 旋转角=0):
    return [[主半径*np.cos(i*2 * np.pi/N+np.pi/2+旋转角), 主半径*np.sin(i*2 * np.pi/N+np.pi/2+旋转角)] for i in range(N)]


# 两两连接所有点


def 连接_全部(点s, 颜色='g'):
    for i in range(len(点s)):
        for j in range(i+1, len(点s)):
            plt.plot([点s[i][0], 点s[j][0]],
                     [点s[i][1], 点s[j][1]], color=颜色)


# 带点两两连接所有点
def 连接_全部_带_点s(点s, 颜色p='b', 颜色l='g'):
    for i in range(len(点s)):
        for j in range(i+1, len(点s)):
            plt.plot([点s[i][0], 点s[j][0]],
                     [点s[i][1], 点s[j][1]], 颜色l)
    for i in range(len(点s)):
        plt.scatter(点s[i][0], 点s[i][1], color=颜色p)

# 首尾连接


def 连接(点s, 颜色='g'):
    num = len(点s)
    for i in range(-1, num-1):
        plt.plot([点s[i][0], 点s[i+1][0]],
                 [点s[i][1], 点s[i+1][1]], color=颜色)


def 连接_顺序(点s, 颜色='g'):
    num = len(点s)
    for i in range(0, num-1):
        plt.plot([点s[i][0], 点s[i+1][0]],
                 [点s[i][1], 点s[i+1][1]], color=颜色)

# 带点首位连接


def 连接_带_点s(点s, 颜色p='b', 颜色l='g'):
    num = len(点s)
    for i in range(-1, num-1):
        plt.plot([点s[i][0], 点s[i+1][0]],
                 [点s[i][1], 点s[i+1][1]], 颜色l)
    for i in range(len(点s)):
        plt.scatter(点s[i][0], 点s[i][1], color=颜色p)

# 多重多边形


def 多重_多边形(n, m, 颜色='b', alpha=0, 旋转角=0):
    for i in range(m):
        连接(n_点s(n, (np.cos(np.pi/n)) **
                (-i), alpha+i*(np.pi/n+旋转角)), 颜色)

# 类梅塔特隆立方体连接


def 连接_like_metatron(n, m, 颜色='b', 旋转角=0):
    点s = []
    for i in range(m):
        点s += n_点s(n, i+1, 旋转角)
    连接_全部(点s, 颜色)

# 卍字连接


def 万字符(n, 主半径, 旋转角=0, 颜色='b'):
    if n == 2:
        for i in range(4):
            plt.plot([主半径*np.sqrt(2)**(n-2)*np.cos(i*2*np.pi/4+旋转角), 0],
                     [主半径*np.sqrt(2) ** (n-2)*np.sin(i*2*np.pi/4+旋转角), 0], color=颜色)
    elif n % 2 == 1:
        for i in range(4):
            plt.plot([主半径*np.sqrt(2)**(n-3)*np.cos(i*2*np.pi/4+旋转角), 0],
                     [主半径*np.sqrt(2) ** (n-3)*np.sin(i*2*np.pi/4+旋转角), 0], color=颜色)
            plt.plot([主半径*np.sqrt(2)**(n-2)*np.cos(i*2*np.pi/4+np.pi/4+旋转角), 0],
                     [主半径*np.sqrt(2) ** (n-2)*np.sin(i*2*np.pi/4+np.pi/4+旋转角), 0], color=颜色)
    else:
        for i in range(4):
            plt.plot([主半径*np.sqrt(2)**(n-2)*np.cos(i*2*np.pi/4+旋转角), 0],
                     [主半径*np.sqrt(2) ** (n-2)*np.sin(i*2*np.pi/4+旋转角), 0], color=颜色)
            plt.plot([主半径*np.sqrt(2)**(n-3)*np.cos(i*2*np.pi/4+np.pi/4+旋转角), 0],
                     [主半径*np.sqrt(2) ** (n-3)*np.sin(i*2*np.pi/4+np.pi/4+旋转角), 0], color=颜色)
    for i in range(4):
        点s = swastika(n, 主半径, i*2*np.pi/4+旋转角)
        连接_顺序(点s, 颜色)


def 万字符s(n, 主半径, m, 颜色='b', 旋转角=0):
    for i in range(m):
        万字符(n, 主半径, i*np.pi/m+旋转角, 颜色)


是 = True
否 = False


def 画板(长, 宽, 坐标等轴=是, 显示坐标轴=否, 背景颜色='#fff'):
    fig, ax = plt.subplots(figsize=(长, 宽))
    if 坐标等轴:
        ax.set_aspect("equal")
    if 显示坐标轴 == 否:
        plt.axis("off")
    fig.patch.set_facecolor(背景颜色)
    return fig, ax


def 画布(长, 宽, 坐标等轴=是, 显示坐标轴=否, 背景颜色='#fff'):
    fig, ax = plt.subplots(figsize=(长, 宽))
    if 坐标等轴:
        ax.set_aspect("equal")
    if 显示坐标轴 == 否:
        plt.axis("off")
    fig.patch.set_facecolor(背景颜色)
    return fig, ax
