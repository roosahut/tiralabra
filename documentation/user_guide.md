# User guide


### How the app works

The app will show you a map centered in helsinki. The routing works only in Helsinki, so click anywhere in Helsinki, and a marker will appear there: that is your starting point. Then click another place (still in Helsinki) and that is the goal place.
You'll have to wait a bit, but the app will give you a route between the given points. It displays the route dijkstra has calculated in red and the fringe search route in blue (note that they might be the same so it might only show blue). 
After the routes have shown up you can choose another points in Helsinki and see the route between them.

I will be adding another features to the frontend but so far that is all there is.

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
Then go to localhost:8000 (web), and there it is! Remember to keep the terminal window open.
