# Setting up for AOC

Before starting these instructions, make sure you have the correct packages installed. All of my packages are stored in `requirements.txt`, but I was sloppy and you might not need all of those 😊

1. Make sure you've got the config information stored in `solutions/config.py`. That file should export the `session` variable, which contains the session key for AOC.
2. Copy `solutions/template.py` to `solutions/day-#.py` and update the `DAY` and `YEAR` variables at the top.
3. When the competition opens, run `$ python day-#.py`. If you do it before the competition opens, it'll say that the input is currently locked. If you don't see that line, the file has downloaded the input to `inputs/day-#.txt`. Be sure to enter `n` so that you don't accidentally submit `None` as your answer.
4. Solve the problem as normal, setting `ans_1` to the answer for part 1. Once that submission is successful, the script will download the markdown for part 2 and store it as `puzzles/day-#.md`. Use that to see the puzzle for part 2 and solve it!

If you want to see the ranks, you can run `ipython -i utils.py` in the solutions folder to load the utilities into a python interpreter session and then run

```python
get_rank(day=4, year=2021)
# => RankInfo(time_1='00:09:55', rank_1=189, time_2='00:16:06', rank_2=311)
```

(of course, replace the day with the correct day number)
