# auth Bernard
# date 2020-03-19

class Student:
    def __init__(self, age, name, score):
        self.age = age
        self.name = name
        self.score = score

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_score(self):
        return self.score


if __name__ == "__main__":
    xiaoming = Student(18, 'xiaoming', [90, 91, 99])
    print(xiaoming.get_age())
    print(xiaoming.get_name())
    print(xiaoming.get_score())
