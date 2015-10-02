__author__ = 'JuanFrancisco'
import curses

def create_window(rows, cols, y, x, title):
    win = curses.newwin(rows, cols, y, x);

    win.box()
    win.move(0, 1)
    win.addstr('title')
    win.move(1, 1)
    return win


def main(stdscr):
    win = create_window(5, 20, 10, 10, 'title')
    win.addstr('hello world')
    win.getch()


    win.mvwin(15, 30)
    stdscr.refresh()

    win.getch()

if __name__ == '__main__':
    curses.wrapper(main)