"""
File: utils.py
--------------

Contains utilities for AOC.
"""
import config
import requests
from datetime import date
import os
from sys import argv
import re
from typing import List
try:
    import termcolor
except ImportError:
    termcolor = None

today = date.today()
year = today.year
start = date(year, 11, 29)
day_idx = (today - start).days

cookies = {
    'session': config.session
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': f'https://adventofcode.com/{year}/day/{day_idx}',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'TE': 'trailers',
}


def cprint(
        msg: str, 
        color: str = 'white', 
        attrs: List[str] = [],
        end: str = '\n'
    ) -> None:
    """
    Prints a message to the console.

    Arguments
    ---------
    msg -- The message to print.
    color -- The color to print the message in.
    attrs -- The attributes to print the message in.
    end -- The end of the message.
    """
    if termcolor:
        termcolor.cprint(msg, color, attrs=attrs, end=end)
    else:
        print(msg, end=end)


def get_input(
        day: int = day_idx, 
        year: int = year,
        write: bool = False,
    ) -> str:
    """
    Returns the input for the current day.

    Arguments
    ---------
    write -- Whether to write the input to a file.
    day -- The day to get the input for.
    year -- The year to get the input for.
    """
    if (year == today.year) and os.path.exists(f'../inputs/day-{day}.txt'):
        with open(f'../inputs/day-{day}.txt', 'r') as f:
            return f.read().strip()

    r = requests.get(
        f'https://adventofcode.com/{year}/day/{day}/input',
        headers=headers, cookies=cookies
    )
    data = r.text

    if "don't repeatedly request this endpoint before it unlocks!" in data:
        print("Input is locked. Wait until midnight Eastern.")
        return None

    if write:
        with open(f'../inputs/day-{day}.txt', 'w') as f:
            f.write(data)

        os.chmod(f'../inputs/day-{day}.txt', 0o777)
    
    return data


def get_puzzle(
        day: int = day_idx, 
        year: int = year
    ):
    """
    Returns the puzzle for the current day.

    Arguments
    ---------
    day -- The day to get the puzzle for.
    year -- The year to get the puzzle for.

    Returns
    -------
    The text of the puzzle (possibly cleaned) for the current day.
    """
    r = requests.get(
        f'https://adventofcode.com/{year}/day/{day}',
        headers=headers, cookies=cookies
    )
    data = r.text

    try:
        import html2text
    except ImportError:
        html2text = None
        cprint('Warning: html2text not installed. Skipping cleaning.', 'yellow')

    if html2text:
        data = html2text.html2text(data)
        data = re.search(r'[^\n]+---.*', data, re.DOTALL).group()
    
    return data


def submit(
        answer: str, level: int, 
        day: int = day_idx, year: int = year
    ) -> bool:
    """
    Submits the answer for the current day.

    Arguments
    ---------
    answer: The answer to submit.
    level: The level of the answer.
    day: The day to submit.
    year: The year to submit.

    Returns
    -------
    Whether or not the submission was correct.
    """
    answer = str(answer)

    cprint(f'------- SUBMITTING -------', 'blue')
    print("You are about to submit ", end = '')
    cprint(answer, 'green', end = '')
    print(f" for level {level} of day {day}, {year}.")
    cprint("Are you sure you want to submit (y/n)? ", 'blue', end = '')
    if input()[0].lower() != 'y':
        return

    r = requests.post(
        f'https://adventofcode.com/{year}/day/{day}/answer',
        headers=headers, cookies=cookies,
        data={'answer': answer, 'level': str(level)}
    )
    r = r.text

    if "don't repeatedly request this endpoint before it unlocks!" in r:
        cprint("Submission is locked: ", 'red', end = '')
        print("Wait until midnight Eastern.")
        return False
    
    elif "That's the right answer" in r:
        cprint("Submission successful!", 'green')
        return True
    
    elif "That's not the right answer" in r:
        cprint("Submission failed: ", 'red', end = '')
        if "your answer is too low" in r:
            print("Your answer is too low.")
        elif "your answer is too high" in r:
            print("Your answer is too high.")
        else:
            print("Incorrect answer.")
        return False

    elif "You gave an answer too recently" in r:
        cprint("Submission failed: ", 'red', end='')
        print("You gave an answer too recently.")
        time_left = re.search(r'You have (.+) left', r).group(1)
        cprint(f'You have {time_left} left.', 'yellow')
        return False
    
    elif "You don't seem to be solving the right level." in r:
        cprint("Submission failed: ", 'red', end='')
        print("Wrong level?")
        return False
    
    return r


if __name__ == '__main__':
    if ('--input' in argv) or ('-i' in argv) or ('--get-input' in argv):
        get_input(write = True)