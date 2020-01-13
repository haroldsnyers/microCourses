#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
__author__ = 'Harold Snyers'
__course__ = 'Micro Courses'
# __teammates__ = ['Jeromie Kirchoff']
__assessment__ = 'Mission 2'
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
import itertools

import matplotlib.pyplot as plt


def updateZips_global():
    for zipcode in newZipcodes:
        Zipcodes.append(zipcode.strip())


def updateZipsWithMap_global(Zipcodes):
    Zipcodes += map(str.strip, newZipcodes)


def updateZipsWithListCom_global(Zipcodes):
    Zipcodes += [iter.strip() for iter in newZipcodes]


def updateZipsWithGenExp_global():
    return itertools.chain(Zipcodes, (iter.strip() for iter in newZipcodes))


result_updateZips_global = []
result_updateZipsWithMap_global = []
result_updateZipsWithListCom_global = []
result_updateZipsWithGenExp_global = []

if __name__ == '__main__':

    fig = plt.figure(figsize=(11.69, 8.27))
    fig.suptitle('python Optimisation', fontsize=16, y=0.95)
    fig.subplots_adjust(top=3.8)
    ax1 = fig.add_subplot(111)

    Zipcodes = ['121212', '232323', '434334']
    m = range(25, 400, 25)
    print(m)
    for n in m:
        print('Number of zipcodes to append : {}'.format(n))
        newZipcodes = ['  131313 ' for i in range(n)]

        repeats = 10000

        t = timeit.Timer('updateZips_global()', setup='from __main__ import updateZips_global')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_updateZips_global.append(sec)

        Zipcodes = ['121212', '232323', '434334']
        t = timeit.Timer('updateZipsWithMap_global(Zipcodes)',
                         setup='from __main__ import updateZipsWithMap_global, Zipcodes')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_updateZipsWithMap_global.append(sec)

        Zipcodes = ['121212', '232323', '434334']
        t = timeit.Timer('updateZipsWithListCom_global(Zipcodes)',
                         setup='from __main__ import updateZipsWithListCom_global, Zipcodes')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_updateZipsWithListCom_global.append(sec)

        Zipcodes = ['121212', '232323', '434334']
        t = timeit.Timer('updateZipsWithGenExp_global()', setup='from __main__ import updateZipsWithGenExp_global')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_updateZipsWithGenExp_global.append(sec)

    ax1.set_ylabel('Time')
    ax1.set_xlabel('Number')

    ax1.plot(m, result_updateZips_global, color="orange", label="updateZips")
    ax1.plot(m, result_updateZipsWithMap_global, color="blue", label="updateZipsWithMap")
    ax1.plot(m, result_updateZipsWithListCom_global, color="green", label="updateZipsWithListCom")
    ax1.plot(m, result_updateZipsWithGenExp_global, color="red", label="updateZipsWithGenExp")

    legend = fig.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.1, 0.90), ncol=1)

    plt.show()

    graphName = "graphes/graph_mission2.png"
    print('\nSaving graph as ' + graphName)
    fig.savefig(graphName, transparent=True)
