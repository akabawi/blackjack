import math

class Line():

	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return math.sqrt( (self.coor2[1]-self.coor1[1])**2 + (self.coor2[0]-self.coor1[0])**2 )

	def slope(self):
		return ( (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0]) )


print("X 1:")
x1=input()

print("Y 1:")
y1=input()

print("X 2:")
x2=input()

print("Y 1:")
y2=input()

c1 = (int(x1),int(y1))
c2 = (int(x2),int(y2))

l = Line(c1,c2)
print("Distance is " + str(l.distance()))
print("Slope is " + str(l.slope()))