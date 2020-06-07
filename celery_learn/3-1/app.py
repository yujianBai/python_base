# auth Bernard
# date 2020-06-03
from tasks import add

if __name__ == "__main__":
    print("start task ...")
    # result = add(2, 8)  这里不是异步方法
    result = add.delay(2, 8)
    print(result)
    print("end task ...")
