# User guide


### How the app works

The app will show you a map centered in Helsinki. You can choose which algorithm (or both) you want to use to count the route in the panle above the map. Then you can click anywhere in Helsinki and a marker will appear there: that is the starting point. Then click again in Helsinki to choose the goal point. It might take a while (please wait patiently), but the route/routes will appear there. In the panel it will also show how many meters the route is and how long did the algorithm take to count the route.

To try other start and end points just click on the map again (you can also change the algorithm).

The first path-finding after opening the map might take longer because on that the app will download the massive graph.

Dijkstra is the red line and Fringe search is the blue.

### How to use

The original plan was to deploy the app to fly.io, and I did it, but the app uses more memory than the free version of fly.io allows, so I decided not to do it.

But, thankfully, the app is easy to use locally too. You only need to do these following things:

First you'll need to clone this repository.

Then to run the app on localhost:8000 in web you'll need to do these steps from the root.

Install poetry depedencies
```bash
poetry install
```
Go to the poetry shell
```bash
poetry shell
```
And then run the app with
```bash
poetry run invoke start
```
Then go to [localhost:8000](http://localhost:8000), and there it is! Remember to keep the terminal window open. HOX!! Lately the app hasn't started rigth after starting the app and the terminal shows an error, but it will work when you refresh the browser a few times :)

I know that right now I have the build of the frontend on GitHub and use it with that (even though that is not the best practise). I did that because I wanted to ensure that the people doing peer reviews on this project can start it even when they don't have npm installed on their computers.
