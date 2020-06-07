# auth Bernard
# date 2020-04-18

"""
内置的算法：
    sorted

    dict /list / set/ tuple


    数据结构/算法         内置语言        内置库

    线性结构             list/tuple     array(数组， 不常用）collectons.namedtuple

    链式结构                            collections.deque(双端队列)

    字典结构             dict           collections.Counter(计数器) / OrderedDict (有序字典）

    集合结构             set / frozenset(不可变集合)

    排序算法             sorted

    二分算法                            bisect模块

    堆算法                              heapq模块

    缓存算法                            functools.lru_cache(Least Recent Used, python3)


collectyions模块： 该模块提供了一些内置的数据结构的扩展
namedtuplde()    factory function for creating tuple subclasses kjwith named fields
deque()          list-like contaioner with fast appends and pops on their end
Counter          dict subclass fro counting hashable objects
OrdereDict       dict subclass that remembers the order enries were added
defaultdict      dict subclass that calls a factory function to supply missing values

"""

import collections

# Point = collections.namedtuple('x', 'y')
# P = Point(1, 2)
# print(P.x)
# print(P.y)


de = collections.deque()

de.append(1)
de.appendleft(0)
print(de)

c = collections.Counter('abcab')
print(c['a'])
print(c.most_common())  # 需要使用计数器功能

od = collections.OrderedDict()  # 可以记录key的访问顺序
od['c'] = 'c'
od['a'] = 'a'
od['b'] = 'b'
print("collections.OrderedDict key是按照key值进入字典的顺序排列")
print(list(od.keys()))

print("*" * 20, "collection.defaultdict()当访问的key不存在时， 设置默认值")
dd = collections.defaultdict(int)  # 带有默认值的字典
print (dd['aa'])

"""
py dict 的底层结构：
    dict底层使用的哈希表
        为了支持快速查找使用了哈希表作为底层结构
        哈希表平均查找时间负责度o(1)
        Cpython 解释器使用二次探查解决哈希冲突
        
        哈希冲突和扩容是常考题 !!!
"""

"""
list 和 tuple区别？
    1， 都是线性结构、 支持下标访问
    2， list是可变对象， tuple保存的引用不可变
"""
t = ([1], 2, 3)
t[0].append('a')
print(t[0])

"""
什么是 LRUCache ? 
    Least-Recently-used 
    缓存剔除策略， 当缓存空间不够用的时候要一种方式剔除 key 
    常见的 LRU(剔除最远使用的), LFU（最近一段时间使用次数最少的剔除）
    LRU通过使用一个循环双端队列， 不断把最新访问的key放到表头实现
    
    
LRU Cache实现：
    一个列表， 一直吧最近使用的放到表的最右侧， 那么没有使用到的就在最左侧， 当需要删除多余的key
    就删除最左侧就行
"""

"""
实现 LRUCache
    使用内置 dict + collection.OrderedDict
    dict用来当做k/v 键值对的缓存
    OrderedDict 用来更新最近访问的key
"""

class LRUCache:
    def __init__(self, capacity=128):
        self.od = collections.OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key in self.od:
            val = self.od[key]
            self.od.move_to_end(key)
            return val
        else:
            return -1

    def put(self, key, value):
        if key in self.od:
            del self.od[key]
            self.od[key] = value
        else:
            self.od[key] = value
            if len(self.od) > self.capacity:
               self.od.popitem(last=False)

def test_LRU_Cache():
    lru_c = LRUCache()
    for i in range(128):
        lru_c.put(i, i)
    assert lru_c.get(1) == 1
    assert lru_c.get(2) == 2
    lru_c.put('a', 'a')
    assert lru_c.get(0) == -1
    assert lru_c.get(3) == 3
    lru_c.put('b', 'b')
    assert lru_c.get(4) == -1

    print(lru_c.od.keys())

if __name__ == "__main__":
    test_LRU_Cache()

