from vector_math import *
import math
import data

def sphere_intersection_point(ray, sphere):
   A = dot_vector(ray.dir, ray.dir)
   B = dot_vector( scale_vector(difference_vector(ray.pt, sphere.center), 2.0), ray.dir)
   C = ( dot_vector(difference_vector(ray.pt, sphere.center), 
         difference_vector(ray.pt, sphere.center)) - (sphere.radius)**2)
   discriminant = (B**2) - (4*A*C)
   if discriminant < 0:
      return None
   t1 = (-1*B + math.sqrt(discriminant))/(2.0*A)
   t2 = (-1*B - math.sqrt(discriminant))/(2.0*A)
   if discriminant == 0: 
      if  t1 >= 0: 
         return translate_point(ray.pt, scale_vector(ray.dir, t1)) 
      else:
         return None
   else: 
      if t1 >= 0 and t2 >= 0:
         return translate_point(ray.pt, scale_vector(ray.dir, t2))
      elif t1 >=0 and t2 < 0:
         return translate_point(ray.pt, scale_vector(ray.dir, t1))
      elif t1 < 0 and t2 < 0 :
         return None

def find_intersection_points(sphere_list, ray):
   new_sphere_list = [(s, sphere_intersection_point(ray, s)) for s in sphere_list]
   return [s for s in new_sphere_list if s[1] != None]
     
def sphere_normal_at_point(sphere, point):
   return normalize_vector(vector_from_to(sphere.center, point))

