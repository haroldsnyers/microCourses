import memory_profiler
from memory_profiler import profile
import time
import timeit


class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}  # keeps track of previous runs

    def __call__(self, *args):
        # checks if answer already is in cache, otherwise execute the function
        if args not in self.memo:
            self.memo[args] = self.fn(*args)
        return self.memo[args]


@Memoize
def fibonacci_mem(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_mem(n-1) + fibonacci_mem(n-2)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# #################### with memoize ###############################
print('#'*20 + "With memoize" + '#'*20)
print(fibonacci_mem.memo)
fibonacci_mem.memo.clear()
print(fibonacci_mem.memo)
for x in (145, 145, 150):
    memory_1 = memory_profiler.memory_usage()
    print("time to execute : " + str(timeit.timeit('fibonacci_mem(x)', globals=globals(), number=1)))
    memory_2 = memory_profiler.memory_usage()
    memory_diff = memory_2[0] - memory_1[0]
    print("Method with memoize took {0} as memory".format(memory_diff))
    # print(fibonacci_mem.memo)
    print('\n')

# #################### without memoize ###############################
print("\n" + '#'*20 + "Without memoize" + '#'*20)

for y in (35, 35, 25):
    memory_1 = memory_profiler.memory_usage()
    print("time to execute : " + str(timeit.timeit('fibonacci(y)', globals=globals(), number=1)))
    memory_2 = memory_profiler.memory_usage()
    memory_diff = memory_2[0] - memory_1[0]
    print("Method without memoize took {0} as memory".format(memory_diff))








