#auth Bernard
#date 2020-04-10

'''
len(), 函数， 求长度，
    参数：
        string, 字符串长度
        list, dict, tuple (元素的个数)


'''
def count(*param):   # *param 元组
    length = len(param)

    print("len(param):{}".format(length))

    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0

        for each in param[i]:
            if each.isalpha():
                letters += 1
            elif each.isdigit():
                digit += 1
            elif each == ' ':
                space += 1
            else:
                others += 1
        print('第 %d 个字符串共有 英文字母 %d个， 数字 %d, 空格 %d个， 其他字符 %d'%(i+1,
            letters, digit, space, others
        ))

def test_count():
    str1 = '''sdfasadffffff拷贝一段话
    asdfasdf
    safdsf
    范德萨发
    '''

    list1 = []
    for each in str1:
        if each not in list1:
            if each == '\n':
                print('\\n','有:', str1.count(each), '个')
            else:
                print(each,'有:', str1.count(each), '个')
            # print(each, str1.count(each))
            list1.append(each)
    print("list1:{}".format(list1))


'''
1, 打字
2, 编程
    面向过程的：c (for, 函数， 数据结构, 面向问题, 算法:程序快, 更准确)
    熟悉一门高级语言: 编程思想, 抽象(类， 封装) ==> 代码复用

3, 具体项目
    没门语言有各自擅长的领域 
    python:机器学习， 人工智能
    java: 大数据, 互联网架构
    C# ： 做windows下的一些东西

==> 面向业务， 面相问题, 单独的模块
    
4, 架构师：
    系统的架构, 从系统运行的角度出发，考虑实现过程

311中国航天发动机集团

'''

if __name__ == "__main__":
    # count('I love fishc.com. ' , 'I loce you, you love me.')
    # a = '123//n4546'
    # print(a)
    test_count()

    # print("原样输出")
    # print("格式化, 数字%d"%10)
    # print("格式化, 浮点数%f"%10.10)
    # # print("格式化, 浮点数%s"%10.10)
    # print("参数一:%d, 参数二：%.2f, 参数三：%s"%(10, 0.1, 'asfdasd'))
    # print("参数一:{}, 参数二：{}，参数3：{}".format(10, 'asdfasf', 0.1))

