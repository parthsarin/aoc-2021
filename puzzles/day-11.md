## \--- Day 11: Dumbo Octopus ---

You enter a large cavern full of rare bioluminescent [dumbo
octopuses](https://www.youtube.com/watch?v=eih-VSaS2g0)! They seem to not like
the Christmas lights on your submarine, so you turn them off for now.

There are 100 octopuses arranged neatly in a 10 by 10 grid. Each octopus
slowly gains _energy_ over time and _flashes_ brightly for a moment when its
energy is full. Although your lights are off, maybe you could navigate through
the cave without disturbing the octopuses if you could predict when the
flashes of light will happen.

Each octopus has an _energy level_ \- your submarine can remotely measure the
energy level of each octopus (your puzzle input). For example:

    
    
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    

The energy level of each octopus is a value between `0` and `9`. Here, the
top-left octopus has an energy level of `5`, the bottom-right one has an
energy level of `6`, and so on.

You can model the energy levels and flashes of light in _steps_. During a
single step, the following occurs:

  * First, the energy level of each octopus increases by `1`.
  * Then, any octopus with an energy level greater than `9` _flashes_. This increases the energy level of all adjacent octopuses by `1`, including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than `9`, it _also flashes_. This process continues as long as new octopuses keep having their energy level increased beyond `9`. (An octopus can only flash _at most once per step_.)
  * Finally, any octopus that flashed during this step has its energy level set to `0`, as it used all of its energy to flash.

Adjacent flashes can cause an octopus to flash on a step even if it begins
that step with very little energy. Consider the middle octopus with `1` energy
in this situation:

    
    
    Before any steps:
    11111
    19991
    19191
    19991
    11111
    
    After step 1:
    34543
    4 _000_ 4
    5 _000_ 5
    4 _000_ 4
    34543
    
    After step 2:
    45654
    51115
    61116
    51115
    45654
    

An octopus is _highlighted_ when it flashed during the given step.

Here is how the larger example above progresses:

    
    
    Before any steps:
    5483143223
    2745854711
    5264556173
    6141336146
    6357385478
    4167524645
    2176841721
    6882881134
    4846848554
    5283751526
    
    After step 1:
    6594254334
    3856965822
    6375667284
    7252447257
    7468496589
    5278635756
    3287952832
    7993992245
    5957959665
    6394862637
    
    After step 2:
    88 _0_ 7476555
    5 _0_ 89 _0_ 87 _0_ 54
    85978896 _0_ 8
    84857696 _00_
    87 _00_ 9 _0_ 88 _00_
    66 _000_ 88989
    68 _0000_ 5943
    _000000_ 7456
    9 _000000_ 876
    87 _0000_ 6848
    
    After step 3:
    _00_ 5 _0_ 9 _00_ 866
    85 _00_ 8 _00_ 575
    99 _000000_ 39
    97 _000000_ 41
    9935 _0_ 8 _00_ 63
    77123 _00000_
    791125 _000_ 9
    221113 _0000_
    _0_ 421125 _000_
    _00_ 21119 _000_
    
    After step 4:
    2263 _0_ 31977
    _0_ 923 _0_ 31697
    _00_ 3222115 _0_
    _00_ 41111163
    _00_ 76191174
    _00_ 53411122
    _00_ 4236112 _0_
    5532241122
    1532247211
    113223 _0_ 211
    
    After step 5:
    4484144 _000_
    2 _0_ 44144 _000_
    2253333493
    1152333274
    11873 _0_ 3285
    1164633233
    1153472231
    6643352233
    2643358322
    2243341322
    
    After step 6:
    5595255111
    3155255222
    33644446 _0_ 5
    2263444496
    2298414396
    2275744344
    2264583342
    7754463344
    3754469433
    3354452433
    
    After step 7:
    67 _0_ 7366222
    4377366333
    4475555827
    34966557 _0_ 9
    35 _00_ 6256 _0_ 9
    35 _0_ 9955566
    3486694453
    8865585555
    486558 _0_ 644
    4465574644
    
    After step 8:
    7818477333
    5488477444
    5697666949
    46 _0_ 876683 _0_
    473494673 _0_
    474 _00_ 97688
    69 _0000_ 7564
    _000000_ 9666
    8 _00000_ 4755
    68 _0000_ 7755
    
    After step 9:
    9 _0_ 6 _0000_ 644
    78 _00000_ 976
    69 _000000_ 8 _0_
    584 _00000_ 82
    5858 _0000_ 93
    69624 _00000_
    8 _0_ 2125 _000_ 9
    222113 _000_ 9
    9111128 _0_ 97
    7911119976
    
    After step 10:
    _0_ 481112976
    _00_ 31112 _00_ 9
    _00_ 411125 _0_ 4
    _00_ 811114 _0_ 6
    _00_ 991113 _0_ 6
    _00_ 93511233
    _0_ 44236113 _0_
    553225235 _0_
    _0_ 53225 _0_ 6 _00_
    _00_ 3224 _0000_
    

After step 10, there have been a total of `204` flashes. Fast forwarding, here
is the same configuration every 10 steps:

    
    
    After step 20:
    3936556452
    56865568 _0_ 6
    449655569 _0_
    444865558 _0_
    445686557 _0_
    568 _00_ 86577
    7 _00000_ 9896
    _0000000_ 344
    6 _000000_ 364
    46 _0000_ 9543
    
    After step 30:
    _0_ 643334118
    4253334611
    3374333458
    2225333337
    2229333338
    2276733333
    2754574565
    5544458511
    9444447111
    7944446119
    
    After step 40:
    6211111981
    _0_ 421111119
    _00_ 42111115
    _000_ 3111115
    _000_ 3111116
    _00_ 65611111
    _0_ 532351111
    3322234597
    2222222976
    2222222762
    
    After step 50:
    9655556447
    48655568 _0_ 5
    448655569 _0_
    445865558 _0_
    457486557 _0_
    57 _000_ 86566
    6 _00000_ 9887
    8 _000000_ 533
    68 _00000_ 633
    568 _0000_ 538
    
    After step 60:
    25333342 _00_
    274333464 _0_
    2264333458
    2225333337
    2225333338
    2287833333
    3854573455
    1854458611
    1175447111
    1115446111
    
    After step 70:
    8211111164
    _0_ 421111166
    _00_ 42111114
    _000_ 4211115
    _0000_ 211116
    _00_ 65611111
    _0_ 532351111
    7322235117
    5722223475
    4572222754
    
    After step 80:
    1755555697
    59655556 _0_ 9
    448655568 _0_
    445865558 _0_
    457 _0_ 86557 _0_
    57 _000_ 86566
    7 _00000_ 8666
    _0000000_ 99 _0_
    _0000000_ 8 _00_
    _0000000000_
    
    After step 90:
    7433333522
    2643333522
    2264333458
    2226433337
    2222433338
    2287833333
    2854573333
    4854458333
    3387779333
    3333333333
    
    After step 100:
    _0_ 397666866
    _0_ 749766918
    _00_ 53976933
    _000_ 4297822
    _000_ 4229892
    _00_ 53222877
    _0_ 532222966
    9322228966
    7922286866
    6789998766
    

After 100 steps, there have been a total of `_1656_` flashes.

Given the starting energy levels of the dumbo octopuses in your cavern,
simulate 100 steps. _How many total flashes are there after 100 steps?_

Your puzzle answer was `1620`.

The first half of this puzzle is complete! It provides one gold star: *

## \--- Part Two ---

It seems like the individual flashes aren't bright enough to navigate.
However, you might have a better option: the flashes seem to be
_synchronizing_!

In the example above, the first time all octopuses flash simultaneously is
step `_195_`:

    
    
    After step 193:
    5877777777
    8877777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    7777777777
    
    After step 194:
    6988888888
    9988888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    8888888888
    
    After step 195:
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    _0000000000_
    

If you can calculate the exact moments when the octopuses will all flash
simultaneously, you should be able to navigate through the cavern. _What is
the first step during which all octopuses flash?_

Answer:

Although it hasn't changed, you can still [get your puzzle input](11/input).

You can also [Shareon
[Twitter](https://twitter.com/intent/tweet?text=I%27ve+completed+Part+One+of+%22Dumbo+Octopus%22+%2D+Day+11+%2D+Advent+of+Code+2021&url=https%3A%2F%2Fadventofcode%2Ecom%2F2021%2Fday%2F11&related=ericwastl&hashtags=AdventOfCode)
[Mastodon](javascript:void\(0\);)] this puzzle.

