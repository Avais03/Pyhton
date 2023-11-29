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
    def cycle_native____(self):
        print('cycle_native____')
        res = 0
        for i in range(n):
            res += self.num[i]

    @timer
    def cycle_sub_native(self):
        print('cycle_sub_native')
        res = 0
        for i in self.num:
            res += i

    @timer
    def cycle_adv1______(self):
        print('cycle_adv1______')
        res = sum(self.num)

    def example(self):
        self.num = [i for i in range(n)]  # n = 10^8
        self.cycle_native____()  # 4.157872818999749s || lenovo: 5.545829300999685
        self.cycle_sub_native()  # 2.491715354997723s || lenovo: 2.705761461000293
        self.cycle_adv1______()  # 0.9733216369932052 || lenovo: 0.4968933929994819


class IndexAccess:
    num = []

    @timer
    def index_____native(self):
        print('index_____native')
        for i in range(len(self.num)):
            tmp = self.num[i]

    @timer
    def index_sub_native(self):
        print('index_sub_native')
        for i in self.num:
            temp = i

    @timer
    def index_______adv1(self):
        print('index_______adv1')
        for i, obj in enumerate(self.num):
            temp = obj

    def example(self):
        self.num = [i for i in range(n)]  # n = 10^8
        self.index_____native()  # 3.904384661000222s || lenovo: 4.798514468999201s
        self.index_sub_native()  # 2.6519364929990843 || lenovo: 2.504630839001038
        self.index_______adv1()  # 0.521043800006737s || lenovo: 0.6232677369989688


class Zip:
    list1 = []
    list2 = []

    @timer
    def native_sum(self):
        print('native_sum')
        for i in range(len(self.list1)):
            res = self.list1[i] + self.list2[i]

    @timer
    def adv1___sum(self):
        print('adv1___sum')
        for list1_obj, list2_obj in zip(self.list1, self.list2):
            res = list1_obj + list2_obj

    def example(self):
        self.list1 = [i for i in range(n)]  # n = 10^8
        self.list2 = [i for i in range(n)]  # n = 10^8
        self.native_sum()  # 7.785930849997385 || lenovo: 6.300028674999339
        self.adv1___sum()  # 3.772999421998975 || lenovo: 3.1109938560002774


class ListComprehension:
    num = []

    @timer
    def find_ans_____native(self):
        print('find_ans_____native')
        res = 0
        for i in range(len(self.num)):
            res += (self.num[i] % 2 == 0)

    @timer
    def find_ans_sub_native(self):
        print('find_ans_sub_native')
        res = 0
        for i in self.num:
            res += (i % 2 == 0)

    @timer
    def list__comprehension(self):
        print('list__comprehension')
        tmp_list = [1 for i in self.num if i % 2 == 0]
        sum(tmp_list)

    @timer
    def list__comprehension_mod(self):
        print('list__comprehension_mod')
        sum([1 for i in self.num if i % 2 == 0])

    @timer
    def generator_______use(self):
        print('generator_______use')
        tmp_list = (1 for i in self.num if i % 2 == 0)
        sum(tmp_list)

    @timer
    def generator_______use_mod(self):
        print('generator_______use_mod')
        sum((1 for i in self.num if i % 2 == 0))

    @timer
    def sub_native_and_list(self):
        print('sub_native_and_list')
        res = len(self.num) - sum([i % 2 for i in self.num])

    def example(self):
        self.num = [randint(0, 100) for i in range(n / 10)]  # n = 10^8
        self.find_ans_____native()  # 7.730938418993901s || lenovo: 7.207540434999828
        self.find_ans_sub_native()  # 4.461346458003391s || lenovo: 3.706796721999126
        self.list__comprehension()  # 3.5958626020001248 || lenovo: 3.6337942739992286
        self.list__comprehension_mod()  # || lenovo: 3.6253979390003224
        self.generator_______use()  # 3.774691840997548s || lenovo: 3.720844411998769
        self.generator_______use_mod()  # || lenovo: 3.7331595510004263
        self.sub_native_and_list()  # || lenovo: 2.45510546100013


def main():
    # example1 = Sum()
    # example1.example()
    #
    # example2 = IndexAccess()
    # example2.example()
    #
    example3 = Zip()
    example3.example()

    # example4 = ListComprehension()
    # example4.example()


if __name__ == "__main__":
    main()
