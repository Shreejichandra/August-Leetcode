# Random Point in Non-overlapping Rectangles

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.N = len(rects)
        
        self.comm_points = [0] * (self.N )
        z = 0
        i = 0
        for x1, y1, x2, y2 in rects:
            z += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.comm_points[i] = z
            i += 1
        self.total_points = self.comm_points[self.N - 1]
           
     
    def pickRect(self):
        rectangle = random.randint(0, self.total_points-1)
        return bisect.bisect(self.comm_points, rectangle)

    def pickPoint(self, rect):
        x1, y1, x2, y2 = rect
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return x, y

    def pick(self) -> List[int]:
        rectIndex = self.pickRect()
        rect = self.rects[rectIndex]
        return self.pickPoint(rect)
