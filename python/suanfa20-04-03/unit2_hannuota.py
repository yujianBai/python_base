#auth Bernard
#date 2020-04-05

# 1， 大傻，只搬一号盘
# 2， 1， 叫谁来做，：1， 从哪个柱子搬到哪个柱子
# 3， 2，搬动自己负责的柱子， 3， 从哪个柱子搬动到哪个柱子

def move(index, start, mid, end):
    if index == 1:
        # 将最后一个盘子从start， 移动到end
        print("{}: {}-->{}".format(index, start, end))
        return
    else:
        move(index-1, start, end, mid) # 把所有盘子从start，经过end,移动到mid上
        print("{}: {}-->{}".format(index, start, end))
        move(index-1, mid, start, end) # 把所有盘子从mid, 经过start, 移动到end

if __name__ == "__main__":
    move(3, "A", "B", "C")
