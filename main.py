'''
Write a Python program that implements the FIFO, LRU, and optimal
page replacement algorithms 
'''

import sys
import random
from fifo import FIFO
from lru import LRU
from opt import Optimal

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
        print(f'FIFO: {fifo.page_fault} page faults, {fifo.page_hit} page hits')

        # run lru
        lru = LRU(self.size, self.page)
        lru.run()
        print(f'LRU: {lru.page_fault} page faults, {lru.page_hit} page hits')
      

        # run optimal
        opt = Optimal(self.size, self.page)
        opt.run()
        print(f'Optimal: {opt.page_fault} page faults, {opt.page_hit} page hits')
      




def generate_page_ref_string(self):
        # generate a string based on the range
        ref_str = [random.randint(PAGE_NUM_RANGE[0], PAGE_NUM_RANGE[1] + 1) for i in range(REFERENCE_STR_SIZE)]
        return ref_str

if __name__ == "__main__":
    # parse command

    # create a main object
    # test_string = "701203042303120"
    # test_string = "701203042303212017"
    # test_string = "130356"
    # test_string = "02164010312"
    # test_string = "7012030423032"
    test_string = "7012030423032"
    # main = Main(num_page_frames, generate_page_ref_string())
    main = Main(4, test_string)
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
            