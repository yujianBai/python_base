# auth Bernard
# date 2020-04-06

board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]

total = 0

def can_place(x, y):
    # 判断（x, y)坐标能否放皇后
    # 1， 判断x行是否有皇后
    for i in range(0, y):
        if board[x][i] == 1:
            return False
    # 2， 判断y轴是否有皇后
    for i in range(0, x):
        if board[i][y] == 1:
            return False
    # 3， 判断 / 方向是否有皇后
    for i in range(0, x):
        if x + y - i <= 7 and board[i][x + y - i] == 1:
            return False
    # 4, 判断\ 方向是否有皇后
    for index, i in enumerate(range(x - 1, -1, -1)):
        s_y = y - (index + 1)
        if s_y >= 0:
            if board[i][s_y] == 1:
                return False
    return True


def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                print("O  ", end="")
            else:
                print("X  ", end="")
        print("\n")


def put_queen(step):
    if step == 8:
        print_board(board)
        global total
        total += 1
        print("----------------------")
    else:
        # 解空间是固定的
        for i in range(8):
            if can_place(step, i):
                # 1, 设置现场
                board[step][i] = 1
                # 2， 开始递归
                put_queen(step + 1)
                # 3， 恢复现场
                board[step][i] = 0


if __name__ == "__main__":
    # print_board(board)
    put_queen(0)
    print("总共有{}方法".format(total))
