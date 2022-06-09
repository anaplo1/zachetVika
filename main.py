import math
import re


#  1


def main1(y, z, x):
    result = 4 * (math.fabs(z ** 3 - y ** 2)) ** 3 + 76 * x ** 4 - (
            (math.exp(z)) ** 5 - 98 * (math.asin(1 + y ** 3 + x ** 2)) ** 7) / (
                     63 * math.sin(68 * x ** 2 + z ** 3 + x) + 8 * math.asin(y) ** 5)
    return result


print(main1(-0.53, -0.98, -0.02))


def main2(y):
    if y < 113:
        result = 84 * (69 * y ** 2 - 97 * y - 50) ** 7 - 71 - (
                4 * (math.cos(1 + y ** 3 + y ** 2)) ** 5)
    elif 113 <= y < 193:
        result = 34 - y ** 4
    elif 193 <= y < 204:
        result = 37 * y
    elif 204 <= y < 237:
        result = math.exp(y) ** 2 + 35 * y ** 4 + (
                49 * (1 - 67 * y ** 2 - y) ** 7)
    elif y >= 237:
        result = y ** 2 + y
    return result


print(main2(244))


def main3(m, n, b, y):
    result = 0
    for c in range(1, b + 1):
        for j in range(1, n + 1):
            for k in range(1, m + 1):
                result += math.sqrt(j) + (
                        (c / 31 - y ** 2 / 3 - k ** 3) ** 4) / 65
    return result


print(main3(3, 4, 2, 0.21))


def main4(n):
    if n == 0:
        return 0.76
    if n >= 1:
        return 11 * (math.sqrt(main4(n - 1) / 22)) ** 3 + 0.03 + (math.log2(main4(n - 1))) ** 2


print(main4(6))


def main5(y, z, x):
    n = len(y)
    y.insert(0, 0)
    x.insert(0, 0)
    z.insert(0, 0)
    result = 0
    for i in range(1, n + 1):
        result += 58 * (28 * (y[n + 1 - i]) ** 3 - z[math.ceil(i / 3)] - 92 * (x[i]) ** 2) ** 2
    return 16 * result


print(main5([0.95, -0.79],
            [0.43, -0.31],
            [0.41, -0.49]))


def zero(x, left, middle, right):
    if x[0] == "VALA":
        return left
    if x[0] == "KRL":
        return middle
    if x[0] == "ANTLR":
        return right


def one(x, left, right):
    if x[1] == "NIX":
        return left
    if x[1] == "VUE":
        return right


def two(x, left, middle, right):
    if x[2] == 2008:
        return left
    if x[2] == 1964:
        return middle
    if x[2] == 2018:
        return right


def four(x, left, right):
    if x[4] == 1964:
        return left
    if x[4] == 2003:
        return right


def three(x, left, middle, right):
    if x[3] == 2001:
        return left
    if x[3] == 1977:
        return middle
    if x[3] == 1995:
        return right


def main6(x):
    return zero(x, four(x, one(x, two(x, 0, 1, 2), three(x, 3, 4, 5)), 6),
                four(x, three(x, two(x, 7, 8, 9), 10, 11), 12), 13)


print(main6(['KRL', 'VUE', 2008, 1977, 1964]))


def main7(input):
    a = (input & 0b00000000000000000000001111111111) << 22
    b = (input & 0b00000001111111111111110000000000) >> 9
    c = (input & 0b00000010000000000000000000000000) >> 7
    d = (input & 0b00000100000000000000000000000000) >> 26
    e = (input & 0b00011000000000000000000000000000) >> 11
    f = (input & 0b11100000000000000000000000000000) >> 10
    return a | b | c | d | e | f


print(main7(0x3adbeec5))


class main(object):
    state = 'A'

    def link(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        elif self.state == 'C':
            self.state = 'D'
            return 3
        elif self.state == 'D':
            self.state = 'F'
            return 7
        else:
            raise KeyError

    def glare(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        elif self.state == 'C':
            self.state = 'C'
            return 5
        elif self.state == 'D':
            self.state = 'E'
            return 6
        elif self.state == 'E':
            self.state = 'F'
            return 8
        else:
            raise KeyError

    def spawn(self):
        if self.state == 'A':
            self.state = 'F'
            return 1
        elif self.state == 'C':
            self.state = 'E'
            return 4
        else:
            raise KeyError


o = main()
# print (o.glare()) # KeyError
print(o.link())  # 0
print(o.glare())  # 2
print(o.glare())  # 5
print(o.link())  # 3
print(o.glare())  # 6
print(o.glare())  # 8


def main8(string):
    key = re.findall(r'{\s*\w*', string)  #  {\s*([^\ \']*)
    code = re.findall(r"'([^\;]*)", string)
    #  string_code = []# - списки
    for i in range(len(key)):
        key[i] = key[i].replace('{', '')
        key[i] = key[i].replace(' ', '')
        key[i] = key[i].replace('\n', '')

        code[i] = code[i].replace("'", '')

        #  string_code.append(code[i].split(' ')) #- списки

    #  d = {key[i]: string_code[i] for i in range(len(key))} #- списки
    d = {key[i]: code[i] for i in range(len(key))}
    return d


print(main8(".begin { ries 'lace_173'; }, { erra_885 'soarla_501';}"
           ",{\ntiorre_368'biri'; }, {rema_46'aron_912'; }, .end"))
