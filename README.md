# Parameter-Learning-Bayesian-Network
Data una rete bayesiana e (le probabilità condizionate dei nodi di tale rete) il programma genera un dataset casuale con un numero n di tuple via via crescente. Usando tali dataset vengono ricavati i parametri che vengono poi confrontati con le probabilità iniziali attraverso la divergenza di Jensen-Shennon. Per ogni n vengono fatte 10 generazioni di dataset e di esse viene presa la media della divergenza per evitare casi particolari. Infine i risultati vengono salvati in un vettore y e visualizzati su un grafo per formare una learning curve.

bayesian_net.py:

        - La classe Node rappresenta i nodi della rete. Per ogni nodo si ha un valore, l'array dei valori dei nodi genitori, colore e tempo di scoperta finale, i quali servono per la visita in profondità per fare l'ordinamento topologico dei nodi
        - La classe BayesianNetwork crea la rete Bayesiana. Con il metodo set_matrix viene settata la matrice degli archi
        
dataset_gen.py:

        - Contiene la funzione dataset_gen che crea un dataset generando un numero casuale e confrontandolo con il valore corretto nel file delle probabilità condizionate
  
dfs_order.py:
  
        - Esegue la visita in profondità dei nodi della rete, scoprendoli via via e settando il loro tempo di scoperta finale, con il quale vengono poi ordinati in modo topologico
       
parameter_learning.py:
        
        - il metodo parameter_learning calcola gli Nij-Nijk servendosi del metodo parents_configuration per calcolare le j configurazioni possibili dei nodi genitori del nodo i-esimo, e del dataset generato. Vengono poi calcolati i parametri usando aijk = 1 e aij = 2 (Laplace Smoothing). 
        
        - i parametri trovati vengono confrontati con le probabilità iniziali usando il metodo jensen_shannon_divergency
 
 main.py:
        
         - in particolare viene usato come esempio una rete Bayesiana chiamata CANCER, con 5 nodi e 4 archi. Per ogni rete servono 3 files: matrix.txt (contiene la matrice di adiacenza della rete); probabilities.txt (contiene le probabilità di ogni nodo condizionate dalle probabilità dei genitori); prob_dataset.csv (contiene il valore delle probabilità della prima configurazione di ogni nodo date le possibili configurazioni dei genitori per generare il dataset)
         
         - per ogni grandezza del dataset n vengono fatte 10 prove e presa la media dei risultati delle divergenze di Jensen-Shannon. In particolare per la rete CANCER si parte da n=10 fino a n = 1011 con passo 100. I risultati vengono salvati in un vettore y, mentre il numero dei nodi in un vettore x. Viene infine visualizzata la learning curve attraverso l'uso della liberia matplot
