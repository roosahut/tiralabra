**Programming language:** Python 

**Language of the documentation:** English (also capable of doing peer reviews in Finnish)

Tietojenkäsittelytieteen kandidaatti

## Topic
- In this project I will be comparing ~~Iterative Deepening A* (IDA*)~~ Fringe Search algorithm and Dijkstra algorithm on their efficiency on finding the shortest path. 
- I had to change the algortihm midway the project because IDA* just didn't work well because the graph is massive and cyclic.
- The goal is to visualize a map and find the shortest path between two points (nodes) that the user will give as inputs, the path will be also visualized on the map. 
- I will be using OpenStreetMap to get the data of the nodes.

## Time and space complexity
- Time complexity of IDA* is O(n^d) where n is the branching factor and d is the depth of the shallowest goal node. Space complexity of IDA* is O(d).
- Time complexity of Dijkstra is O(n + m log m) where n is the number of nodes and m is the number of edges. The space complexity of Dijkstra is O(n2).
- The information on Fringe Search is very limited, so I wasn't able to find out what its time and space complexities are suppoused to be.


[Fringe search article](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf)