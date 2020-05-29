import memory_profiler
from memory_profiler import profile
import time


# Build and return a list
# @profile
def calculate_first_n(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


n = 1_000_000

memory_first_1 = memory_profiler.memory_usage()
time_first_1 = time.time()
sum_of_first_n = sum(calculate_first_n(n))
time_first_2 = time.time()
memory_first_2 = memory_profiler.memory_usage()
time_difference = time_first_2 - time_first_1
memory_diff = memory_first_2[0] - memory_first_1[0]
print("Method without generators took {0} time and took {1} as memory".format(time_difference, memory_diff))


# a generator that yields items instead of returning a list
# @profile
def calculate_first_n_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1


memory_first_gen_1 = memory_profiler.memory_usage()
time_first_gen_1 = time.time()
sum_of_first_n_gen = sum(calculate_first_n_gen(n))
time_first_gen_2 = time.time()
memory_first_gen_2 = memory_profiler.memory_usage()
time_difference_gen = time_first_gen_2 - time_first_gen_1
memory_diff_gen = memory_first_gen_2[0] - memory_first_gen_1[0]
print("Method with generators took {0} time and took {1} as memory".format(time_difference_gen, memory_diff_gen))



