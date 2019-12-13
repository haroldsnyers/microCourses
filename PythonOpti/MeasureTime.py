import timeit
import profile

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def while_loop(array):
    i = 0
    sum_numbers = 0
    while i < len(array):
        sum_numbers += i
        i += 1


def for_loop(array):
    sum_numbers = 0
    for i in array:
        sum_numbers += i


def for_loop2(array):
    sum_numbers = 0
    for i in range(len(array)):
        sum_numbers += array[i]


def sum_function(array):
    sum(array)


result_while = []
result_for = []
result_for2 = []
result_sum = []

if __name__ == '__main__':

    fig = plt.figure(figsize=(11.69, 8.27))
    for point in range(0, 1000, 100):
        array_to_sum = [x for x in range(point)]
        repeats = 100
        # print('while loop')
        t_while = timeit.Timer('while_loop(array_to_sum)', setup="from __main__ import while_loop, array_to_sum")
        sec_while = t_while.timeit(repeats) / repeats
        # print('{} seconds'.format(sec_while))
        result_while.append(sec_while)
        # profile.run("arrayToSum : while_loop(array_to_sum) ")

        # print('for loop')
        t_for = timeit.Timer('for_loop(array_to_sum)', setup="from __main__ import for_loop, array_to_sum")
        sec_for = t_for.timeit(repeats) / repeats
        # print('{} seconds'.format(sec_for))
        result_for.append(sec_for)

        t_for2 = timeit.Timer('for_loop2(array_to_sum)', setup="from __main__ import for_loop2, array_to_sum")
        sec_for2 = t_for2.timeit(repeats) / repeats
        # print('{} seconds'.format(sec_for))
        result_for2.append(sec_for2)

        # print('sum loop')
        t_sum = timeit.Timer('sum_function(array_to_sum)', setup="from __main__ import sum_function, array_to_sum")
        sec_sum = t_sum.timeit(repeats) / repeats
        # print('{} seconds'.format(sec_sum))
        result_sum.append(sec_sum)

        # print('End')
    for_patch = mpatches.Patch(color="orange", label="For Loop")
    while_patch = mpatches.Patch(color="blue", label="While Loop")
    sum_patch = mpatches.Patch(color="green", label="Sum Loop")
    for2_patch = mpatches.Patch(color="red", label="for loop with range")
    fig.legend(handles=[for_patch, while_patch, sum_patch, for2_patch], loc=2, fancybox=False, shadow=False, ncol=3,
               fontsize='small', bbox_to_anchor=(0.1, 0.9))

    plt.plot(result_while)
    plt.plot(result_for)
    plt.plot(result_sum)
    plt.plot(result_for2)
    plt.show()

    fig.savefig('graph.png', transparent=True)
