# Test Document

## Unit tests
You can see the unit test coverage percent and how it's divided in [![codecov](https://codecov.io/gh/roosahut/tiralabra/branch/main/graph/badge.svg?token=HY1aerZ5ob)](https://codecov.io/gh/roosahut/tiralabra).

I have only done unit testing on the backend/src file, since the frontend is done with React and it's basically part of the UI.

I also don't include the backend/data, because it only has code that loads data with OSMNX library (which is already tested) and the actual graph data.

From backend/src I excluded main.py and api.py, because those are part of the UI too, and use the FastAPI and uvicorn packages. I also excluded the index.py
because it only uses functions from the other parts of the application logic that I have tested and are a part of the coverage. index.py also uses one function of the OSMNX library 
(the one that get the nearest nodes from a given graph when it's given a wanted latitude and longitude), since that is also a part of the OSMNX library which is already tested, I don't see a point in testing that.

Obliviosly I don't test the build in backend/src since it's only the build version of the frontend.

## Performance testing

Dijkstra finds the shortest path always. Fringe search does too, most of the time, but there are times when sometimes it gives a route that is longer than Dijkstra's. There is probably some problem with the algorithm, but it's the best implementation of Fringe Search I could do. As I said, it works right most of the time, and the closer the two points are to each other, the surer it is that it will work right.

Here is a graph showing how much time both algorithms took when given same start and goal points. 

![timecomparison](https://github.com/roosahut/tiralabra/blob/main/documentation/pictures/timecomparison.png)

As you can see, Fringe Search is faster when the distance is shorter, but gets a lot slower when the distance gets bigger.

Dijkstra stays mostly the same, because it visits all the nodes everytime, and only once, when Fringe Search might go over the same ones many times.

## Doing the tests

After installing the poetry depedencies (poetry install), you can run the unit tests like this:
```bash
poetry shell
```
and then
```bash
poetry run invoke test
```

You can view the unit test coverage by clicking the codecov badge.
