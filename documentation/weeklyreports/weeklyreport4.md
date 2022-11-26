# Weekly report 4

Time spent: 11h

### What I did

This week I spent over 5 hours trying to get the IDA* work until I realized that it actually worked if the distance wasn't too long. That's what made me question if it's gonna work at all with my graph.
So I decided to make a fringe search algorithm instead. I got it to work so now I'm quite happy because the biggest stress about the project is now done.

I was suppoused to, once again, begin doing the tests, but I ran out of time. I did make my own graph and node objects though, so now testing everything will be a lot easier.

I also made everything work with my own graph object instead of the networkx multigraph and that took quite a lot of time.

### What I learned

I learned a lot about the fringe search algorithm which was completely new to me. I was afraid I wouldn't be able to make it work, but since I knew how A* and IDA* worked it wasn't that hard to understand after reading the article given in the course material about fringe search.

### What was hard

Working with the IDA* was very hard, but now it's thankfully over. Understanding the fringe search was hard at first but once I got it it actually made sense.

### What will I do next

I said the same last week, but next week I will definitely start the tests. Since now everything works with my own graph, it will be must easier. I will also start doing docstring next week on the code.