from decimal import Decimal

# Clase para el nodo
class Nodo:
    def __init__(self, nodo):
        self.nodo = nodo

# Clase para el vertice
class Vertice:
    def __init__(self, v_nodo, longitud):
        self.v_nodo = v_nodo
        self.longitud = longitud


# Clase para el grafo
class Grafo:
    def __init__(self):
        self.nodos = set()
        self.vertices = dict()

    def agregar_nodo(self, nodo):
        self.nodos.add(nodo)

    def agregar_vertice(self, d_nodo, v_nodo, longitud):
        vertice = Vertice(v_nodo, longitud)
        if d_nodo.nodo in self.vertices:
            d_nodo_vertices = self.vertices[d_nodo.nodo]
        else:
            self.vertices[d_nodo.nodo] = dict()
            d_nodo_vertices = self.vertices[d_nodo.nodo]
        d_nodo_vertices[v_nodo.nodo] = vertice

# Distancia entre los nodos
def distancia(d, dist):
    distancia = None
    for nodo in d:
        if distancia == None:
            distancia = nodo
        elif dist[nodo] < dist[distancia]:
            distancia = nodo

    return distancia


INFINITY = Decimal('Infinity')

# Algoritmo de djkstra
def djkstra(g, s):
    d = set()
    dist = {}
    prev = {}

    for v in g.nodos:
        dist[v] = INFINITY
        prev[v] = INFINITY
        d.add(v)

    dist[s] = 0

    while d:
        u = distancia(d, dist)
        d.remove(u)

        if u.nodo in g.vertices:
            for _, v in g.vertices[u.nodo].items():
                alt = dist[u] + v.longitud
                if alt < dist[v.v_nodo]:
                    dist[v.v_nodo] = alt
                    prev[v.v_nodo] = u

    return dist, prev


# Array de los nodos
def arreglo(prev, d_nodo):
    prev_nodo = prev[d_nodo]
    ruta = [d_nodo.nodo]
    while prev_nodo != INFINITY:
        ruta.append(prev_nodo.nodo)
        temp = prev_nodo
        prev_nodo = prev[temp]

    ruta.reverse()
    return ruta

# Agregando los nodos del ejercicio
grafo = Grafo()
nodo_a = Nodo("A")
grafo.agregar_nodo(nodo_a)
nodo_b = Nodo("B")
grafo.agregar_nodo(nodo_b)
nodo_c = Nodo("C")
grafo.agregar_nodo(nodo_c)
nodo_d = Nodo("D")
grafo.agregar_nodo(nodo_d)
nodo_e = Nodo("E")
grafo.agregar_nodo(nodo_e)
nodo_f = Nodo("F")
grafo.agregar_nodo(nodo_f)
nodo_g = Nodo("G")
grafo.agregar_nodo(nodo_g)
nodo_h = Nodo("H")
grafo.agregar_nodo(nodo_h)
nodo_i = Nodo("I")
grafo.agregar_nodo(nodo_i)
nodo_j = Nodo("J")
grafo.agregar_nodo(nodo_j)
nodo_k = Nodo("K")
grafo.agregar_nodo(nodo_k)
nodo_l = Nodo("L")
grafo.agregar_nodo(nodo_l)
nodo_m = Nodo("M")
grafo.agregar_nodo(nodo_m)


# Agregando los vertices o distancia que hay entre los nodos prev y dist
grafo.agregar_vertice(nodo_a, nodo_b, 2)
grafo.agregar_vertice(nodo_b, nodo_a, 2)

grafo.agregar_vertice(nodo_a, nodo_e, 2)
grafo.agregar_vertice(nodo_e, nodo_a, 2)

grafo.agregar_vertice(nodo_b, nodo_e, 1)
grafo.agregar_vertice(nodo_e, nodo_b, 1)

grafo.agregar_vertice(nodo_b, nodo_h, 1)
grafo.agregar_vertice(nodo_h, nodo_b, 1)

grafo.agregar_vertice(nodo_b, nodo_c, 3)
grafo.agregar_vertice(nodo_c, nodo_b, 3)

grafo.agregar_vertice(nodo_b, nodo_i, 1)
grafo.agregar_vertice(nodo_i, nodo_b, 1)

grafo.agregar_vertice(nodo_c, nodo_i, 2)
grafo.agregar_vertice(nodo_d, nodo_c, 2)

grafo.agregar_vertice(nodo_d, nodo_i, 2)
grafo.agregar_vertice(nodo_i, nodo_d, 2)

grafo.agregar_vertice(nodo_d, nodo_j, 2)
grafo.agregar_vertice(nodo_j, nodo_d, 2)

grafo.agregar_vertice(nodo_d, nodo_m, 2)
grafo.agregar_vertice(nodo_m, nodo_d, 2)

grafo.agregar_vertice(nodo_e, nodo_f, 1)
grafo.agregar_vertice(nodo_f, nodo_e, 1)

grafo.agregar_vertice(nodo_e, nodo_g, 2)
grafo.agregar_vertice(nodo_g, nodo_e, 2)

grafo.agregar_vertice(nodo_e, nodo_h, 2)
grafo.agregar_vertice(nodo_h, nodo_e, 2)

grafo.agregar_vertice(nodo_f, nodo_g, 2)
grafo.agregar_vertice(nodo_g, nodo_f, 2)

grafo.agregar_vertice(nodo_g, nodo_h, 2)
grafo.agregar_vertice(nodo_h, nodo_g, 2)

grafo.agregar_vertice(nodo_g, nodo_i, 3)
grafo.agregar_vertice(nodo_i, nodo_g, 3)

grafo.agregar_vertice(nodo_g, nodo_k, 3)
grafo.agregar_vertice(nodo_k, nodo_g, 3)

grafo.agregar_vertice(nodo_h, nodo_i, 2)
grafo.agregar_vertice(nodo_i, nodo_h, 2)

grafo.agregar_vertice(nodo_k, nodo_l, 2)
grafo.agregar_vertice(nodo_l, nodo_k, 2)

grafo.agregar_vertice(nodo_k, nodo_i, 2)
grafo.agregar_vertice(nodo_i, nodo_k, 2)

grafo.agregar_vertice(nodo_l, nodo_i, 1)
grafo.agregar_vertice(nodo_i, nodo_l, 1)

grafo.agregar_vertice(nodo_l, nodo_j, 2)
grafo.agregar_vertice(nodo_j, nodo_l, 2)

grafo.agregar_vertice(nodo_l, nodo_m, 1)
grafo.agregar_vertice(nodo_m, nodo_l, 1)

grafo.agregar_vertice(nodo_i, nodo_j, 2)
grafo.agregar_vertice(nodo_j, nodo_i, 2)

grafo.agregar_vertice(nodo_m, nodo_j, 1)
grafo.agregar_vertice(nodo_j, nodo_m, 1)

# Desde el nodo_g se puede llegar a los siguientes nodos:
dist, prev = djkstra(grafo, nodo_g)

print("La ruta mas rapida desde {} hasta {} es: [{}] con una distancia de {}".format(
    nodo_g.nodo,
    nodo_a.nodo,
    " -> ".join(arreglo(prev, nodo_a)), str(dist[nodo_a]))
)
