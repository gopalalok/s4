# coding=utf-8
from random import randint
import matplotlib.pyplot as plt

from solvers.generalizedparity import generalized_parity_solver
from tools import timer, generators

"""
This module benchmarks the generalized parity games algorithm
"""


def benchmark_random_k_functions(n, k, iterations=3, step=10, plot=False, path=""):
    """
    Benchmarks the classical algorithm for generalized parity games using a random game arenas generator.
    Arenas size 1 to n, each with k priority functions are solved.
    :param n: number of nodes in generated graph.
    :param k: number of priority functions in the generated graph.
    :param iterations: number of times the algorithm is timed (default is 3).
    :param step: step to be taken in the generation.
    :param plot: if True, plots the data using matplotlib.
    :param path: path to the file in which to write the result.
    """

    y = []  # list for the time recordings
    n_ = []  # list for the x values

    total_time = 0  # accumulator to record total time

    nbr_generated = 0  # conserving the number of generated mesures (used to get the index of a mesure)

    chrono = timer.Timer(verbose=False)  # Timer object

    info = "Time to solve"  # info about the current benchmark

    # print first line of output
    print(u"Generator".center(40) + "|" + u"Nodes (n)".center(12) + "|" + info.center(40) + "\n" + \
          "-" * 108)

    # games generated are size 1 to n
    for i in range(2, n + 1, step):
        g = generators.random_generalized(i, k, i, 1, (i / 2))
        temp = []
        # #iterations calls to the solver are timed
        for j in range(iterations):
            with chrono:
                generalized_parity_solver(g)  # solver call
            temp.append(chrono.interval)  # add time recording

        min_recording = min(temp)
        y.append(min_recording)  # get the minimum out of #iterations recordings
        n_.append(i)
        total_time += min_recording

        print("Random graphs".center(40) + "|" + str(i).center(12) + "|" \
              + str(y[nbr_generated]).center(40) + "\n" + "-" * 108)

        nbr_generated += 1  # updating the number of generated mesures

        # at the end, print total time
    print("-" * 108 + "\n" + "Total time".center(40) + "|" + "#".center(12) + "|" + \
          str(total_time).center(40) + "\n" + "-" * 108 + "\n")

    if plot:
        plt.grid(True)
        plt.title(u"Random graph of size 1 to " + str(n)+" with "+str(k)+" priority functions")
        plt.xlabel(u'number of nodes')
        plt.ylabel(u'time (s)')
        points, = plt.plot(n_, y, 'g.', label=u"Execution time")
        plt.legend(loc='upper left', handles=[points])
        plt.savefig(path)
        plt.clf()
        plt.close()

def benchmark_random_n_nodes(n, k, iterations=3, step=10, plot=False, path=""):
    """
    Benchmarks the classical algorithm for generalized parity games using a random game arenas generator.
    Arenas of size n with 1 to k priority functions are solved.
    :param n: number of nodes in generated graph.
    :param k: number of priority functions in the generated graph.
    :param iterations: number of times the algorithm is timed (default is 3).
    :param step: step to be taken in the generation.
    :param plot: if True, plots the data using matplotlib.
    :param path: path to the file in which to write the result.
    """

    y = []  # list for the time recordings
    n_ = []  # list for the x values

    total_time = 0  # accumulator to record total time

    nbr_generated = 0  # conserving the number of generated mesures (used to get the index of a mesure)

    chrono = timer.Timer(verbose=False)  # Timer object

    info = "Time to solve"  # info about the current benchmark

    # print first line of output
    print(u"Generator".center(40) + "|" + u"Nodes (n)".center(12) + "|" + info.center(40) + "\n" + \
          "-" * 108)

    # games generated are size 1 to n
    for i in range(2, k + 1, step):
        g = generators.random_generalized(n, i, n, 1, n/2)
        temp = []
        # #iterations calls to the solver are timed
        for j in range(iterations):
            with chrono:
                generalized_parity_solver(g)  # solver call
            temp.append(chrono.interval)  # add time recording

        min_recording = min(temp)
        y.append(min_recording)  # get the minimum out of #iterations recordings
        n_.append(i)
        total_time += min_recording

        print("Random graph".center(40) + "|" + str(i).center(12) + "|" \
              + str(y[nbr_generated]).center(40) + "\n" + "-" * 108)

        nbr_generated += 1  # updating the number of generated mesures

        # at the end, print total time
    print("-" * 108 + "\n" + "Total time".center(40) + "|" + "#".center(12) + "|" + \
          str(total_time).center(40) + "\n" + "-" * 108 + "\n")

    if plot:
        plt.grid(True)
        plt.title(u"Random graph of size " + str(100)+" with 1 to "+str(k)+" priority functions")
        plt.xlabel(u'number of nodes')
        plt.ylabel(u'time (s)')
        points, = plt.plot(n_, y, 'g.', label=u"Execution time")
        plt.legend(loc='upper left', handles=[points])
        plt.savefig(path)
        plt.clf()
        plt.close()

def benchmark_worstcase_n_nodes(n, k, iterations=3, step=10, plot=False, path=""):
    """
    Benchmarks the classical algorithm for generalized parity games using the worst case game arenas generator.
    Arenas are the arenas of the worst case for the recursive algorithm for parity games, generalized with k functions
    :param n: number of nodes in generated graph.
    :param k: number of priority functions in the generated graph.
    :param iterations: number of times the algorithm is timed (default is 3).
    :param step: step to be taken in the generation.
    :param plot: if True, plots the data using matplotlib.
    :param path: path to the file in which to write the result.
    """

    y = []  # list for the time recordings
    n_ = []  # list for the x values

    total_time = 0  # accumulator to record total time

    nbr_generated = 0  # conserving the number of generated mesures (used to get the index of a mesure)

    chrono = timer.Timer(verbose=False)  # Timer object

    info = "Time to solve"  # info about the current benchmark

    # print first line of output
    print(u"Generator".center(40) + "|" + u"Nodes (n)".center(12) + "|" + info.center(40) + "\n" + \
          "-" * 108)

    # games generated are size 1 to n
    for i in range(1, n, step):
        g = generators.strong_parity_worst_case(i)  # generated game
        g = generators.multiple_priorities(g,k)

        temp = []
        # #iterations calls to the solver are timed
        for j in range(iterations):
            with chrono:
                generalized_parity_solver(g)  # solver call
            temp.append(chrono.interval)  # add time recording

        min_recording = min(temp)
        y.append(min_recording)  # get the minimum out of #iterations recordings
        n_.append(i)
        total_time += min_recording

        print("Worst-case graph".center(40) + "|" + str(i).center(12) + "|" \
              + str(y[nbr_generated]).center(40) + "\n" + "-" * 108)

        nbr_generated += 1  # updating the number of generated mesures

        # at the end, print total time
    print("-" * 108 + "\n" + "Total time".center(40) + "|" + "#".center(12) + "|" + \
          str(total_time).center(40) + "\n" + "-" * 108 + "\n")

    if plot:
        plt.grid(True)
        plt.title(u"Worst-case graph of size 1 to " + str(n)+" with 1 to "+str(k)+" priority functions")
        plt.xlabel(u'number of nodes')
        plt.ylabel(u'time (s)')
        points, = plt.plot(n_, y, 'g.', label=u"Execution time")
        plt.legend(loc='upper left', handles=[points])
        plt.savefig(path)
        plt.clf()
        plt.close()

#benchmark_worstcase_n_nodes(100, 3, iterations=3, step=1, plot=True, path="generalized-worst-up100n-3k-10s.pdf")

#benchmark_random_k_functions(200, 3, iterations=3, step=10, plot=True, path="generalized-random-up100n-3k-10s.pdf")
