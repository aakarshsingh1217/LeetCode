import collections

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = collections.deque()
        self.sum = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.sum += val

        while len(self.queue) > self.size:
            popped_val = self.queue.popleft()
            self.sum -= popped_val

        return self.sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)