class LRU:
    def __init__(self, frame_size, page_list):
        self.frame = [-1 for _ in range(frame_size)]
        self.frame_size = frame_size
        self.page_list = page_list
        self.page_fault = 0
        self.page_hit = 0

    
    def run(self):
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
        lru = -1
        for i in range(page_index -1, -1, -1):
            if self.page_list[i] in self.frame:
                lru = self.page_list[i]
            else:
                break

        return lru