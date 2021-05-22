# Pythonlesson20210522
class Student:
    def __init__(self):  # __init__(self) 初始化
        myname = input("請輸入名字")

        self.name = myname
        print("我出現了，名字是",myname)
        self.do_hw("英文")
        self.study()

    def do_hw(self,hw):
        print("我在寫作業",hw)
    def study(self):
        print("我在讀書")
s = Student()
print(s)
