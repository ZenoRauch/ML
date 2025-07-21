class Util:
    def find_range(self, points:list[Point]):
        min_x = 0
        max_x = 0
        min_y = 0 
        max_y = 0
        for point in points:
            if point.X < min_x : min_x = point.X
            if point.X > max_x : max_x = point.X
            if point.Y < min_y : min_y = point.Y
            if point.Y > max_y : max_y = point.Y
        return (min_x*1.1, max_x*1.1), (min_y*1.1, max_y*1.1)