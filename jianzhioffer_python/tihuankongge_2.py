# auth Bernard
# date 2020-06-07

'''
2.替换空格
Q: 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

A1： 先计算最终需要给出的长度，然后建立两个指针p1,p2，p1指向原始字符串的末尾，p2指向替换后的字符串的末尾。
同时移动p1,p2, 将p1指的内容逐个复制到p2, 当p1遇到空格时，在p2处插入 %20， p1向前移动一个位置，p2向前移动3个位置，当p1和p2位置重合时，全部替换完成。

A2: python中可以利用append() [O(1)]，新建list，一次遍历，碰到空格就添加 %20，否则就添加原始字符串s内容。

'''


def neizhi_func(s):
    return s.replace(' ', '%20')


def replaceSpace(s):
    if not isinstance(s, str) or len(s) <= 0 or s == None:
        return ''
    spaceNum = 0
    for i in s:
        if i == " ":
            spaceNum += 1
    newStrLen = len(s) + spaceNum * 2  # 新字符串长度
    newStr = newStrLen * [None]  # 新字符串， 默认都是None
    indexOfOrginal, indexOfNew = len(s) - 1, newStrLen - 1
    while indexOfNew >= 0 and indexOfOrginal <= indexOfNew:
        if s[indexOfOrginal] == " ":
            newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
            indexOfNew -= 3
            indexOfOrginal -= 1
        else:
            newStr[indexOfNew] = s[indexOfOrginal]
            indexOfNew -= 1
            indexOfOrginal -= 1
    return ''.join(newStr)


def replaceSpace2(s):
    ret = []
    for i in s:
        if i == " ":
            ret.append('%20')
        else:
            ret.append(i)
    return "".join(ret)


def replaceSpace3(s):
    if not isinstance(s, str) or len(s) <= 0 or s == None:
        return ''
    ret = ''
    for i in s:
        if i == " ":
            ret += '%20'
        else:
            ret += i
    return ret


if __name__ == "__main__":
    # print(neizhi_func('are you reday'))
    # print(replaceSpace("I'm reday"))
    # print(replaceSpace("How are you "))
    print(replaceSpace2("How are you 2"))
    print(replaceSpace3("How are you 3"))
