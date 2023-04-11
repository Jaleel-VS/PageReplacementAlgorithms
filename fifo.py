from base import BaseClass

class FIFO(BaseClass):
    def __init__(self, frame_size, page_list):
        super().__init__(frame_size, page_list)
    
    def run(self):
        for page in self.page_list:
            if page in self.frame:
                self.page_hit += 1
            else:
                self.page_fault += 1
                self.frame.pop(0)
                self.frame.append(page)
    
