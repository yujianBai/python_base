# auth Bernard
# date 2020-04-16

class Base(object):
    def hello(self):
        print('hello')


class C(Base):
    def hello(self):
        # py2
        return super(C, self).hello()


class C2(Base):
    def hello(self):
        # py3
        return super().hello()


if __name__ == "__main__":
    pass
