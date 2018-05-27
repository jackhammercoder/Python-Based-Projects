import unittest
from data import *
from vector_math import *
from collisions import *
from cast import *
class TestCases(unittest.TestCase):
   def test_point(self):
      point_1 = Point(-.03,4,50)
      self.assertAlmostEqual(-.03, point_1.x)
      self.assertEqual(4, point_1.y)
      self.assertEqual(50, point_1.z)

   def test_point_2(self):
      point_2 = Point(50.48,6004,5670)
      self.assertAlmostEqual(50.48, point_2.x)
      self.assertEqual(6004, point_2.y)
      self.assertEqual(5670, point_2.z)

   def test_point_3(self):
      point_1 = Point(-.03, 4, 50)
      point_2 = Point(-.03, 4, 50)
      self.assertEqual(point_1, point_2) 

   def test_point_4(self):
      point_1 = Point(-.03, 4, 50)
      point_2 = Point(1.0, 4, 50)
      self.assertEqual(point_1 == point_2, False)

   def test_point_5(self):
      point_1 = Point(-.03, 4, 50)
      point_2 = Point(-.03, 5, 50)
      self.assertEqual(point_1 == point_2, False)

   def test_point_6(self):
      point_1 = Point(-.03, 4, 50)
      point_2 = Point(-.03, 4, 51)
      self.assertEqual(point_1 == point_2, False)

   def test_vector(self):
      vector_1 = Vector(40, -50, 3.3)
      self.assertEqual(40, vector_1.x)
      self.assertEqual(-50, vector_1.y)
      self.assertAlmostEqual(3.3, vector_1.z)

   def test_vector_2(self):
      vector_2 = Vector(4000, -5980,673.3)
      self.assertEqual(4000, vector_2.x)
      self.assertEqual(-5980, vector_2.y)
      self.assertAlmostEqual(673.3, vector_2.z)

   def test_vector_3(self):
      vector_1 = Vector(1.0, 2.0, -6.0)
      vector_2 = Vector(1.0, 2.0, -6.0)
      self.assertEqual(vector_1, vector_2)

   def test_vector_4(self):
      vector_1 = Vector(2.0, 2.0, -6.0)
      vector_2 = Vector(1.0, 2.0, -6.0)
      self.assertEqual(vector_1 == vector_2, False)

   def test_vector_5(self):
      vector_1 = Vector(1.0, 4.0, -6.0)
      vector_2 = Vector(1.0, 2.0, -6.0)
      self.assertEqual(vector_1 == vector_2, False)

   def test_vector_6(self):
      vector_1 = Vector(1.0, 2.0, -7.0)
      vector_2 = Vector(1.0, 2.0, -6.0)
      self.assertEqual(vector_1 == vector_2, False)

   def test_ray(self):
      ray_1 = Ray(Point(0,4,5),Vector(1,3,1))
      self.assertEqual(0, ray_1.pt.x)
      self.assertEqual(4, ray_1.pt.y)
      self.assertEqual(5, ray_1.pt.z)
      self.assertEqual(1, ray_1.dir.x)
      self.assertEqual(3, ray_1.dir.y)
      self.assertEqual(1, ray_1.dir.z)

   def test_ray_2(self):
      ray_2 = Ray(Point(3.0,774,895),Vector(.1,433,221))
      self.assertAlmostEqual(3.0, ray_2.pt.x)
      self.assertEqual(774, ray_2.pt.y)
      self.assertEqual(895, ray_2.pt.z)
      self.assertAlmostEqual(.1, ray_2.dir.x)
      self.assertEqual(433,ray_2 .dir.y)
      self.assertEqual(221, ray_2.dir.z)

   def test_ray_3(self):
      ray_1 = Ray(Point(3.0, 4.0, -5.0), Vector(1.4, 2.6, -7.9))
      ray_2 = Ray(Point(3.0, 4.0, -5.0), Vector(1.4, 2.6, -7.9))
      self.assertEqual(ray_1 , ray_2)

   def test_ray_4(self):
      ray_1 = Ray(Point(3.0, 5.0, -5.0), Vector(1.4, 2.6, -7.9))
      ray_2 = Ray(Point(3.0, 4.0, -5.0), Vector(1.4, 2.6, -7.9))
      self.assertEqual(ray_1 == ray_2, False)

   def test_ray_5(self):
      ray_1 = Ray(Point(3.0, 4.0, -5.0), Vector(1.4, 3.6, -7.9))
      ray_2 = Ray(Point(3.0, 4.0, -5.0), Vector(1.4, 2.6, -7.9))
      self.assertEqual(ray_1 == ray_2, False)

   def test_sphere(self):
      sphere_1 = Sphere(Point(2,4,6),.003, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      self.assertEqual(2, sphere_1.center.x)
      self.assertEqual(4, sphere_1.center.y)
      self.assertEqual(6, sphere_1.center.z)
      self.assertAlmostEqual(.003, sphere_1.radius)

   def test_sphere_2(self):
      sphere_2 = Sphere(Point(.002,34334,666),40.1,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      self.assertAlmostEqual(.002, sphere_2.center.x)
      self.assertEqual(34334, sphere_2.center.y)
      self.assertEqual(666, sphere_2.center.z)
      self.assertAlmostEqual(40.1, sphere_2.radius)

   def test_sphere_3(self):
      sphere_1 = Sphere(Point(.002, 34334.0, 666.0), 40.1,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      sphere_2 = Sphere(Point(.002, 34334.0, 666.0), 40.1,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      self.assertEqual(sphere_1, sphere_2)

   def test_sphere_4(self):
      sphere_1 = Sphere(Point(.0023333, 34334.0, 666.0), 40.1, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      sphere_2 = Sphere(Point(.002, 34334.0, 666.0), 40.1, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      self.assertEqual(sphere_1 == sphere_2, False)

   def test_sphere_5(self):
      sphere_1 = Sphere(Point(.002, 34334.0, 666.0), 60.1, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      sphere_2 = Sphere(Point(.002, 34334.0, 666.0), 40.1, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      self.assertEqual(sphere_1 == sphere_2, False)

   def test_scale_vector(self):
      vector_1 = scale_vector(Vector(1.0,1.0,1.0), 3.0)
      vector_2 = scale_vector(Vector(1.5,1.5,1.5), 2.0)
      self.assertEqual(vector_1, vector_2)

   def test_scale_vector_2(self):
      vector_1 = scale_vector(Vector(2.0,1.0,1.0), 3.0)
      vector_2 = scale_vector(Vector(1.5,1.5,1.5), 2.0)
      self.assertEqual(vector_1 == vector_2, False)

   def test_scale_vector_3(self):
      vector_1 = scale_vector(Vector(1.0,1.0,1.0), 4.0)
      vector_2 = scale_vector(Vector(1.5,1.5,1.5), 2.0)
      self.assertEqual(vector_1 == vector_2, False)

   def test_dot_vector(self):
      vector_1 = ( dot_vector(Vector(1.0,1.0,1.0), 
                   Vector(2.0,2.0,2.0)))
      vector_2 = ( dot_vector(Vector(3.0,0.0,0.0),
                   Vector(2.0,0.0,0.0)))
      self.assertEqual(vector_1, vector_2)

   def test_dot_vector_2(self):
      vector_1 = ( dot_vector(Vector(1.0,1.0,0.0),
                   Vector(2.0,2.0,2.0)))
      vector_2 = ( dot_vector(Vector(1.0,1.0,1.0), 
                   Vector(2.0,2.0,2.0)))
      self.assertEqual(vector_1 == vector_2, False)
   
   def test_dot_vector_3(self):
      vector_1 = (dot_vector(Vector(1.0,1.0,1.0),
                 Vector(3.0,2.0,2.0)))
      vector_2 = (dot_vector(Vector(1.0,1.0,1.0),
                 Vector(2.0,2.0,2.0)))
      self.assertEqual(vector_1 == vector_2, False)

   def test_length_vector(self):
      length_1 = length_vector(Vector(0.0, 1.0, 1.0))
      length_2 = length_vector(Vector(1.0, 1.0, 0.0))
      self.assertEqual(length_1, length_2)
   
   def test_length_vector_2(self):
      length_1 = length_vector(Vector(0.0, 1.0, 1.0))
      length_2 = length_vector(Vector(0.0, 1.0, 3.0))
      self.assertEqual(length_1 == length_2, False)

   def test_normalize_vector(self):
      vector_1 = normalize_vector(Vector(5.0, 5.0, 5.0))
      vector_2 = normalize_vector(Vector(10.0, 10.0, 10.0))
      self.assertEqual(vector_1, vector_2)

   def test_normalize_vector_2(self):
      vector_1 = normalize_vector(Vector(5.0, 5.0, 5.0))
      vector_2 = normalize_vector(Vector(5.0, 5.0, 80.0))
      self.assertEqual(vector_1 == vector_2, False)

   def test_difference_point(self):
      vector_1 = (difference_point(Point(5.0, 5.0, 5.0), 
                 Point(6.0, 6.0, 6.0)))
      vector_2 = (difference_point(Point(4.0, 4.0, 4.0), 
                 Point(5.0, 5.0, 5.0)))
      self.assertEqual(vector_1, vector_2)

   def test_difference_point_2(self):
      vector_1 = (difference_point(Point(5.0, 5.0, 5.0), 
                 Point(6.0, 6.0, 6.0)))
      vector_2 = (difference_point(Point(4.0, 4.0, 4.0), 
                 Point(7.0, 7.0, 7.0)))
      self.assertEqual(vector_1 == vector_2, False)

   def test_difference_vector(self):
      vector_1 = (difference_vector(Vector(5.0, 5.0, 5.0), 
                 Vector(16.0, 16.0, 16.0)))
      vector_2 = (difference_vector(Vector(4.0, 4.0, 4.0), 
                 Vector(15.0, 15.0, 15.0)))
      self.assertEqual(vector_1, vector_2)

   def test_difference_vector_2(self):
      vector_1 = (difference_vector(Vector(5.0, 5.0, 5.0), 
                 Vector(16.0, 16.0, 16.0)))
      vector_2 = (difference_vector(Vector(4.0, 4.0, 4.0), 
                 Vector(16.0, 16.0, 19.0)))
      self.assertEqual(vector_1 == vector_2, False)

   def test_translate_point(self):
      point_1 = (translate_point(Point(5.0, 5.0, 5.0), 
                 Vector(16.0, 16.0, 16.0)))
      point_2 = (translate_point(Point(4.0, 4.0, 4.0), 
                 Vector(17.0, 17.0, 17.0)))
      self.assertEqual(point_1, point_2)
   
   def test_translate_point_2(self):
      point_1 = (translate_point(Point(5.0, 5.0, 5.0), 
                 Vector(16.0, 16.0, 16.0)))
      point_2 = (translate_point(Point(4.0, 4.0, 4.0), 
                 Vector(18.0, 19.0, 16.0)))
      self.assertEqual(point_1 == point_2, False)

   def test_vector_from_to(self):
      vector_1 = (vector_from_to(Point(5.0, 5.0, 5.0), 
                 Point(16.0, 16.0, 16.0)))
      vector_2 = (vector_from_to(Point(4.0, 4.0, 4.0), 
                 Point(15.0, 15.0, 15.0)))
      self.assertEqual(vector_1, vector_2)

   def test_vector_from_to_2(self):
      vector_1 = (vector_from_to(Point(5.0, 5.0, 5.0), 
                 Point(16.0, 16.0, 16.0)))
      vector_2 = (vector_from_to(Point(4.0, 4.0, 4.0), 
                 Point(20.0, 15.9, 15.67)))
      self.assertEqual(vector_1 == vector_2, False)
   
# following test case is both t values are positive (det > 0). intersects sphere twice but will return first intersection. 
   def test_sphere_intersect_point(self):
      s = Sphere(Point(0.0,0.0,100.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0,0.0,0.0), data.Vector(0,0,1.0))
      self.assertEqual(sphere_intersection_point(r,s),Point(0.0, 0.0, 99.0))

# following test case is both t values are positive (det > 0). intersects sphere twice but will return first intersection. 
   def test_sphere_intersect_point_2(self):
      s = Sphere(Point(0.0, 50.0 , 0.0), 2.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0 , 0.0, 0.0), data.Vector(0.0,1.0,0.0))
      self.assertEqual(sphere_intersection_point(r,s),Point(0.0, 48.0, 0))

# following test case is both t values are positive (det > 0) intersects sphere twice but will return first intersection  This is the complicated one 
   def test_sphere_intersect_point_3(self):
      s = Sphere(Point(-3.0,3.0,3.0), 1.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(5.0,-3.0,1.6), data.Vector(-7.0,5.0,1.0))
      self.assertEqual(sphere_intersection_point(r,s),Point(-2.39473659994, 2.28195471424 , 2.65639094285))

# following test case is when the determinant is zero and the root is positive. 
   def test_sphere_intersect_point_4(self):
      s = Sphere(Point(0.0, 0.0 , 3.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0 , -3.0, 2.0), data.Vector(0.0,1.0,0.0))
      self.assertEqual(sphere_intersection_point(r,s),Point(0.0, 0.0,2.0))

# following test case is when the determinant is zero and t is a postive( this case t =0). 
   def test_sphere_intersect_point_5(self):
      s = Sphere(Point(5.0, 6.0 , 3.0), 1.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(5.0 , 5.0 , 3.0), data.Vector(1.0,0.0,0.0))
      self.assertEqual(sphere_intersection_point(r,s),Point(5.0, 5.0, 3.0))


# following test case is when the determinant is zero and the root is negative. 
   def test_sphere_intersect_point_6(self):
      s = Sphere(Point(0.0, 0.0 , 3.0), 1.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0 , 1.0, 4.0), data.Vector(0.0,0.0,1.0))
      self.assertEqual(sphere_intersection_point(r,s), None)

# following test case is when the determinant is negative. 
   def test_sphere_intersect_point_7(self):
      s = Sphere(Point(0.0, 0.0 , 3.0), 1.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0 , 1.0, 4.0), data.Vector(1.0,0.0,0.0))
      self.assertEqual(sphere_intersection_point(r,s), None)

# following test case is when the determinant is negative 
   def test_sphere_intersect_point_8(self):
      s = Sphere(Point(3.0, 0.0 , 0.0), 1.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0 , 0.0, -100.0), data.Vector(1.0,0.0,0.0))
      self.assertEqual(sphere_intersection_point(r,s), None)

# following test case is when the determinant is zero and the root is negative. 
   def test_sphere_intersect_point_9(self):
      s = Sphere(Point(1.0, 1.0 , 1.0), 1.0, Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      r = Ray(Point(0.0 ,0.0 ,-4.0), data.Vector(1.0,0.0,0.0))
      self.assertEqual(sphere_intersection_point(r,s), None)

#testing the case where no spheres in the list are hit
   def test_find_intersection_points(self):
    ray = Ray(Point(-4.0 ,0.0 ,0.0), data.Vector(0.0,0.0,1.0))
    sphere_1 = Sphere(Point(3.0, 0.0 , 0.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4)) 
    sphere_2 = Sphere(Point(1.0, 1.0 , 1.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4)) 
    sphere_3 = Sphere(Point(0.0, 0.0 , 3.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
    sphere_list = [ sphere_1 , sphere_2 , sphere_3 ]
    expected = []
    self.assertEqual(find_intersection_points(sphere_list, ray), expected)

#testing the case where 1 sphere in the list is hit
   def test_find_intersection_points_2(self):
    ray = Ray(Point(-4.0 ,0.0 ,0.0), data.Vector(0.0,0.0,1.0))
    sphere_1 = Sphere(Point(-4.0, 0.0 , 1.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4)) 
    sphere_2 = Sphere(Point(1.0, 1.0 , 1.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4)) 
    sphere_3 = Sphere(Point(0.0, 0.0 , 3.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
    sphere_list = [ sphere_1 , sphere_2 , sphere_3 ]
    expected = [(sphere_1,Point(-4,0.0,0.0))]
    self.assertEqual(find_intersection_points(sphere_list, ray), expected)

#testing the case where 3 spheres in the list is hit
   def test_find_intersection_points_3(self):
    ray = Ray(Point(0.0 ,0.0 ,0.0), data.Vector(1.0,0.0,0.0))
    sphere_1 = Sphere(Point(3.0, 0.0 , 0.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4)) 
    sphere_2 = Sphere(Point(7.0, 0.0 , 0.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4)) 
    sphere_3 = Sphere(Point(14.0, 0.0 , 0.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
    sphere_list = [ sphere_1 , sphere_2 , sphere_3 ]
    expected = [(sphere_1,Point(2.0,0.0,0.0)),(sphere_2, Point(6.0,0.0,0.0)),(sphere_3,Point(13.0,0.0,0.0))]
    self.assertEqual(find_intersection_points(sphere_list, ray), expected)

# testing the normal vector function for a intersection point on a sphere
   def test_sphere_normal_at_point(self):
      point1 = Point(0.0, 0.0, 2.0)
      sphere1 = Sphere(Point(0.0, 0.0 , 3.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      expected = Point(0.0, 0.0, -1.0)
      self.assertEqual(sphere_normal_at_point(sphere1, point1), expected)

# testing the normal vector function for a intersection point on a sphere
   def test_sphere_normal_at_point_2(self):
      point1 = Point(5.0, 5.0, 3.0)
      sphere1 = Sphere(Point(5.0, 6.0 , 3.0), 1.0,Color(0.0,0.0,0.0), Finish(.4,.4,.4,.4))
      expected = Point (0.0, -1.0, 0.0)
      self.assertEqual(sphere_normal_at_point(sphere1, point1), expected)

# testing the cast_ray function to return the color white, when it hits nothing:
   def test_cast_ray(self):
      amb = Color(1.0,1.0,1.0)
      light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
      ray = Ray(Point(0,0,0), Vector(1,0,0))
      sphere_list = [Sphere(Point(0, 2, 0 ), 1.0, Color(1.0, 0.0,0.0), Finish(.4,.4,.4,.4)), Sphere(Point(0, 5.0 , 0), 1.0, Color(0.0,0.0,1.0), Finish(.4,.4,.4,.4))] 
      self.assertEqual(cast_ray(ray, sphere_list,amb, light), Color(1.0, 1.0, 1.0))


# tsting result of a random sphere i chose.
   def test_cast_ray_2(self):
      amb = Color(1.0,1.0,1.0)
      light = Light(Point(-100, 100, -100), Color(1.5, 1.5, 1.5))
      ray = Ray(Point(0,0,0), Vector(1,0,0))
      sphere_list = [Sphere(Point(10000, 0, 0 ), 100, Color(0.0, 0.0, 1.0), Finish(.4,.4,.4,.4)), Sphere(Point(1,1.0, 0),1.0, Color(1.0, 0.0, 0.0), Finish(.4,.4,.4,.4))] 
      self.assertEqual(cast_ray(ray, sphere_list, amb, light), Color(.4, 0.0, 0.0))

# testing the find_points_to_test with the example points in asgn4 part 1
   def test_find_points_to_test(self):
      min_x = -4
      max_x = 4
      min_y = -2
      max_y = 2
      width = 4.0
      height = 2.0
      self.assertEqual(find_points_to_test(min_x, max_x, min_y, max_y, width, height), [Point(-4,2,0), Point(-2,2,0), Point(0,2,0), Point(2,2,0), Point(-4,0,0), Point(-2,0,0), Point(0,0,0), Point(2,0,0)]) 


# testing the find_points_to_test
   def test_find_points_to_test_2(self):
      min_x = -4
      max_x = 4
      min_y = -2
      max_y = 2
      width = 4
      height = 4
      self.assertEqual(find_points_to_test(min_x, max_x, min_y, max_y, width, height), [Point(-4,2,0), Point(-2,2,0), Point(0,2,0), Point(2,2,0), Point(-4,1,0), Point(-2,1,0), Point(0,1,0), Point(2,1,0), Point(-4, 0,0), Point(-2,0,0), Point(0, 0,0),Point (2,0,0), Point(-4,-1,0), Point(-2,-1,0), Point(0,-1,0), Point(2,-1,0)]) 

# testing the output of asgn 5
light = Light(Point(-100.0, 100.0, -100.0), Color(1.5,1.5,1.5))
ambient_light= Color(1.0,1.0,1.0)
eye_point = Point(0.0, 0.0, -14.0)
sphere_list = [Sphere(Point(1.0,1.0, 0.0),2.0, Color(0.0,0.0,1.0),Finish(0.2, 0.4, 0.5, 0.05)), Sphere(Point(.5, 1.5, -3.0),.5,Color(1.0,0.0,0.0),Finish(0.4,0.4, 0.5, 0.05))]
cast_all_rays(-10,10 ,-7.5, 7.5, 512, 384, eye_point, sphere_list, ambient_light, light, open("image_final.ppm", "w"))





if __name__ == "__main__":
   unittest.main()
   


