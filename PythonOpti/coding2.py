import timeit
import itertools
import time

import matplotlib.pyplot as plt


def iterate2list_zip():
    # for f, b in zip(numbers, letters):
    #     print(f, b)
    zipped = zip(numbers, letters)

    return list(zipped)


# problem in this for loop is that the two list have to be of the
# same size
def iterate2list_for_loop():
    zipped = []
    for index in range(len(numbers)):
        zipped += [(numbers[index], letters[index])]
    return zipped


def iterate2list_itertools_with_for_loop(numbers, letters):
    zipped = []
    for nu, l in itertools.zip_longest(numbers, letters):
        zipped += [(nu, l)]
    return zipped


def iterate2list_itertools(numbers, letters):
    zipped = itertools.zip_longest(numbers, letters)

    return zipped


def slice_function(end):
    copie = []

    for i in range(0, end):
        copie += [numbers[i]]

    return copie


def copy_list_slice(end):
    sObject = slice(end)
    a = numbers[sObject]
    return a


def copy_list_slice1(start, end):
    a = numbers[start:end+1]
    return a


def copy_list_copy():
    a = numbers.copy()
    return a


def copy_list_list():
    a = list(numbers)
    return a


def iterate_list_enumerate1():
    # print(list(enumerate(letters, start=1)))
    list(enumerate(letters, start=1))


def iterate_list_enumerate3(list_letters):
    list_new = []
    for index, item in enumerate(list_letters, 1):
        list_new.append((index, item))
    # print(list_new)


def iterate_list_enumerate2():
    list_new = []
    for index, item in enumerate(letters, 1):
        list_new.append((index, item))
    # print(list_new)


def iterate_list_for():
    list_new = []
    i = 1
    for item in letters:
        list_new.append((i, item))
        i += 1
    # print(list_new)


def iterate_list_while():
    list_new = []
    i = 0
    while i < len(letters):
        list_new.append((i, letters[i]))
        i += 1
    # print(list_new)


result_iterate2list_zip = []
result_iterate2list_for_loop = []
result_iterate2list_itertools_with_for_loop = []
result_iterate2list_itertools = []
result_copy_list_slice = []
result_slice_function = []
result_copy_list_slice1 = []
result_copy_list_list = []
result_copy_list_copy = []
result_iterate_list_enumerate1 = []
result_iterate_list_enumerate2 = []
result_iterate_list_enumerate3 = []
result_iterate_list_for = []
result_iterate_list_while = []

if __name__ == '__main__':

    fig = plt.figure(figsize=(8.27, 11.69))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)

    ax1.title.set_text('iterate through two lists Comparison')
    ax2.title.set_text('Copy of a list comparison')
    ax3.title.set_text('iterate through a list comparison')
    time0 = time.time()

    m = range(1, 4000, 200)
    print(m)
    for n in m:
        print('Number of zipcodes to append : {}'.format(n))
        numbers = [n for n in range(n)]
        letters = ['a' for n in range(n)]
        repeats = 100
        repeats_copy = 100

        start = 0
        end = len(numbers)

        t = timeit.Timer('iterate2list_zip()',
                         setup='from __main__ import iterate2list_zip')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_iterate2list_zip.append(sec)

        t = timeit.Timer('iterate2list_for_loop()',
                         setup='from __main__ import iterate2list_for_loop')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_iterate2list_for_loop.append(sec)

        t = timeit.Timer('iterate2list_itertools_with_for_loop(numbers, letters)',
                         setup='from __main__ import iterate2list_itertools_with_for_loop, numbers, letters')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_iterate2list_itertools_with_for_loop.append(sec)

        t = timeit.Timer('iterate2list_itertools(numbers, letters)',
                         setup='from __main__ import iterate2list_itertools, numbers, letters')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_iterate2list_itertools.append(sec)

        # slice
        t = timeit.Timer('copy_list_slice(end)',
                         setup='from __main__ import copy_list_slice, end')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_copy_list_slice.append(sec)

        t = timeit.Timer('slice_function(end)',
                         setup='from __main__ import slice_function, end')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_slice_function.append(sec)

        t = timeit.Timer('copy_list_slice1(start, end)',
                         setup='from __main__ import copy_list_slice1, start, end')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_copy_list_slice1.append(sec)

        t = timeit.Timer('copy_list_copy()',
                         setup='from __main__ import copy_list_copy, end')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_copy_list_copy.append(sec)

        t = timeit.Timer('copy_list_list()',
                         setup='from __main__ import copy_list_list, end')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_copy_list_list.append(sec)

        # enumerate
        t = timeit.Timer('iterate_list_enumerate1()',
                         setup='from __main__ import iterate_list_enumerate1')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        result_iterate_list_enumerate1.append(sec)

        t = timeit.Timer('iterate_list_enumerate2()',
                         setup='from __main__ import iterate_list_enumerate2')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_iterate_list_enumerate2.append(sec)

        t = timeit.Timer('iterate_list_enumerate3(letters)',
                         setup='from __main__ import iterate_list_enumerate3, letters')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_iterate_list_enumerate3.append(sec)

        t = timeit.Timer('iterate_list_for()',
                         setup='from __main__ import iterate_list_for')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_iterate_list_for.append(sec)

        t = timeit.Timer('iterate_list_while()',
                         setup='from __main__ import iterate_list_while')
        sec = t.timeit(repeats_copy) / repeats_copy
        sec1 = t.timeit(repeats)
        result_iterate_list_while.append(sec)

    ax1.set_ylabel('Time')
    ax1.set_xlabel('Number')
    ax2.set_ylabel('Time')
    ax2.set_xlabel('Number')
    ax3.set_ylabel('Time')
    ax3.set_xlabel('Number')

    ax1.plot(m, result_iterate2list_zip, color="orange", label="iterate2list_zip")
    ax1.plot(m, result_iterate2list_for_loop, color="blue", label="iterate2list with for loop")
    ax1.plot(m, result_iterate2list_itertools_with_for_loop, color="red", label="iterate2list_itertools and for loop")
    ax1.plot(m, result_iterate2list_itertools, color="green", label="iterate2list_itertools")

    ax2.plot(m, result_copy_list_slice, color="orange", label="copy list: slice()")
    ax2.plot(m, result_slice_function, color="purple", label="function slice()")
    ax2.plot(m, result_copy_list_slice1, color="blue", label="copy list: [:]")
    ax2.plot(m, result_copy_list_copy, color="red", label="copy list: copy()")
    ax2.plot(m, result_copy_list_list, color="green", label="copy list: list()")

    ax3.plot(m, result_iterate_list_enumerate1, color="orange", label="enumerate 1 line")
    ax3.plot(m, result_iterate_list_enumerate2, color="blue", label="enumerate loop ")
    ax3.plot(m, result_iterate_list_enumerate3, color="red", label="enumerate loop with param")
    ax3.plot(m, result_iterate_list_for, color="green", label="iterate loop with for")
    ax3.plot(m, result_iterate_list_while, color="pink", label="iterate loop with while")

    legend1 = ax1.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.05, 0.92))
    legend2 = ax2.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.03, 0.95))
    legend3 = ax3.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.03, 0.95))

    plt.show()

    fig.savefig('graph_effect1.png')

    time1 = time.time()
    timeTotal = time1-time0
    print(timeTotal)
