import copy

import networkx as nx

from database.DAO import DAO

class Model:
    def __init__(self):
        self.idMap={}
        self.grafo=nx.Graph()
        self.bestCosto=0
        self.solBest=[]

    def getOptPath(self,n):
        self.solBest=[]
        self.bestCosto=0
        self.ricorsione([],n)
        return self.solBest,self.bestCosto

    def buildGraph(self, country,anno):
        self.grafo.clear()
        allNodes=DAO.getRetailers(country)
        for n in allNodes:
            self.idMap[n.Retailer_code]=n
        self.grafo.add_nodes_from(allNodes)
        allEdges=DAO.getArchi(country,anno)
        for e in allEdges:
            r1=self.idMap[e[0]]
            r2=self.idMap[e[1]]
            peso=e[2]
            self.grafo.add_edge(r1,r2,weight=peso)


    def getPesoVicini(self):
        diz={}
        for n in self.grafo.nodes():
            somma=0
            for v in self.grafo.neighbors(n):
                somma+=self.grafo[n][v]["weight"]
            diz[n]=somma
        dizOrdinato=sorted(diz.items(), key=lambda item: item[1], reverse=True)
        return dizOrdinato


    def getCountry(self):
        return DAO.getCountry()

    def getYear(self):
        return DAO.getYear()

    def getNumNodes(self):
        return self.grafo.number_of_nodes()

    def getNumEdges(self):
        return self.grafo.number_of_edges()

    def calcolaCosto(self,parziale):
        for n in self.grafo.nodes():
            if n in parziale:
                somma=0
                for v in self.grafo[n]:
                    if v in parziale:
                somma+=self.grafo[n][v]["weight"]
    def ricorsione(self,parziale,n):

        if len(parziale)-1==n:
            if self.calcolaCosto(parziale) > self.bestCosto:
                self.solBest=copy.deepcopy(parziale)
                self.bestCosto=self.calcolaCosto(parziale)

        else:
            for n in self.grafo.nodes():
                if n not in parziale:
                    parziale.append(n)
                    self.ricorsione(parziale,n)
                    parziale.pop()





