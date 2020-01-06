import parameter_learning as pe
import dataset_gen as dg
import numpy as np
import bayesian_net
import matplotlib.pyplot as plt
import csv


def average(values):
    sum = 0
    for i in range(len(values)):
        sum += values[i]
    avg = sum / len(values)
    return avg


def main():
    # Costruisce la rete bayesiana e carica i file necessari convertendoli in matrici numpy
    bayesian_network = bayesian_net.BayesianNetwork(5)
    adjacency_matrix = np.loadtxt("CANCER/matrix.txt", dtype='i', delimiter=' ')
    p_array = np.loadtxt("CANCER/probabilities.txt", delimiter=',')
    bayesian_network.set_matrix(adjacency_matrix)
    nodes = bayesian_network.get_nodes()
    prob = []  # array di array
    prob_file = open('CANCER/prob_dataset.csv', 'rt')
    prob_reader = csv.reader(prob_file, delimiter=',')
    for i in range(len(nodes)):
        row = next(prob_reader)
        r_prob = np.zeros(len(row))
        for j in range(len(row)):
            r_prob[j] = row[j]
        prob.append(r_prob)

    x = []
    y = []
    tries = 10
    start = 10
    end = 1011
    iter = 100
    for n in range(start, end, iter):
        x.append(n)
        y_tries = []
        for j in range(tries):
            dataset = dg.dataset_gen(n, adjacency_matrix, nodes, prob)
            y_tries.append(pe.parameter_learning(nodes, p_array, dataset, n))
        y.append(average(y_tries))

    print("x: ", x)
    print("y: ", y)
    plt.title("Learning Curve Jensen-Shennon Divergency")
    plt.xlabel("Dimensione dataset (n)")
    plt.ylabel("Distanza tra p e qn")
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()
