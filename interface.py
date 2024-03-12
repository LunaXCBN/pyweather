import curses
import json

def first_launch_config():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.curs_set(False)
    if curses.has_colors():
        curses.start_color()

    stdscr.addstr("LOL")
    stdscr.refresh()
    stdscr.getch()
    curses.endwin()

with open('config.json', 'r') as f:
    config = json.load(f)

if config['first_launch'] == True:
    print("True")
    first_launch_config()
else:
    print("False")
