## Comparison between Fringe search and Dijkstra

![GHA workflow badge](https://github.com/roosahut/tiralabra/workflows/CI/badge.svg)

This is a project for the Datastructures and Algorithms project course in the University of Helsinki.

The goal is to compare two shortest path algorithms, Fringe search and Dijkstra. The original plan was to compare IDA* and Dijkstra but I changed it because IDA* was not working well for the massive graph from OpenStreetMap that I'm using in this project.

### How to use

The original plan was to deploy the app to fly.io, and I did it, but the app uses more memory than the free version of fly allows, so I most likely won't be doing that.

But happily you can run the app locally too, and it doesn't take much.

First you'll need to clone this repository.

Then to run the app on localhost:8000 first you'll need to do this from the root.

Move to the backend folder (where there is also a build of the frontend):
```bash
cd backend
```
Then you'll need to install poetry depedencies.
```bash
poetry install
```
And then run the app with
```bash
poetry run start
```
The app should open on localhost:8000 !

The app works like this:
The app works only in Helsinki, so click anywhere in Helsinki, and a marker will appear there, that is your starting point. Then click another place (still in Helsinki) and that is the goal place.
You'll have to wait a bit, but the app will give you a route between the given points. It displays the route dijkstra has counted in red and the fringe search route in blue (note that they might be the same so it might only show blue). 
After the routes have shown up you can choose another points in Helsinki and see the route between them.

I will be adding another features to the frontend but so far that is all there is.
I also don't have tests yet which is a problem and will be the next thing I'm doing.

### Documentation

[Definition document](https://github.com/roosahut/tiralabra/blob/main/documentation/definitiondocument.md)

### Weekly reports

[Week 1](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport1.md)

[Week 2](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport2.md)

[Week 3](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport3.md)

[Week 4](https://github.com/roosahut/tiralabra/blob/main/documentation/weeklyreports/weeklyreport4.md)
