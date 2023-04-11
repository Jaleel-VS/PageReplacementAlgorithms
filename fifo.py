class FIFO:
    def __init__(self, frame_size, page_list):
        self.queue = [-1 for _ in range(frame_size)]
        self.frame_size = frame_size
        self.page_list = page_list
        self.page_fault = 0
        self.page_hit = 0
    
    def run(self):
        for page in self.page_list:
            if page in self.queue:
                self.page_hit += 1
            else:
                self.page_fault += 1
                self.queue.pop(0)
                self.queue.append(page)
    
