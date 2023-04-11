from base import BaseClass

class Optimal(BaseClass):
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
                    opt_page = self.find_optimal(i)
                    self.frame[self.frame.index(opt_page)] = page

    def find_optimal(self, page_index):
        opt = -1
        used = []
        for i in range(page_index, len(self.page_list)):
            if self.page_list[i] in self.frame:
                if self.page_list[i] not in used:
                    opt = self.page_list[i]
                    used.append(opt)

        if len(used) != self.frame_size:
            for page in self.frame:
                if page not in used:
                    opt = page

        return opt