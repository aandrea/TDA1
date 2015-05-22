#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from linkedlist import LkdList

INF = sys.maxint

class Graph(object):
    def __init__(self):
        self.nodes = LkdList()
        self.nodesNmb = 0
        self.edges = LkdList()
        self.edgesNmb = 0
   
    def addNode(self, ID, name):
        node = Node(ID, name)
        self.nodes.insertLast(node)
        self.nodesNmb += 1
        return node
 
#Ojo: como no es digrafo por cada arista addEdge se ejecuta 2 veces
    def addEdge(self, node1, node2, weight=1):
        edge = Edge(node1, node2, weight)
        node1.addEdge(edge) #agrego a la lista de adyacentes del nodo
        self.edges.insertLast(edge) #agrego a la lista de aristas del grafo
        self.edgesNmb += 1

    def getNodeNumber(self):
        return self.nodesNmb

    def getEdgeNumber(self):
        return self.edgesNmb

    def minPathsFrom(self, sourceNode):

        self.resetVisited(self.nodes)
        sourceNode.visited = True
        levelCount = 0
        levels = LkdList()
        
        firstPath = LkdList() #camino es una lista de nodos
        firstPath.insertLast(sourceNode)

        pathsTo = {}
        self.initializePathsToNodes(pathsTo) 
        pathsTo[sourceNode].insertLast(firstPath) # caminos a nodo fuente

        levels.insertLast(firstPath) #LO #Levels es una lista con listas de nodos en un nivel como elemento

        currents = firstPath #lista de nodos

        while currents : 

            nextLevel = LkdList()

            for current in currents:
                for edge in current.getEdges():
                    if edge.node2.visited == False :

                        for path in pathsTo[current]:
                            auxPath = path #listas de nodos..
                            auxPath.insertLast(edge.node2)
                            pathsTo[edge.node2].insertLast(auxPath)

                            if edge.node2 not in nextLevel:
                                nextLevel.insertLast(edge.node2)

            self.setVisited(nextLevel)
            currents = nextLevel
            levels.insertLast(nextLevel)

            levelCount +=1
        
        return levels, pathsTo, levelCount

    def resetVisited(self, nodesList):
        for node in nodesList:
            node.visited = False

    def setVisited(self, nodesList):
        for node in nodesList:
            node.visited = True

    def initializePathsToNodes(self, pathsTo):
        for node in self.nodes:
            pathsTo[node]= LkdList()


    def __str__(self):
        s = ""
        for node in self.nodes:
            e = "("
            for edge in node.getEdges():
                e += edge.node2.name + ";"
            s += node.name + ":" + e + ")" + "\n"
        return s.strip()




class Node(object):
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        #self.parent = None
        self.distance = INF
        self.visited = False
        self.edges = LkdList()
    
    def addEdge(self, edge):
        self.edges.insertLast(edge)
   
    def getEdges(self):
        return self.edges

class Edge(object):
    def __init__(self, node1, node2, weight=1):
        self.weight = weight
        self.node1 = node1
        self.node2 = node2

