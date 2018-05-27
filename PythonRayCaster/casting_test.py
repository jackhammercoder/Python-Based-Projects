from cast import *
print 'P3'

width = 512
height = 384

print width, height
print 255

light = Light(Point(-100.0, 100.0, -100.0), Color(1.5,1.5,1.5))
ambient_light= Color(1.0,1.0,1.0)
eye_point = Point(0.0, 0.0, -14.0)
sphere_list = [Sphere(Point(1.0,1.0, 0.0),2.0, Color(0.0,0.0,1.0),Finish(0.2, 0.4, 0.5, 0.05)), Sphere(Point(.5, 1.5, -3.0),.5,Color(1.0,0.0,0.0),Finish(0.4,0.4, 0.5, 0.05))]
cast_all_rays(-10,10 ,-7.5, 7.5, width, height, eye_point, sphere_list, ambient_light, light)
 
