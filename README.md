## Comparison between Fringe search and Dijkstra

![GHA workflow badge](https://github.com/roosahut/tiralabra/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/roosahut/tiralabra/branch/main/graph/badge.svg?token=HY1aerZ5ob)](https://codecov.io/gh/roosahut/tiralabra)

This is a project for the Datastructures and Algorithms project course in the University of Helsinki.

The goal is to compare two shortest path algorithms, Fringe search and Dijkstra. The original plan was to compare IDA* and Dijkstra but I changed it because IDA* was not working well for the massive graph from OpenStreetMap that I'm using in this project.

The backend is done with python and for the API I used is pythons FastAPI. The frontend is done with React.js and for the map I used React-leaflet.
The map data is downloaded with pythons OSMNX library which can download data from OpenStreetMap. This app uses the map data (a graph) of Helsinki. You can find out how to use the app in the [user guide](https://github.com/roosahut/tiralabra/blob/main/documentation/user_guide.md).

### Documentation

[Definition document](https://github.com/roosahut/tiralabra/blob/main/documentation/definitiondocument.md)

[User guide](https://github.com/roosahut/tiralabra/blob/main/documentation/user_guide.md)

### Weekly reports

[Week 1](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport1.md)

[Week 2](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport2.md)

[Week 3](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport3.md)

[Week 4](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport4.md)
