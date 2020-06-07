# auth Bernard
# date 2020-06-07


if __name__ == "__main__":
    a = [1, 2, 3, 4]
    a_l = len(a)
    print(a[a_l - 2: a_l + 1])
    a[a_l - 2: a_l + 1] = [5, 6, 7]
    print("len(a):{}, a:{}".format(len(a), a))
