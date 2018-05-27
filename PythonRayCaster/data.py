import math
from utility import *
class Point:
   def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z
   
   def __eq__(self, other):
      return (epsilon_equal(self.x, other.x) and
              epsilon_equal(self.y, other.y) and
              epsilon_equal(self.z, other.z)) 

class Vector:
   def __init__(self,x,y,z):
      self.x = x
      self.y = y
      self.z = z
   
   def __eq__(self,other):
      return (epsilon_equal(self.x, other.x) and
              epsilon_equal(self.y, other.y) and
              epsilon_equal(self.z, other.z))
class Ray:
   """a class that creates a ray
      Attributes:
         pt-point object
         dir- vector object"""

   def __init__(self,pt,dir):
      self.pt = pt
      self.dir = dir

   def __eq__(self,other):
      return (self.pt == other.pt and
              self.dir == other.dir)
class Sphere:
   """a class that represents spheres
      Attributes:
         center- point object
         radius - float
         color- Color object"""

   def __init__(self,center,radius, color, finish):
      self.center = center
      self.radius = radius
      self.color = color
      self.finish = finish

   def __eq__(self,other):
      return (self.center == other.center and
              epsilon_equal(self.radius, other.radius) and self.color == other.color and self.finish == other.finish)

class Color:
   """ represents a color in terms of Red, Green, and Blue)"""
   
   def __init__(self,red,green,blue):
      self.red = red
      self.green = green
      self.blue = blue

   def __eq__(self, other):
      return (epsilon_equal(self.red, other.red) and epsilon_equal(self.green, other.green) and epsilon_equal(self.blue, other.blue))

class Finish:
   """think of dull or shiny white on an ibject when light is shone on it. ambinet represents the percentage of abient light reflected by the finish"""
   def __init__(self, ambient, diffuse, specular, roughness):
      self.ambient = ambient
      self.diffuse = diffuse
      self.specular = specular
      self.roughness = roughness

   def __eq__(self, other):
      return epsilon_equal(self.ambient, other.ambient) and epsilon_equal(self.diffuse,other.diffuse) and epsilon_equal(self.specular, other.specular) and epsilon_equal(self.roughness, other.roughness)

class Light:
   """takes a Point object as the position of the light anad a Color object that represents the intensity of the light"""
   def __init__(self, point, color):
      self.point = point
      self.color = color

   def __eq__(self, other):
      return self.point == other.point and self.color == other.color      
