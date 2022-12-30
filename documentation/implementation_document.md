# Implementation document

## Structure

The basic structure of the app is divided tpo frontend and backend, since the UI is a web app.

There is nothing that special about the fronend, it's basically a basic React app created by create-react-app.

The backend has two directories: src and data. Data has the massive graph of Helsinki loaded with OSMNX from OpenStreetMap.

Source (src) has all the application logic and the API. (It also has the build of the frontend so the app can be used with one terminal only.)

### Basically everything works like this:

The user clicks on two wanted points in the map and the frontend sends the API a POST request and gives it params of the 2 points in latitude and longitude. 

The api/route POST route calls for the get_shortest_path function which is located in the index.py file. That functions loads the graph of the helsinki stored in pickle format and then uses OSMNX to find the nodes from the map that are the closest to the given latitude and longitude. 

Then it creates the Graph -object from the Networkx.MultiGraph format (OSMNX loads map data in that format).
then the function calls for the Dijkstra and Fringe search algorithms to get the shortest paths and the costs of those paths. Since the algorithm gives the paths in nodes, the function calls for the function that changes the path of nodes to a path of latlng.

The function returns the routes to the api.py POST route which return the routest back to frontend. Then the routes are displayed to the React-leaflet map.

## Comparing the two algorithms

After spending a lot of time on this projects and trying both algorithms in the map, I'll have to say that Dijkstra does seem to be better for this project. It is a lot more consistent in time and always gives either the same path as Fringe Search or a faster one. That means that Fringe Search does not work right always. I'm not really sure why, since the algorithm was very hard, and I don't have a lot of information about it.

It seems that Fringe Search is faster when the distance is short (just like IDA* is), but it gets unsure when the distance grows. It does get the same path as Dijkstra on bigger distances too sometimes, but it is must lower. Just like this graph comparing the time it took both algorithms on certain start and goals points (when fringe search showed the right path):

![timecomparison](https://github.com/roosahut/tiralabra/blob/main/documentation/pictures/timecomparison.png)

Dijkstra is true to its time and space complexities (time O(n + m log m) and space O(n2)), as the time it takes is always around same. It visits every node of the graph, and keeps track of them, and that shows in its space complexity.

Fringe search does seem to be a lot slower (on bigger distances), but its space complexity is a lot better. It borrows the idea of IDA* and keeps its space saving features. It travels only the current frontier at once. IDA* didn't work at all on my graph, which shows that Fringe Search is more effective that it in huge cyclic graphs. But it does seem like when the amount of edges is greater, Fringe Search also gets slower, just like IDA* didn't work at all.

The best possible algorithm for this project would have been A*, but testing these different algorithms really gave me a lot of insight into the world of path-finding algos. Fringe Search was hard, but I'm really glad I tried it.

## Projects possible shortcomings and proposals for improvement

I feel like I knew too little about Fringe Search, so I'm not entirely sure if I got it working exactly how it's suppoused to work. But to be honest I'm also happy with how it's working right now, because I couldn't get IDA* working at all, because the graph was too big and cyclic for it.

Sometimes Fringe Search gets the same path Dijkstra does, but it takes it alot more time. Not once has Fringe search got a shorter path, it's always the same or longer than Dijkstras. I don't know if the problem is with my implementation or if the algorithm just doesn't work that well with big cyclic graphs (like IDA*).

It would have been interesting to see how A* compares with both of these algorithms, since it's very close to both of them.

## Sources

[Fringe search article](https://webdocs.cs.ualberta.ca/~holte/Publications/fringe.pdf)
