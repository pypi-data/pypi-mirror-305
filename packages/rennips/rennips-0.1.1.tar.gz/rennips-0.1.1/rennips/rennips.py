import os
import sys
import time
from itertools import cycle


__version__ = "0.1.1"


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
        self.spinner = cycle(self.spinner_chars)
        self.start_time = None

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

    def print_progress(self):
        spinner_char = next(self.spinner)
        self.progress_time = time.time() - self.start_time

        if self.mode.lower() == "simple":
            progress_str = f'\r{self.desc} {spinner_char}'
        else:
            progress_str = f'\r{self.desc} {spinner_char} '
            if self.total is not None:
                progress = min(100, round(self.current / self.total * 100, 1))
                progress_str += f'{progress}% [{self.current}/{self.total}] '
            else:
                progress_str += f'[{self.current} items] '

        sys.stdout.write(progress_str)
        sys.stdout.flush()

    def close(self):
        sys.stdout.write('\r')
        sys.stdout.write(' Finished.')
        sys.stdout.flush()


def rennips(iterable, desc="", mode="normal"):
    return Rennips(iterable, desc, mode)
