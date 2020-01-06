import dfs_order as dfs
import numpy as np
import random


def dataset_gen(n, adjacency_matrix, nodes, prob):
    dataset = np.zeros((n, len(nodes)))
    # viene usata la visita in profondità per l'ordinamento topologico dei nodi
    ordered_array = dfs.order(adjacency_matrix, nodes)
    for i in range(n):  # per ogni riga del dataset
        for j in range(len(ordered_array)):  # per ogni nodo (colonne)
            v = random.random()
            # se il nodo non ha genitori
            if len(prob[int(ordered_array[j])]) == 1:
                if v <= prob[int(ordered_array[j])]:
                    dataset[i, int(ordered_array[j])] = 0
                else:
                    dataset[i, int(ordered_array[j])] = 1
            # se il nodo ha genitori
            else:
                index = 0
                parents = nodes[j].get_parents()
                # calcola l'indice in base al valore dei genitori, per trovare la probabilità corrispondente
                for k in range(len(parents)):
                    index += dataset[i, parents[k]] * (2**k)
                if v <= prob[int(ordered_array[j])][int(index)]:  # probabilities è un array di array
                    dataset[i, int(ordered_array[j])] = 0
                else:
                    dataset[i, int(ordered_array[j])] = 1
    return dataset
