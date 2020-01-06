import math
import numpy as np
import itertools as iter


def precisione_di_macchina():
    eps = 1
    while eps + 1 > 1:
        eps /= 2
    return eps


def jensen_shannon_divergence(p_array, qn_array):
    s1 = 0
    s2 = 0
    for i in range(len(qn_array)):
        if p_array[i] == 0:
            p_array[i] = precisione_di_macchina()
        s1 += p_array[i] * math.log((p_array[i]) / (0.5 * (p_array[i] + qn_array[i])))
        s2 += qn_array[i] * math.log((qn_array[i] / (0.5 * (p_array[i] + qn_array[i]))))
    js = s1 + s2
    return js


def parents_configuration(nparents):
    configuration = []
    for i in iter.product([0, 1], repeat=nparents):
        configuration.append(i)
    return configuration


def parameter_learning(nodes, p_array, dataset, n):
    # Laplace Smoothing
    aijk = 1
    aij = 2

    # Costruzione degli Nij e degli Nijk
    Nij_array = []
    Nijk_array = []
    for i in range(len(nodes)):
        # Calcola le configurazioni dei nodi genitori
        config = parents_configuration(len(nodes[i].get_parents()))
        parents = nodes[i].get_parents()
        tmp_Nij = []
        tmp1_Nijk = []
        for j in range(2**len(parents)):
            count_ij = 0
            tmp2_Nijk = np.zeros(2)
            for l in range(n):
                match = True
                for m in range(len(parents)):
                    # per ogni genitore guarda nel dataset se il valore corrisponde al valore della j-esima config.
                    if (dataset[l])[parents[m]] != config[j][m]:
                        match = False
                        break
                if match:
                    # Conta per ogni valore di k quante volte compare la config j-esima dei genitori
                    tmp2_Nijk[int(dataset[l][i])] += 1
            tmp1_Nijk.append(tmp2_Nijk)
            tmp_Nij.append(sum(tmp2_Nijk))  # Somma gli Nijk per fare Nij
        # Per ogni nodo i inserisce gli Nij-Nijk
        Nijk_array.append(tmp1_Nijk)
        Nij_array.append(tmp_Nij)

    # Usando gli Nij-Nijk e gli aij-aijk trova i parametri
    qn_array = []
    for i in range(len(nodes)):
        parents = nodes[i].get_parents()
        for j in range(2**len(parents)):
            for k in range(2):
                qn_array.append((aijk + Nijk_array[i][j][k]) / (aij + Nij_array[i][j]))
    return jensen_shannon_divergence(p_array, qn_array)
