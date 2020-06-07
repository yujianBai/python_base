# auth Bernard
# date 2020-04-20
"""
如何实现一个短网址系统
    什么是短网址系统？
        把长网址缩短为短网址的系统
        转换之后的网址后缀不超过7字符或者数字

    包含那些接口？


    场景和限制：
        功能：一个长网址转换为短网址并存储； 根据短网址还原为长网址
        转换之后的网址后缀不超过7字符或者数字
        预估峰值插入请求数量级，数百， 查询请求数量级，数千


    数据库设计：
        只需要保存，长网址和对应的短网址

        索引的设计

    算法的实现设计：
        1， md5 摘要算法

        hashlib.md5(url.encode())
        hashlib.md5(url.encode()).
        md5 生成的是32 位的字符

        进制转换：
"""


def mybin(num):
    if num == 0:
        return 0
    res = []
    while num:
        num, rem = divmod(num, 2)
        res.append(str(rem))
    return ''.join(reversed(res))


CHARS = "abcdefghigklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ0123456789"


def encode(num):
    res = []
    if num == 0:
        return 0
    while num:
        num, rem = divmod(num, len(CHARS))
        res.append(CHARS[rem])
    return ''.join(reversed(res))

# 递增序列算法

if __name__ == "__main__":
    print(encode(1))
    print(encode(61))
"""
如何设计一个短网址系统：
    考虑需求
        1, 给一个长网址， 返回一个长度为7的字符
        2，长短链接可以相互转换
        
    数据库设计
        1, id, long2shorturl, short2longurl
        
    并发量
        这个一般为上百人使用， 可以用mysql
        
    算法设计
       递增排序算法
       可以使用的字符为a~z, A~Z, 0~9一共62个字符， 62^7中选择， 满足需求 
"""

CHAR = "asgfasgas"
def encode(num):
    res = []
    if num == 0:
        return 0
    while num:
        num, rem = divmod(num, len(CHAR))
        res.append(CHAR[num])
    return ''.join(reversed(res))
