import string
import random

class Robot:
    name_list = [""]

    def __init__(self):
        self.name = ""
        self.get_name()

    def get_name(self):
        def generator():
            uppers = [i for i in string.ascii_uppercase]
            digits = [i for i in string.digits]
            str1 = ''.join((random.choices(uppers, k=2)))
            str2 = ''.join((random.choices(digits, k=3)))
            return (str1 + str2)
        name = generator()
        if name in Robot.name_list:
            self.get_name()
        else:
            Robot.name_list.append(name)
            self.name = name

    def reset(self):
        self.__init__() # reinitialize
