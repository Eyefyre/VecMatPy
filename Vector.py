import math
class Vector2D():
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def sum(self, vec2):
        self.x += vec2.x
        self.y += vec2.y

    def subtract(self, vec2):
        self.x -= vec2.x
        self.y -= vec2.y

    def scale(self, scalar):
        self.x *= scalar
        self.y *= scalar

    def setVector(self,x,y):
        self.x = x
        self.y = y

    def getMagnitude(self):
        ax = self.x * self.x
        bx = self.y * self.y
        d = ax + bx
        return math.sqrt(d)

    def negate(self):
        self.x *= -1
        self.y *= -1

    def normalise(self):
        m = self.getMagnitude()
        if m > 0:
            self.x /= m
            self.y /= m

    def dot(self,vec2):
        vx = self.x * vec2.X
        vy = self.y * vec2.y
        return vx + vy

    def dist(self, vec2):
        d = (self.x - vec2.x) * (self.x - vec2.x)
        e = (self.y - vec2.y) * (self.y - vec2.y)
        f = d + e
        return math.sqrt(f)

    def div(self, div):
        self.x /= div
        self.y /= div 

    def setMagnitude(self, len):
        self.normalise()
        self.scale(len)

    def limitMag(self, max):
        mSq = self.getMagnitude() * self.getMagnitude()
        if mSq > (max * max):
            self.setMagnitude(max)

    def copy(self):
        return self

    def vectorDistance(self, vec1, vec2):
        d = (self.x - vec2.x) * (self.x - vec2.x)
        e = (self.y - vec2.y) * (self.y - vec2.y)
        f = d + e
        return math.sqrt(f)
        math.atan2

    def getAngle(self, vec1):
        vx = self.x - vec1.x
        vy = self.y - vec1.y
        return math.degrees(math.atan2(vx, vy))
    
    @staticmethod
    def sumVector(vec1,vec2):
        vec = Vector2D(vec1.x + vec2.x,vec1.y + vec2.y)
        return vec

    @staticmethod
    def subtractVector(vec1,vec2):
        vec = Vector(vec1.x - vec2.x,vec1.y-vec2.y)
        return vec

    @staticmethod
    def negateVector(vec1):
        vec = Vector2D(vec1.x * -1,vec1.y * -1)
        return vec

    @staticmethod
    def scaleVector(scalar):
        vec = Vector2D(vec1.x * scalar,vec1.y * scalar)
        return vec

    @staticmethod
    def dotVector(vec1,vec2):
        vx = vec1.x * vec2.X
        vy = vec1.y * vec2.y
        return vx + vy

    @staticmethod
    def getVectorAngle(self, vec1, vec2):
        vx = vec2.x - vec1.x
        vy = vec2.y - vec1.y
        return math.degrees(math.atan2(vx, vy))

    def __str__(self):
        return str("X: " + str(self.x) + ", " "Y: " + str(self.y) + ", Mag: " + str(self.getMagnitude()))

