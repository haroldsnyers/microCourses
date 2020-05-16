#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
__author__ = 'Harold Snyers'
__course__ = 'Micro Courses'
# __teammates__ = ['Jeromie Kirchoff']
__assessment__ = 'Coding 1'
__title__ = 'Measuring time execution'
__date__ = '2020/01/12'
__description__ = 'Python optimisation showing time optimisation of sum \n' \
                  '             function compared to while and for loop'
print('# ' + '=' * 78)
print('Author: ' + __author__)
print('Course: ' + __course__)
print('Assessment: ' + __assessment__)
print('Title: ' + __title__)
print('Date: ' + __date__)
print('Description: ' + __description__)
print('# ' + '=' * 78)

# =============================================================================
# Imports
# =============================================================================
import timeit
import profile

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# =============================================================================
# Code
# =============================================================================


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
    n = range(0, 10000, 1000)
    for point in n:
        print("Compute of elements of given list of size " + str(point))
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
    fig.legend(handles=[for_patch, while_patch, sum_patch, for2_patch], loc=2, fancybox=False, shadow=False,
               fontsize='medium', bbox_to_anchor=(0.1, 0.95))

    plt.ylabel('Time')
    plt.xlabel('Number')

    plt.plot(n, result_while)
    plt.plot(n, result_for)
    plt.plot(n, result_sum)
    plt.plot(n, result_for2)
    plt.show()

    graphName = "graphes/graph_coding1.png"
    print('\nSaving graph as ' + graphName)
    fig.savefig(graphName, transparent=True)

