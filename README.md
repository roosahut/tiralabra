## Comparison between Fringe search and Dijkstra

This is a project for the Datastructures and Algorithms project course in the University of Helsinki.

The goal is to compare two shortest path algorithms, Fringe search and Dijkstra. The original plan was to compare IDA* and Dijkstra but I changed it because IDA* was not working well for the massive graph from OpenStreetMap that I'm using in this project.

### How to use

I will de deploying the project to fly.io but right now you can use the app locally.

First you'll need to clone this repository.

Then to run backend firts you'll need to run these commmands in the root of the repo:
```bash
poetry install
```
```bash
poetry run python3 backend/src/main.py
```
This will open the backend in localhost:8000.

And then to run the frontend open another treminal and go to the frontend folder and run these commands:
```bash
npm install
```
```bash
npm start
```
This will open the frontend in localhost:3000.

The app works like this:
So far the app works only in Helsinki, so click anywhere in Helsinki, and a marker will appear there, that is your starting point. Then click another place (still in Helsinki) and that is the goal place.
You'll have to wait a bit, but the app will give you a route between the given points. It displays the route dijkstra has counted in red and the fringe search route in blue (note that they might be the same so it might only show blue). 
After the routes have shown up you can choose another points in Helsinki and see the route between them.

I will be adding another features to the frontend but so far that is all there is.

### Documentation

[Definition document](https://github.com/roosahut/tiralabra/blob/main/documentation/definitiondocument.md)

### Weekly reports

[Week 1](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport1.md)

[Week 2](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport2.md)

[Week 3](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport3.md)

[Week 4](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport4.md)
