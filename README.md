# [Advent of Code, 2021](https://adventofcode.com/2021)

![](https://img.shields.io/badge/day%20📅-9-blue)
![](https://img.shields.io/badge/stars%20⭐-16-yellow)

## Day 1 (7918/6466)

Day 1 was a solitary adventure, though I hope others will join in soon. Nobody really missed much -- the puzzles today were pretty straightforward and solved entirely in two lines in the interactive interpreter. Only 2,000 lines, so efficiency wasn't a big deal.

A solid start to a hopefully fun holiday season.

— Parth


## Day 2 (2268/2040)

Michael joined in, but Unicornelius was a bit late to the party. Submarine adventures - solved in ~6 mins, at a rank of ~2000. Very impressed by how quickly everyone solves these things.

— Unicornelius (and Michael)

## Day 3 (1935/1863)

We've got a full team by now! Yasmine, Michael, Unicornelius, and Parth are all in. We fiddled around with some `numpy` magic for the first one, but ended up using it mostly for the `sum` function to count the number of 1s in a column. Part 2 was really finnicky. The edge case where the number of 1s is equal to the number of 0s prevented us from using the `min` and `max` functions. We also got confused a bit between the oxygen vs co2 rules (filter on the most or least occurring value).

It all worked out and our rank has been improving: despite 26 minutes on part 2, we got our best rank (1863) so far. Still no leaderboard, but it's possible we'll hit something soon.

— Parth

## Day 4 (189/311)
Great day! We managed to track sub-400 placements for both part 1 and part 2. We had a lot of success
today creating a class to represent the `Bingo` board and making use of Python's features. 

The leaderboard is in sight!

— Yasmine

## Day 5 (1218/1277)

This was a rough day, just in terms of the solving process (even though our rank went down since last time, I don't think that's a huge mark on progress since it's still monotonic improvement from day 3). We made two big missteps, I think

1. We stored a dictionary mapping points `(x, y)` to the number of times they were visited. Then, we counted the number of times each point was visited more than twice like this:

   ```python
   ans = 0
   for k, v in d:
       if v >= 2:
           ans += 1 
   ```

   Super subtle, but do you see the bug? It's just going over `d`, which is `d.keys()` as an iterable, so `k` is the `x` coordinate and `v` is the `y` coordinate. Neither of them are the number of times visited.

2. We (I) read too quickly and didn't realize the lines had slope ±1. This sent us down a rabbithole trying to calculate if a point was on a line with this function:

    ```python
    def is_on_line(p, x1, x2, y1, y2):
        x, y = p

        # test entire line
        m = float(y2 - y1) / float(x2 - x1)
        b = y1 - m * x1
        on_line = y == m * x + b

        # in bounds?
        in_bounds = x1 <= x <= x2 and y1 <= y <= y2
        return on_line and in_bounds
    ```

    It was much simpler, and we rerouted quickly.

— Parth

## Day 6 (417/452)

Today was an adventure in fish breeding. Maybe I should go into fish farming.

Successful day though - onward and upward!

— Michael

## Day 7 (188/744)

Missing Michael today, though we did go up in rank to achieve our best yet. 

Top 100 is in reach.

— Yasmine

## Day 8 (51/617)

Missing Yasmine today, but we did manage to break the leaderboard! 51 on part 1, answered in just over 3 minutes! Honestly, the problem wasn't too difficult but the reading took a while. I think we managed to just slide in there.

I'm still quite proud of our 617 rank on part 2, where the real substance of the problem was. For each line, we're basically searching for a pairing between the letters "fake" a–g and the "true" letters a–g. We're guaranteed that there is exactly one pairing which works. But, there are 7! such pairings. We can't just brute force it, so we're going to use a clever trick.

> **Edit**: Turns out we *could* just brute force it (and most solutions did just that). But we were fancy 😎

We started by reducing the number of pairings based on the length of each number. If the "fake" word has two letters, we can narrow the possible pairings down to those which map those two letters to either `e` or `f`. Applying this, we narrowed the search space considerably—down to 8 dictionaries for each line! 

> **Technical detail**: At this point, we were expressing the search space as a dictionary which mapped the fake letters to all possible true letters it could be after the length-pruning. For example, it started as
> 
> ```python
> candidates = {
>     'a': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
>     'b': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
>     'c': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
>     'd': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
>     'e': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
>     'f': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
>     'g': {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
> }
> ```
> 
> And then if we saw the word `"ab"` we narrowed to
> 
> ```python
> candidates = {
>     'a': {'c', 'f'},
>     'b': {'c', 'f'},
>     'c': {'a', 'b', 'd', 'e', 'g'},
>     'd': {'a', 'b', 'd', 'e', 'g'},
>     'e': {'a', 'b', 'd', 'e', 'g'},
>     'f': {'a', 'b', 'd', 'e', 'g'},
>     'g': {'a', 'b', 'd', 'e', 'g'},
> }
> ```
> 
> (actually we didn't even take out `c`, `f` but that's not important)

Finally, we used recursion to get a list of all possible pairings from this search space and... we just tried them! We ran into a sneaky return statement bug which made us rethink life.

We can get the leaderboard again for sure! Or as Michael would say, "straight path to the leaderboard" 😉

— Parth
