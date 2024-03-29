class Nodo:
    def __init__(self, valor):
        self.info = valor
        self.arcos = []

    def enlace(self, ndestino, peso=1, bdir=False):
        if (type(ndestino) == type(self)):
            arco = Arco(ndestino, peso)
            self.arcos.append(arco)
            if (bdir == True):
                arco = Arco(self, peso)
                ndestino.arcos.append(arco)
            return True
        return False

    def mostra_enlaces(self):
        for arco in self.arcos:
            print
            arco.nodo.info,
            print
            arco.peso

    def existe_enlace(self, ndestino):
        for arco in self.arcos:
            if (arco.nodo == ndestino):
                return arco
        return False

    def eli_enlace(self, ndestino):
        arco = self.existe_enlace(ndestino)
        if (arco != False):
            self.arcos.remove(arco)
            return True
        return False

    def __del__(self):
        del self.arcos


class Arco:
    def __init__(self, ndestino, peso=0):
        self.nodo = ndestino
        self.peso = peso


class Grafo:
    def __init__(self, dirigido=True):
        self.__nodos = []
        self.__dirigido = dirigido

    def buscaNodo(self, valor):
        for nodo in self.__nodos:
            if (nodo.info == valor):
                return nodo
        return False

    def enlace(self, valOrigen, valDestino, peso=1, bdir=False):

        norigen = self.buscaNodo(valOrigen)
        if (not (norigen)):
            return False

        ndestino = self.buscaNodo(valDestino)
        if (not (ndestino)):
            return False

        if (self.__dirigido == False):
            bdir = True

        norigen.enlace(ndestino, peso, bdir)
        return True

    def ins_nodo(self, valor):
        if (self.buscaNodo(valor) == False):
            nodo = Nodo(valor)
            self.__nodos.append(nodo)
            return nodo
        return False

    def eli_nodo(self, valor):
        nodoE = self.buscaNodo(valor)
        if (nodoE == False):
            return False

        for nodo in self.__nodos:
            nodo.eli_enlace(nodoE)

        self.__nodos.remove(nodoE)
        return True

    def existen_islas(self):
        for nodo in self.__nodos:
            if (len(nodo.arcos) == 0):
                esIsla = True
                for norigen in self.__nodos:
                    if (norigen.existe_enlace(nodo) != False):
                        esIsla = False
                        break

                if (esIsla == True):
                    return True
        return False

    def elimina_bucles(self):
        for nodo in self.__nodos:
            if nodo.existe_enlace(nodo):
                nodo.eli_enlace(nodo)

    def existe_caminho(self, valOrigen, valDestino, camino=[]):

        nOrigen = self.buscaNodo(valOrigen)
        nDestino = self.buscaNodo(valDestino)
        if (nOrigen == False or nDestino == False):
            return False

        camino.append(valOrigen)
        if (nOrigen.existe_enlace(nDestino) != False):
            camino.append(valDestino)
            return True

        for arco in nOrigen.arcos:
            if (arco.nodo.info in camino):
                continue

            if (self.existe_caminho(arco.nodo.info, valDestino, camino)):
                return True
            camino.pop()

        return False

    def sub_grafo(self, *valores):
        sg = Grafo()

        for valOrigen in valores:
            nOrigen = self.buscaNodo(valOrigen)
            if (nOrigen != False):
                sg.ins_nodo(nOrigen.info)

        for valOrigen in valores:
            nOrigen = self.buscaNodo(valOrigen)
            if (nOrigen == False):
                continue

            for arco in nOrigen.arcos:
                if (arco.nodo.info in valores):
                    sg.enlace(nOrigen.info, arco.nodo.info)

        return sg

    def arco_maior_camino(self, valOrigen, valDestino, camino=[], mayor=None):

        nOrigen = self.buscaNodo(valOrigen)
        nDestino = self.buscaNodo(valDestino)
        if (nOrigen == False or nDestino == False):
            return False

        if (len(camino) == 0):
            mayor = Arco()

        camino.append(valOrigen)
        arco = nOrigen.existe_enlace(nDestino)
        if (arco):
            camino.append(valDestino)
            if (arco.peso > mayor.peso):
                mayor = arco

            pos = camino.index(mayor.nodo.info) - 1
            return True, camino[pos], mayor.nodo.info

        for arco in nOrigen.arcos:
            if (arco.nodo.info in camino):
                continue

            if (arco.peso > mayor.peso):
                mayor = arco

            enc, vi, vf = self.arco_maior_camino(arco.nodo.info, valDestino, camino, mayor)
            if (enc == True):
                return True, vi, vf
            camino.pop()

        return False, None, None

    def __str__(self):
        grafo = ""
        for nodo in self.__nodos:
            grafo = grafo + nodo.info
            arcos = ""
            for arco in nodo.arcos:
                if (arcos != ""):
                    arcos = arcos + ", "
                arcos = arcos + arco.nodo.info + ":" + str(arco.peso)
            grafo = grafo + "(" + arcos + ") "
        return grafo