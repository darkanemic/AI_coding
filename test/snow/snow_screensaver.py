import curses
import random
import time


def main(stdscr):
    curses.curs_set(0)  # hide cursor
    stdscr.nodelay(True)  # non-blocking input
    max_y, max_x = stdscr.getmaxyx()
    snowflakes = []

    for _ in range(max_x // 2):
        x = random.randint(0, max_x - 1)
        y = random.randint(0, max_y - 1)
        snowflakes.append([y, x])

    while True:
        stdscr.erase()
        new_flakes = []
        for y, x in snowflakes:
            char = '*'
            stdscr.addch(y, x, char)
            y += 1
            if y < max_y:
                new_flakes.append([y, x])
            else:
                new_flakes.append([0, random.randint(0, max_x - 1)])
        snowflakes = new_flakes
        stdscr.refresh()
        time.sleep(0.1)

        try:
            if stdscr.getch() != -1:
                break
        except curses.error:
            pass


if __name__ == '__main__':
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
