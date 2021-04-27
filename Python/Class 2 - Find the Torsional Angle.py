class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, other):
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        x1 = self.x
        y1 = self.y
        z1 = self.z
        x2 = other.x
        y2 = other.y
        z2 = other.z
        return (x1 * x2 + y1 * y2 + z1 * z2)

    def cross(self, other):
        x1 = self.x
        y1 = self.y
        z1 = self.z
        x2 = other.x
        y2 = other.y
        z2 = other.z
        return Points(y1 * z2 - y2 * z1, -1 * (x1 * z2 - x2 * z1), x1 * y2 - x2 * y1)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
