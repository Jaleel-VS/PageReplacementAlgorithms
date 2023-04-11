'''
Write a Python program that implements the FIFO, LRU, and optimal
page replacement algorithms 
'''

import sys
import random
from fifo import FIFO
from lru import LRU

REFERENCE_STR_SIZE = 12
PAGE_NUM_RANGE = (0, 9)
MAX_PAGE_FRAMES = 7


class Main:
    def __init__(self, size, page):
        self.size = size
        self.page = page

    

    def run_algorithms(self):
        # run fifo
        fifo = FIFO(self.size, self.page)
        fifo.run()
        print("FIFO: ", fifo.page_fault, fifo.page_hit)

        lru = LRU(self.size, self.page)
        lru.run()
        print("LRU: ", lru.page_fault, lru.page_hit)



def generate_page_ref_string(self):
        # generate a string based on the range
        ref_str = [random.randint(PAGE_NUM_RANGE[0], PAGE_NUM_RANGE[1] + 1) for i in range(REFERENCE_STR_SIZE)]
        return ref_str

if __name__ == "__main__":
    # parse command

    # create a main object
    test_string = "701203042303120"
    # main = Main(num_page_frames, generate_page_ref_string())
    main = Main(3, test_string)
    main.run_algorithms()

    # command = sys.argv

    # if len(sys.argv) != 2:
    #     print("Usage: python paging.py [number of page frames]")

    # else:
    #     # get the number of page frames
    #     num_page_frames = int(command[1])
    #     if num_page_frames > MAX_PAGE_FRAMES:
    #         print("Number of page frames must be less than or equal to 7")
    #     else:
            