class Iterator:
    def __init__(self, start=0, limit=1100):
        self.limit = limit
        self.num = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < self.limit:
            num = self.num
            self.num += 1
        else:
            raise StopIteration
        return num

