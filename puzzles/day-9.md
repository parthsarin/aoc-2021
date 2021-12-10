## \--- Day 9: Smoke Basin ---

These caves seem to be [lava tubes](https://en.wikipedia.org/wiki/Lava_tube).
Parts are even still volcanically active; small hydrothermal vents release
smoke into the caves that slowly settles like rain.

If you can model how the smoke flows through the caves, you might be able to
avoid it and be that much safer. The submarine generates a heightmap of the
floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the
following heightmap:

    
    
    2 _1_ 9994321 _0_
    3987894921
    98 _5_ 6789892
    8767896789
    989996 _5_ 678
    

Each number corresponds to the height of a particular location, where `9` is
the highest and `0` is the lowest a location can be.

Your first goal is to find the _low points_ \- the locations that are lower
than any of its adjacent locations. Most locations have four adjacent
locations (up, down, left, and right); locations on the edge or corner of the
map have three or two adjacent locations, respectively. (Diagonal locations do
not count as adjacent.)

In the above example, there are _four_ low points, all highlighted: two are in
the first row (a `1` and a `0`), one is in the third row (a `5`), and one is
in the bottom row (also a `5`). All other locations on the heightmap have some
lower adjacent location, and so are not low points.

The _risk level_ of a low point is _1 plus its height_. In the above example,
the risk levels of the low points are `2`, `1`, `6`, and `6`. The sum of the
risk levels of all low points in the heightmap is therefore `_15_`.

Find all of the low points on your heightmap. _What is the sum of the risk
levels of all low points on your heightmap?_

Your puzzle answer was `500`.

The first half of this puzzle is complete! It provides one gold star: *

## \--- Part Two ---

Next, you need to find the largest basins so you know what areas are most
important to avoid.

A _basin_ is all locations that eventually flow downward to a single low
point. Therefore, every low point has a basin, although some basins are very
small. Locations of height `9` do not count as being in any basin, and all
other locations will always be part of exactly one basin.

The _size_ of a basin is the number of locations within the basin, including
the low point. The example above has four basins.

The top-left basin, size `3`:

    
    
    _21_ 99943210
    _3_ 987894921
    9856789892
    8767896789
    9899965678
    

The top-right basin, size `9`:

    
    
    21999 _43210_
    398789 _4_ 9 _21_
    985678989 _2_
    8767896789
    9899965678
    

The middle basin, size `14`:

    
    
    2199943210
    39 _878_ 94921
    9 _85678_ 9892
    _87678_ 96789
    9 _8_ 99965678
    

The bottom-right basin, size `9`:

    
    
    2199943210
    3987894921
    9856789 _8_ 92
    876789 _678_ 9
    98999 _65678_
    

Find the three largest basins and multiply their sizes together. In the above
example, this is `9 * 14 * 9 = _1134_`.

_What do you get if you multiply together the sizes of the three largest
basins?_

Answer:

Although it hasn't changed, you can still [get your puzzle input](9/input).

You can also [Shareon
[Twitter](https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Smoke+Basin%22+%2D+Day+9+%2D+Advent+of+Code+2021&url=https%3A%2F%2Fadventofcode%2Ecom%2F2021%2Fday%2F9&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void\(0\);)] this puzzle.

