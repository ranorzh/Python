class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的学习.' % self._name)

    def watch_av(self):
        if self._age >= 18:
            print('%s正在看《权力的游戏》.' % self._name)
        else:
            print('%s只能观看《虹猫蓝兔七侠传》.' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在愉快地学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._name, self._title, course))


def main():
    stu1 = Student('陈辰', 15, '初三')
    stu1.study('音乐')
    stu1.play()
    stu1.watch_av()
    stu2 = Student('李四', 21, '大四')
    stu2.study('跳舞')
    stu2.play()
    stu2.watch_av()
    t = Teacher('辰长', 22, '中二阳光宅男')
    t.teach('Python和Taichi')
    t.watch_av()
    t.play()


if __name__ == '__main__':
    main()
