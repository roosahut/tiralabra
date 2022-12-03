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