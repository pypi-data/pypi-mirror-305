import curses
from enum import Enum
import threading
import time
from typing import Dict
from queue import Queue

from . import scripture as Message


class Color(Enum):
    """Color options for BlessedCLI"""

    DEFAULT = -1
    BLACK = curses.COLOR_BLACK
    BLUE = curses.COLOR_BLUE
    CYAN = curses.COLOR_CYAN
    GREEN = curses.COLOR_GREEN
    MAGENTA = curses.COLOR_MAGENTA
    RED = curses.COLOR_RED
    WHITE = curses.COLOR_WHITE
    YELLOW = curses.COLOR_YELLOW


class BlessedCLI:
    """CLI helper class powered by Buddha"""

    def __init__(self, stdscr: curses.window):
        self.__stdscr = stdscr
        self.__colors = self.__init_colors()

    def __init_colors(self) -> Dict[int, int]:
        """Initialize color pairs with built-in colors"""
        # Set the terminal to default color
        curses.use_default_colors()

        colors = {}
        for i, color in enumerate(Color):
            if color == Color.DEFAULT:
                colors[color] = curses.color_pair(0)
                continue
            curses.init_pair(i, color.value, -1)
            colors[color] = curses.color_pair(i)
        
        return colors
    
    def clear(self):
        """Clear the screen"""
        self.__stdscr.clear()
    
    def print(self, message: str = "", color: Color = Color.DEFAULT):
        """Print a message to the screen"""
        self.__stdscr.addstr(message, self.__colors[color])
    
    def bless(self):
        """Give a blessing to the program"""
        self.print(Message.BLESSING)

    def pray(self, process: callable, kwargs: dict = {}, message: str = ""):
        """Run a long-running process and pray for its success until it ends"""
        stop_event = threading.Event()
        queue = Queue()

        def run_process():
            try:
                result = process(**kwargs)
                queue.put(result)
            except Exception as e:
                queue.put(e)
            finally:
                # Stop the prayer
                stop_event.set()

        def pray_for_success():
            self.__stdscr.clear()
            for i, chunk in enumerate(Message._PRAYER_CHUNKS):
                chunk_color = self.__colors[Color.YELLOW] if i % 2 == 1 else self.__colors[Color.DEFAULT]
                self.__stdscr.addstr(chunk, chunk_color)
            self.__stdscr.addstr("\n" + message)
            cursor = self.__stdscr.getyx()

            state = 0
            # Pray until the process ends
            while not stop_event.is_set(): 
                # Animate praying arms
                self.__stdscr.addstr(7, 33, Message._PRAYING_ARMS[state % 2])
                dots = "." * (state % 4)
                self.__stdscr.addstr(*cursor, dots.ljust(3, " "))
                
                # Update text every 0.5 seconds
                self.__stdscr.refresh()
                state = state + 1
                stop_event.wait(0.5)
        
        # Run the process in a separate thread
        thread = threading.Thread(target=run_process)
        thread.start()
        pray_for_success()
        thread.join()

        # Return the result from the process
        if not queue.empty():
            result = queue.get()
            print(result)
            if isinstance(result, Exception):
                raise result
            return result
        
    def approve(self):
        """Print a message to the screen"""
        self.__stdscr.addstr("Approved!", self.__colors[Color.GREEN])

    def error(self, message: str = ""):
        """Print an error message to the screen"""
        self.__stdscr.clear()
        for i, chunk in enumerate(Message._ERROR_CHUNKS[:-1]):
            chunk_color = self.__colors[Color.RED] if i % 2 == 0 else self.__colors[Color.DEFAULT]
            self.__stdscr.addstr(chunk, chunk_color)
        
        # Print last chunk one by one
        for char in Message._ERROR_CHUNKS[-1]:
            self.__stdscr.addch(char, self.__colors[Color.RED])
            self.__stdscr.refresh()
            time.sleep(0.1)

        self.__stdscr.addstr("\n" + message)

    def wait(self):
        """Wait for a key press"""
        return self.__stdscr.getkey()
    
    def input(self):
        """Get user input until enter key is pressed"""
        # Get the starting cursor position
        cursor = self.__stdscr.getyx()

        text = ""
        while True:
            key = self.__stdscr.getch()

            if key == 10: # Enter
                break
            elif key in (127, 8): # Backspace
                text = text[:-1]
                self.__stdscr.addstr(*cursor, text + " ")
                self.__stdscr.addstr(*cursor, text)
            elif 32 <= key <= 126:
                text += chr(key)
                self.__stdscr.addch(key)

            # Update the screen right away
            self.__stdscr.refresh()

        return text

if __name__ == "__main__":
    pass