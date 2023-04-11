from base import BaseClass

class LRU(BaseClass):
    def __init__(self, frame_size, page_list):
        super().__init__(frame_size, page_list)
       

    
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
        checked = []
        for i in range(page_index -1, -1, -1):
            if self.page_list[i] in self.frame:
                if self.page_list[i] not in checked:
                    lru = self.page_list[i]
                    checked.append(lru)
            else:
                break

        return lru