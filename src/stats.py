#!/usr/bin/python
# -*- coding: utf-8 -*-

from linkedlist import LkdList
from graph import Graph, Node


class Popularity(object):
    def __init__(self):
        self.name = 0
        self.friendsNmb = 0 #cantidad de amigos

    def __lt__(self, other):
        return self.friendsNmb < other.friendsNmb

    def __le__(self, other):
        return self.friendsNmb <= other.friendsNmb

    def __ge__(self, other):
        return self.friendsNmb >= other.friendsNmb

class Stats(object):
    def __init__(self, graph):
        self.graph = graph

    def computePopularity (self):

        popularities = LkdList()

        for node in self.graph.nodes : 
            popularity = Popularity()
            popularity.name = node.name 
            popularity.friendsNmb = node.edges.length
            popularities.insertSortedInverse(popularity)
        return popularities

    def showPopularities (self, popularities):
        for pop in popularities:
            print pop.name +": ", pop.friendsNmb 


    def computeInfluences(self):
        influences = {}
        self.initializeInfluences(influences)

        for node in self.graph.nodes :
#            print "Calculando caminos mínimos desde nodo", node.name
            levels, minPaths, levelCount = self.graph.minPathsFrom(node)
#            print "Caminos mínimos encontrados: ", len(minPaths.keys())
#            print "Actualizando influencias", node.name
            self.updateInfluences(levels, minPaths, levelCount, influences)

        return influences

    
    def updateInfluences(self, levels, minPaths, levelCount, influences):
        auxInfluences = {}
        self.initializeInfluences(auxInfluences)
        i=0

#       while (i <= levelCount):
        for level in levels:
            if i>1 : 
                for node in level:

                    paths = minPaths[node] #lista de caminos(que son listas de nodos)
                    pathsCount = paths.length
    #                print "pathsCount: ", pathsCount
                    
                    if pathsCount >0:
                        for path in paths:
                            stepCount = 0
                            pathLen= path.length

                            for step in path: #cada step es un nodo..
                                if stepCount>0 and stepCount<(pathLen -1) :
                                    auxInfluences[step] +=1
                                stepCount+=1
                            
                                            
                    for key in auxInfluences:
                        influences[key] += auxInfluences[key] / pathsCount
            i+=1


    def initializeInfluences(self, influences):
        for node in self.graph.nodes:
            influences[node]= 0.0

    def showInfluences (self, influences):

        for node, influence in influences.items():
            print node.name + ": ", influence


    def computeRecommendations(self):
        recommendations = {}

        for node in self.graph.nodes :
            friendsIC, recNode = self.calculateRecommendationFor(node)
            recommendations[node] = (recNode, friendsIC)
        return recommendations


    def calculateRecommendationFor(self, node):
#        print "calculando recomendaciones para :", node.name
        nodeFriends = LkdList()

        for edge in node.getEdges():
            nodeFriends.insertLast(edge.node2)

        friendsInCommon = 0
        recommendedNode = None
             
        for otherNode in self.graph.nodes:
            if node <> otherNode and otherNode not in nodeFriends:
                friendsCount=0
                for otherEdge in otherNode.getEdges():
                    if otherEdge.node2 in nodeFriends : 
                        friendsCount+=1
                if friendsCount > friendsInCommon :
                    friendsInCommon = friendsCount
                    recommendedNode = otherNode

        return friendsInCommon, recommendedNode

    def showRecommendations (self, recommendations):

        for node, recommendation in recommendations.items():
            line = node.name
            line+= ": "
            if recommendation[0] :
                line+= recommendation[0].name 
                line+= "("
                line += `recommendation[1]`
                line+=" amigos en común)"
            else:
                line+= "no hay recomendaciones"

            print line
#            print node.name + ": ", recommendation[0].name +"(",recommendation[1]+"amigos en común)"


