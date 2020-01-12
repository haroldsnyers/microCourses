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


def updateZips_param(newZipcodes, Zipcodes):
    for zipcode in newZipcodes:
        Zipcodes.append(zipcode.strip())


def updateZipsWithMap_param(newZipcodes, Zipcodes):
    Zipcodes += map(str.strip, newZipcodes)


def updateZipsWithListCom_param(newZipcodes, Zipcodes):
    Zipcodes += [iter.strip() for iter in newZipcodes]


def updateZipsWithGenExp_param(newZipcodes, Zipcodes):
    return itertools.chain(Zipcodes, (iter.strip() for iter in newZipcodes))


result_updateZips_global = []
result_updateZipsWithMap_global = []
result_updateZipsWithListCom_global = []
result_updateZipsWithGenExp_global = []
result_updateZips_param = []
result_updateZipsWithMap_param = []
result_updateZipsWithListCom_param = []
result_updateZipsWithGenExp_param = []
result_updateZips= []
result_updateZipsWithMap = []
result_updateZipsWithListCom = []
result_updateZipsWithGenExp = []

if __name__ == '__main__':

    fig = plt.figure(figsize=(11.69, 8.27))
    fig.suptitle('python Optimisation', fontsize=16, y=0.95)
    fig.subplots_adjust(top=3.8)
    ax1 = fig.add_subplot(111)
    # ax2 = fig.add_subplot(323)
    # ax3 = fig.add_subplot(324)
    # ax4 = fig.add_subplot(325)
    # ax5 = fig.add_subplot(326)
    # ax1.title.set_text('Comparison')
    # ax2.title.set_text('for loop')
    # ax3.title.set_text('Map')
    # ax4.title.set_text('List Comprehension ')
    # ax5.title.set_text('generator expression')

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
        # print('updateZips_global() Time              : {} seconds'.format(sec))
        # print('updateZips_global() Time t            : {} seconds'.format(sec1))
        result_updateZips_global.append(sec)

        Zipcodes = ['121212', '232323', '434334']
        t = timeit.Timer('updateZipsWithMap_global(Zipcodes)',
                         setup='from __main__ import updateZipsWithMap_global, Zipcodes')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        # print('updateZipsWithMap_global() Time       : {} seconds'.format(sec))
        # print('updateZipsWithMap_global()() Time t   : {} seconds'.format(sec1))
        result_updateZipsWithMap_global.append(sec)

        Zipcodes = ['121212', '232323', '434334']
        t = timeit.Timer('updateZipsWithListCom_global(Zipcodes)',
                         setup='from __main__ import updateZipsWithListCom_global, Zipcodes')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        # print('updateZipsWithListCom_global() Time   : {} seconds'.format(sec))
        # print('updateZipsWithListCom_global() Time t : {} seconds'.format(sec1))
        result_updateZipsWithListCom_global.append(sec)

        Zipcodes = ['121212', '232323', '434334']
        t = timeit.Timer('updateZipsWithGenExp_global()', setup='from __main__ import updateZipsWithGenExp_global')
        sec = t.timeit(repeats) / repeats
        sec1 = t.timeit(repeats)
        # print('updateZipsWithGenExp_global() Time    : {} seconds'.format(sec))
        # print('updateZipsWithGenExp_global() Time t  : {} seconds'.format(sec1))
        result_updateZipsWithGenExp_global.append(sec)

        # Zipcodes = ['121212', '232323', '434334']
        # t = timeit.Timer('updateZips_param(newZipcodes, Zipcodes)',
        #                  setup='from __main__ import updateZips_param, Zipcodes, newZipcodes')
        # sec = t.timeit(repeats) / repeats
        # sec1 = t.timeit(repeats)
        # # print('updateZips_global() Time              : {} seconds'.format(sec))
        # # print('updateZips_global() Time t            : {} seconds'.format(sec1))
        # result_updateZips_param.append(sec)
        #
        # Zipcodes = ['121212', '232323', '434334']
        # t = timeit.Timer('updateZipsWithMap_param(newZipcodes, Zipcodes)',
        #                  setup='from __main__ import updateZipsWithMap_param, Zipcodes, newZipcodes')
        # sec = t.timeit(repeats) / repeats
        # sec1 = t.timeit(repeats)
        # # print('updateZipsWithMap_global() Time       : {} seconds'.format(sec))
        # # print('updateZipsWithMap_global()() Time t   : {} seconds'.format(sec1))
        # result_updateZipsWithMap_param.append(sec)
        #
        # Zipcodes = ['121212', '232323', '434334']
        # t = timeit.Timer('updateZipsWithListCom_param(newZipcodes, Zipcodes)',
        #                  setup='from __main__ import updateZipsWithListCom_param, Zipcodes, newZipcodes')
        # sec = t.timeit(repeats) / repeats
        # sec1 = t.timeit(repeats)
        # # print('updateZipsWithListCom_global() Time   : {} seconds'.format(sec))
        # # print('updateZipsWithListCom_global() Time t : {} seconds'.format(sec1))
        # result_updateZipsWithListCom_param.append(sec)
        #
        # Zipcodes = ['121212', '232323', '434334']
        # t = timeit.Timer('updateZipsWithGenExp_param(newZipcodes, Zipcodes)',
        #                  setup='from __main__ import updateZipsWithGenExp_param, Zipcodes, newZipcodes')
        # sec = t.timeit(repeats) / repeats
        # sec1 = t.timeit(repeats)
        # # print('updateZipsWithGenExp_global() Time    : {} seconds'.format(sec))
        # # print('updateZipsWithGenExp_global() Time t  : {} seconds'.format(sec1))
        # result_updateZipsWithGenExp_param.append(sec)

    ax1.set_ylabel('Time')
    ax1.set_xlabel('Number')
    # ax2.set_ylabel('Time')
    # ax2.set_xlabel('Number')
    # ax3.set_ylabel('Time')
    # ax3.set_xlabel('Number')
    # ax4.set_ylabel('Time')
    # ax4.set_xlabel('Number')
    # ax5.set_ylabel('Time')
    # ax5.set_xlabel('Number')

    ax1.plot(m, result_updateZips_global, color="orange", label="updateZips")
    ax1.plot(m, result_updateZipsWithMap_global, color="blue", label="updateZipsWithMap")
    ax1.plot(m, result_updateZipsWithListCom_global, color="green", label="updateZipsWithListCom")
    ax1.plot(m, result_updateZipsWithGenExp_global, color="red", label="updateZipsWithGenExp")

    # ax2.plot(m, result_updateZips_global, color="orange", label="updateZips_global")
    # ax2.plot(m, result_updateZips_param, color="blue", label="updateZips_param")
    # ax2.plot(m, result_updateZips, color="green", label="updateZips")

    # ax3.plot(m, result_updateZipsWithMap_global, color="orange", label="updateZipsWithMap_global")
    # ax3.plot(m, result_updateZipsWithMap_param, color="blue", label="updateZipsWithMap_param")
    # ax3.plot(m, result_updateZipsWithMap, color="green", label="updateZipsWithListMAP")

    # ax4.plot(m, result_updateZipsWithListCom_global, color="orange", label="updateZipsWithListCom_global")
    # ax4.plot(m, result_updateZipsWithListCom_param, color="blue", label="updateZipsWithListCom_param")
    # ax4.plot(m, result_updateZipsWithListCom, color="green", label="updateZipsWithListCom")

    # ax5.plot(m, result_updateZipsWithGenExp_global, color="orange", label="result_updateZipsWithGenExp_global")
    # ax5.plot(m, result_updateZipsWithGenExp_param, color="blue", label="result_updateZipsWithGenExp_param")
    # ax5.plot(m, result_updateZipsWithGenExp, color="green", label="result_updateZipsWithGenExp")

    legend = fig.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.1, 0.90), ncol=1)
    # legend1 = ax2.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.1, 0.9))
    # legend2 = ax3.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.1, 0.9))
    # legend3 = ax4.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.1, 0.9))
    # legend4 = ax5.legend(loc='upper left', shadow=True, fontsize='medium', bbox_to_anchor=(0.1, 0.9))

    plt.show()

    fig.savefig('graph_opti.png')
