import math

class Cylinder():

	def __init__(self, rad, h):
		self.rad = rad
		self.h = h

	def volume(self):
		return 3.14 * (self.rad**2) * self.h

	def area(self):
		return ( (2*(3.14*(self.rad**2))) + ((2*3.14*self.rad)*self.h) )


print("Radius:")
r=input()

print("Height:")
h=input()

cyl = Cylinder(int(r),int(h))
print("Volume is " + str(cyl.volume()))
print("Area is " + str(cyl.area()))