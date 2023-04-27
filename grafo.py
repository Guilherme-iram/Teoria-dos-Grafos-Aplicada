#Criação da classe Grafo
class Graph:
    def __init__(self, adjacency_matrix, adjacency_list):
        self.adjacency_matrix = adjacency_matrix
        self.adjacency_list = adjacency_list
    
    def __len__(self):
        return len(self.adjacency_list)

    def get_matrix(self):
        
        n = len(self.adjacency_matrix)
        matriz = []
        for i in range(n):
            linha = []
            for j in range(n):
                linha.append(self.adjacency_matrix[i][j])
            matriz.append(linha)

        return matriz


def read_graph(graph_txt):
    # le o tamanho do grafo
    len_graph = int(graph_txt[0])
    
    # cria uma matriz nxn sendo n o total de vértices diferentes do grafo
    adjacency_matrix = [[None] * len_graph for i in range(len_graph)]
    # cria uma lista de listas que correspondem aos vizinhos adjacentes de cada vértice
    adjacency_list = [[] for i in range(len_graph)]

    for i, line in enumerate(graph_txt):
        
        # ignora a primeira linha do txt
        if i == 0:
            continue
        # converte cada linha numerada do grafo enumerado em lista de inteiros binários
        line_graph = [int(c) for c in line.split()] 
        # atribui essa lista de inteiro a cada linha da matriz de adjacencia
        adjacency_matrix[i - 1] = line_graph
        
        # atribui cada vértice vizinho ao seu vértice correspondente 
        for j in range(len_graph):
            if (line_graph[j] == 1):
                adjacency_list[i - 1].append(j + 1)
                
    return adjacency_matrix, adjacency_list