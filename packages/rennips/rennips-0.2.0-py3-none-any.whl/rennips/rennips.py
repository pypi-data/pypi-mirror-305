import os
import shutil
import sys
import time
from itertools import cycle


__version__ = "0.2.0"


class Rennips:
    def __init__(self, iterable, desc="", mode="normal"):
        self.iterable = iterable
        self.desc = desc
        self.progress_time = 0
        self.mode = mode

        if hasattr(iterable, '__len__'):
            self.total = len(iterable)
        else:
            self.total = None

        self.current = 0
        self.spinner_chars = ['|', '/', '-', '\\']
        self.big_spinner_chars = ['█', '▓', '▒', '░']

        self.terminal_width, self.terminal_height = shutil.get_terminal_size()

        if self.mode.lower() == "big":
            self.total_chars = self.terminal_width * (self.terminal_height - 1)
            self.spinner = cycle(self.big_spinner_chars)
        else:
            self.spinner = cycle(self.spinner_chars)
        self.start_time = None
        self.max_progress_length = 0

    def __iter__(self):
        self.start_time = time.time()
        self._iterator = iter(self.iterable)
        return self

    def __next__(self):
        try:
            value = next(self._iterator)
            self.current += 1
            self.print_progress()
            return value
        except StopIteration:
            self.close()
            raise

    def create_big_spinner_frame(self, progress_info):
        spinner_char = next(self.spinner)

        frame = []

        info_row = self.terminal_height // 2
        info_start_col = (self.terminal_width - len(progress_info)) // 2

        # 각 줄 생성
        for row in range(self.terminal_height - 1):  # 마지막 줄은 남겨둠
            if row == info_row:
                line = spinner_char * info_start_col
                line += progress_info
                line += spinner_char * (self.terminal_width - len(line))
            else:
                line = spinner_char * self.terminal_width
            frame.append(line)

        return '\n'.join(frame)

    def print_progress(self):
        self.progress_time = time.time() - self.start_time

        if self.mode.lower() == "simple":
            spinner_char = next(self.spinner)
            progress_str = f"\r{self.desc} {spinner_char}"
            self.max_progress_length = max(self.max_progress_length, len(progress_str))
            sys.stdout.write(progress_str)
            sys.stdout.flush()
        elif self.mode.lower() == "big":
            if self.total is not None:
                progress = min(100, round(self.current / self.total * 100, 1))
                progress_info = f' {progress}% [{self.current}/{self.total}] '
            else:
                progress_info = f' [{self.current} items] '

            frame = self.create_big_spinner_frame(progress_info)

            sys.stdout.write('\033[H')  # Cursors to Home Position
            sys.stdout.write('\033[2J')  # Clear screen
            sys.stdout.write(frame)
        else:
            spinner_char = next(self.spinner)
            progress_str = f"\r{self.desc} {spinner_char} "
            if self.total is not None:
                progress = min(100, round(self.current / self.total * 100, 1))
                progress_str += f"{progress}% [{self.current}/{self.total}] "
            else:
                progress_str += f"[{self.current} items] "
            self.max_progress_length = max(self.max_progress_length, len(progress_str))
            sys.stdout.write(progress_str)
            sys.stdout.flush()

    def close(self):
        if self.mode.lower() == "simple":
            sys.stdout.write("\r" + " " * self.max_progress_length + "\r")
        elif self.mode.lower() == "big":
            sys.stdout.write('\033[2J')
            sys.stdout.write('\033[H')
        else:
            sys.stdout.write("\r")
        sys.stdout.write("Finished.")
        sys.stdout.flush()


def rennips(iterable, desc="", mode="normal"):
    return Rennips(iterable, desc, mode)
