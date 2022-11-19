# Weekly report 3

Time spent: 14h

### What I did

I was suppoused to get the IDA star working this week and start the tests but I got exited about learning to use the react-leaflet and actually crete a working 
app so I got carried away. I created a frontend with React and Leaflet and a backend with Python's FastAPI. So far on the react app you can pick too points that will
show up as markers and then the backend will count the shortest path between those points with the dijkstras algo I did last week. 
I also downloaded the graph of Helsinki from openstreetmap with the osmnx library so that it doesn't have to be downloaded every time.
So far the app can count routes in Helsinki, and I'm thinking about leaving it with that, because already that graph is massive.

I plan on deploying the app on fly.io when it's ready enough.
So far you can test it by cloning this repo and then typing: poetry install and then starting the backend with: poetry run python backend/main.
The frontend you can start with going to frontend and typing: npm install and then: npm start

I know I was suppoused to start the tests already but I got carried away so that will be the first thing I do next week.
But overall I'm happy because now it's much easier to visualize the paths.

### What I learned

I learned a lot about react-leaflet and fastapi, since it was my first time using fastapi and leaflet.

### What was hard

The hardest part was getting everything with leaflet work, but it all worked out anyway.

### What will I do next

Next week I will start with the tests, and I will probably change the multi networkx graph I'm using now to my own graph model so the algorithms will be easier to test.
I will also try to get the IDA* actually work next week.
