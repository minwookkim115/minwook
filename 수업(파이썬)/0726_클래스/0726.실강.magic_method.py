class Shape:

    def __init__(self, w, h):
        self.w = w
        self.h = h

    def __gt__(self, other):
        return self.w * self.h > other.w * other.h
    
    def __eq__ (self, other):
        return self.w * self.h == other.w * other.h


s1 = Shape(3, 4)
s2 = Shape(5, 6)
s3 = Shape(6, 5)

print(s2 > s1)
print(s2 == s3)