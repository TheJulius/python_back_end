class Grafo:
    def __init__(self):
        self.__nodos = []
        self.__matriz = []

    def buscaNodo(self, valor):
        if (valor in self.__nodos):
            return self.__nodos.index(valor)
        return -1

    def ins_nodo(self, valor):
        if (self.buscaNodo(valor) < 0):
            self.__nodos.append(valor)
            self.__matriz.append({})
            return True
        return False

    def ins_arco(self, valOrigen, valDestino, peso=1):
        posOrigen = self.buscaNodo(valOrigen)
        posDestino = self.buscaNodo(valDestino)
        if (posOrigen >= 0 and posDestino >= 0):
            self.__matriz[posOrigen][valDestino] = peso
            return True
        return False


    def mostrar_nodos(self):
        i = 0
        for nodo in self.__nodos:
            print
            i, nodo
            i = i + 1


    def mostrar_arcos(self, valor):
        posOrigen = self.buscaNodo(valor)
        if (posOrigen < 0):
            return False

        for valDestino in self.__matriz[posOrigen]:
            peso = self.__matriz[posOrigen][valDestino]
            print
            valDestino, peso
        return True


    def existe_arco(self, valOrigen, valDestino):
        posOrigen = self.buscaNodo(valOrigen)
        posDestino = self.buscaNodo(valDestino)
        if (posOrigen >= 0 and posDestino >= 0):
            if (valDestino in self.__matriz[posOrigen]):
                return True
        return False


    def elimina_nodo(self, valOrigen):
        posOrigen = self.buscaNodo(valOrigen)
        del self.__nodos[posOrigen]
        del self.__matriz[posOrigen]

        for arcos in self.__matriz:
            if (valOrigen in arcos):
                del arcos[valOrigen]

    def existen_islas(self):
        pos = 0
        for arcos in self.__matriz:
            if (len(arcos) == 0):
                valDestino = self.__nodos[pos]

                esIsla = True
                posNodo = 0
                for valNodo in self.__nodos:
                    if (valDestino in self.__matriz[posNodo]):
                        esIsla = False
                    posNodo = posNodo + 1

                if (esIsla == True) or (self.existe_arco(valNodo, valNodo)):
                    return True

            pos = pos + 1
        return False

    def existe_caminho(self, valOrigen, valDestino):

        posOrigen = self.buscaNodo(valOrigen)
        posDestino = self.buscaNodo(valDestino)
        if (posOrigen < 0 or posDestino < 0):
            return False

        try:
            self.__caminho.append(valOrigen)
        except AttributeError:
            self.__caminho = [valOrigen]

        if (valDestino in self.__matriz[posOrigen]):
            return True

        for valNodo in self.__matriz[posOrigen]:
            if (valNodo in self.__caminho):
                continue
            if (self.existe_caminho(valNodo, valDestino)):
                return True
            self.__caminho.pop()

        return False

    def no_dirigido(self):

        posOrigen = 0
        for valOrigen in self.__nodos:
            for valDestino in self.__matriz[posOrigen]:
                peso = self.__matriz[posOrigen][valDestino]
                self.ins_arco(valDestino, valOrigen, peso)

            posOrigen = posOrigen + 1

    def elimina_bucle(self):
        posOrigen = 0
        for valOrigen in self.__nodos:
            for valDestino in self.__matriz[posOrigen]:
                if (valOrigen == valDestino):
                    del self.__matriz[posOrigen][valDestino]
                    break

            posOrigen = posOrigen + 1

    def mostrar_estrutura_grafo(self):
        print
        self.__nodos
        print
        self.__matriz


# MAIN

g = Grafo()
g.ins_nodo("A")
g.ins_nodo("B")
g.ins_nodo("C")
g.ins_nodo("D")
g.ins_nodo("E")

g.ins_arco("A", "B")
g.ins_arco("A", "C", 3)
g.ins_arco("A", "A", 1)
g.ins_arco("A", "D", 1)
g.ins_arco("B", "A")
g.ins_arco("C", "B")
g.ins_arco("C", "D")
g.ins_arco("D", "E")

g.mostrar_estrutura_grafo()

print
"Nodos"
g.mostrar_nodos()

print
"arcos de A"
g.mostrar_arcos("A")

print
"Existe arco de A a B", g.existe_arco("A", "B")
print
"Existe arco de A a E", g.existe_arco("A", "E")

print
"Existe Caminho de A a E", g.existe_caminho("A", "E")
print
"Existe Caminho de B a E", g.existe_caminho("B", "E")

print
"Existen Islas", g.existen_islas()
g.elimina_nodo("D")
g.mostrar_estrutura_grafo()