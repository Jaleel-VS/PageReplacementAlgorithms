class BaseClass:
    def __init__(self, frame_size, page_list):
        self.frame = [-1 for _ in range(frame_size)]
        self.frame_size = frame_size
        self.page_list = page_list
        self.page_fault = 0
        self.page_hit = 0