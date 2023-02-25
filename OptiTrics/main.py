from time import perf_counter
from random import randint

n = 100_000_000


def timer(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        func(*args, **kwargs)
        print(perf_counter() - start)

    return wrapper


class Sum:
    num = []

    @timer
    def cycle_native(self):
        res = 0
        for i in range(n):
            res += self.num[i]

    @timer
    def cycle_sub_native(self):
        res = 0
        for i in self.num:
            res += i

    @timer
    def cycle_adv1(self):
        res = sum(self.num)

    def example(self):
        self.num = [i for i in range(n)]  # n = 10^8
        self.cycle_native()  # 4.157872818999749s
        self.cycle_sub_native()  # 0.9733216369932052
        self.cycle_adv1()  # 2.491715354997723


class IndexAccess:
    num = []

    @timer
    def index_____native(self):
        for i in range(len(self.num)):
            tmp = self.num[i]

    @timer
    def index_sub_native(self):
        for i in self.num:
            temp = i

    @timer
    def index_______adv1(self):
        for i, obj in enumerate(self.num):
            temp = obj

    def example(self):
        self.num = [i for i in range(n)]  # n = 10^8
        self.index_____native()  # 3.904384661000222s
        self.index_sub_native()  # 2.6519364929990843
        self.index_______adv1()  # 0.521043800006737


class Zip:
    list1 = []
    list2 = []

    @timer
    def native_sum(self):
        for i in range(len(self.list1)):
            res = self.list1[i] + self.list2[i]

    @timer
    def adv1___sum(self):
        for list1_obj, list2_obj in zip(self.list1, self.list2):
            res = list1_obj + list2_obj

    def example(self):
        self.list1 = [i for i in range(n)]  # n = 10^8
        self.list2 = [i for i in range(n)]  # n = 10^8
        self.native_sum()  # 7.785930849997385
        self.adv1___sum()  # 3.772999421998975


class ListComprehension:
    num = []

    @timer
    def find_ans_____native(self):
        res = 0
        for i in range(len(self.num)):
            res += (self.num[i] % 2 == 0)

    @timer
    def find_ans_sub_native(self):
        res = 0
        for i in self.num:
            res += (i % 2 == 0)

    @timer
    def list__comprehension(self):
        tmp_list = [1 for i in self.num if i % 2 == 0]
        sum(tmp_list)

    @timer
    def generator_______use(self):
        tmp_list = (1 for i in self.num if i % 2 == 0)
        sum(tmp_list)

    def example(self):
        self.num = [randint(0, 100) for i in range(n)]  # n = 10^8
        self.find_ans_____native()  # 7.730938418993901s
        self.find_ans_sub_native()  # 4.461346458003391s
        self.list__comprehension()  # 3.5958626020001248
        self.generator_______use()  # 3.774691840997548


def main():
    # example1 = Sum()
    # example1.example()
    #
    # example2 = IndexAccess()
    # example2.example()
    #
    # example3 = Zip()
    # example3.example()

    example4 = ListComprehension()
    example4.example()


if __name__ == "__main__":
    main()
