'''
Write a Python program that implements the FIFO, LRU, and optimal
page replacement algorithms 
'''

import sys
import random

REFERENCE_STR_SIZE = 38
PAGE_NUM_RANGE = (0, 9)
MAX_PAGE_FRAMES = 7


class Paging:
    def __init__(self, frame_size, page_list):
        self.frame = [-1 for _ in range(frame_size)]
        self.frame_size = frame_size
        self.page_list = page_list
        self.page_fault = 0
        self.page_hit = 0

    def clear_cache(self):
        self.frame = [-1 for _ in range(self.frame_size)]
        self.page_fault = 0
        self.page_hit = 0

    def run_algorithms(self):
        # run fifo
        self.fifo()
        print(f'FIFO: {self.page_fault} page faults, {self.page_hit} page hits')

        # run lru
        self.lru()
        print(f'LRU: {self.page_fault} page faults, {self.page_hit} page hits')

        # run optimal
        self.opt()
        print(
            f'Optimal: {self.page_fault} page faults, {self.page_hit} page hits')

    # FIFO
    def fifo(self):
        self.clear_cache()
        
        for page in self.page_list:
            if page in self.frame:
                self.page_hit += 1
            else:
                self.page_fault += 1
                self.frame.pop(0)
                self.frame.append(page)

    # LEAST RECENTLY USED
    def lru(self):
        self.clear_cache()

        for i in range(len(self.page_list)):
            page = self.page_list[i]
            if page in self.frame:
                self.page_hit += 1
            else:
                self.page_fault += 1
                if -1 in self.frame:
                    self.frame[self.frame.index(-1)] = page
                else:
                    lru_page = self.find_least_recently_used(i)
                    self.frame[self.frame.index(lru_page)] = page

    def find_least_recently_used(self, page_index):
        # find the least recently used page
        lru_val = -1
        checked = []
        for i in range(page_index - 1, -1, -1):
            if self.page_list[i] in self.frame:
                if self.page_list[i] not in checked:
                    lru_val = self.page_list[i]
                    checked.append(lru_val)
            else:
                break

        return lru_val

    # OPTIMAL
    def opt(self):
        self.clear_cache()

        for i in range(len(self.page_list)):
            page = self.page_list[i]
            if page in self.frame:
                self.page_hit += 1
            else:
                self.page_fault += 1
                if -1 in self.frame:
                    self.frame[self.frame.index(-1)] = page
                else:
                    opt_page = self.find_optimal(i)
                    self.frame[self.frame.index(opt_page)] = page

    def find_optimal(self, page_index):
        opt_val = -1
        used = []
        for i in range(page_index, len(self.page_list)):
            if self.page_list[i] in self.frame:
                if self.page_list[i] not in used:
                    opt_val = self.page_list[i]
                    used.append(opt_val)

        if len(used) != self.frame_size:
            for page in self.frame:
                if page not in used:
                    opt_val = page

        return opt_val


def generate_page_ref_string():
    # generate a string based on the range
    ref_str = [random.randint(PAGE_NUM_RANGE[0], PAGE_NUM_RANGE[1] + 1)
               for i in range(REFERENCE_STR_SIZE)]
    return ref_str


if __name__ == "__main__":

    command = sys.argv

    if len(command) != 2:
        print("Usage: python paging.py [number of page frames]")

    try:
        num_pages = int(command[1])

    except ValueError:
        print("Usage: please specify a valid integer")
        sys.exit()

    if num_pages >= 1 and num_pages <= MAX_PAGE_FRAMES:
        paging_algorithms = Paging(num_pages, generate_page_ref_string())
        paging_algorithms.run_algorithms()

    else:
        print("Usage: please specify a number between 1 and 7")
