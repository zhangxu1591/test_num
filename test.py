# 题目1: 用一个数组实现两个栈，只需处理整型，实现l_pop/l_push/r_pop/r_push，需要UT。
num_list = [1, 2, 3, 4, 5, 6]


class Num(object):
    def l_pop(self):
        num_list.pop(0)
        print(num_list)

    def r_pop(self):
        num_list.pop()
        print(num_list)

    def l_push(self, num):
        num_list.insert(0, num)
        print(num_list)

    def r_push(self, num):
        num_list.append(num)
        print(num_list)


number = Num()
number.l_pop()
number.r_pop()
number.l_push(1)
number.r_push(1)

# 题目2: 实现一个hash table，input数据是最长1024的ascii码，需要UT。

# 题目3: 大数加法，需要UT。

# 题目4: 大数乘法，需要UT。
