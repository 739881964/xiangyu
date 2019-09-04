class Calc(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def minus(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return '被除数不能为0'
