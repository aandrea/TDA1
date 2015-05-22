#!/usr/bin/python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from parser import Parser
from graph import Graph
from stats import Stats

def main():

    filename = sys.argv[1]

    graph = Graph()
    parser = Parser()

    #parse gdf file
    parser.parse(filename, graph)
#    print graph.__str__()

    stats = Stats(graph)

    #compute popularity
    popularities = stats.computePopularity()
    print "Popularidad"
    print "********************************"
    stats.showPopularities(popularities)

    #compute influences
    influences = stats.computeInfluences()
    print ""
    print "Influencias"
    print "********************************"
    stats.showInfluences(influences)

    #obtain recomendations
    print ""
    print "Recomendaciones"
    print "********************************"
    recommendations = stats.computeRecommendations()
    stats.showRecommendations(recommendations)

if __name__ == "__main__":
    main()
