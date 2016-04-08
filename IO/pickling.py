# import pickle
# d = dict(name='Bob', age=20, score=88)
# pickle.dumps(d)
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()
#
# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)


import json

d = dict(name='Bob', age=20, score=88)
a = json.dumps(d)
print(a)

d = json.loads(a)
print(d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


s = Student('Bob', 20, 80)
print(json.dumps(s, default=student2dict))
