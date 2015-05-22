#!/usr/bin/python
# -*- coding: utf-8 -*-


from graph import Graph, Node

class Parser(object):
 
    def __init__(self):
        self.wordSplitter = ',' 
        self.graph = None      
    
    def parse(self, nf, graph):
        
        networkFile = open(nf, 'r')
        self.graph = graph
        people = self._parsePeople(networkFile)
        self._parseFriendships(networkFile, people)        
        return graph
    
    def _parsePeople(self, networkFile):
        people = {}
        # read first line (i.e. nodedef>name VARCHAR,label VARCHAR,sex VARCHAR,locale VARCHAR,agerank INT)
        line = networkFile.readline().strip()
        line = networkFile.readline().strip()

        while(line):  # loop blank line or EOF            
            person = line.split(self.wordSplitter)
            personNode = self.graph.addNode( person[0], person[1])
            people[person[0]] = personNode #me guardo puntero al nodo de la persona... para agregar las aristas después        
            line = networkFile.readline().strip()

        return people



    def _parseFriendships(self, networkFile, people):

        # read first line (i.e. edgedef>node1 VARCHAR,node2 VARCHAR)
        line = networkFile.readline().strip()
        line = networkFile.readline().strip()        

        while(line):  #until EOF
            friendship = line.split(self.wordSplitter)
            person1 = people[friendship[0]]
            person2 = people[friendship[1]]
            self.graph.addEdge(person1, person2)
            self.graph.addEdge(person2, person1)
            line = networkFile.readline().strip()
        return


