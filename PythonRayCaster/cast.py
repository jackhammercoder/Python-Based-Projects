from collisions import *
from data import *
from vector_math import *

def cast_ray(ray, sphere_list, color, light):
   test_list = find_intersection_points(sphere_list, ray)
   if test_list != []:
      final_list = []
      for (s,p) in test_list:
        N = sphere_normal_at_point(s,p)
        scaled_N = scale_vector(N, .01)
        pe = translate_point(p, scaled_N)
        Ldir = normalize_vector(vector_from_to(pe, light.point))
        dot_prod = dot_vector(N, Ldir)
        ref_vec = difference_vector(Ldir,  scale_vector( N, (2*dot_prod)))
        vdir = normalize_vector(vector_from_to(ray.pt, pe))
        spec_inten = dot_vector(ref_vec, vdir)
        ray_to_light = find_intersection_points(sphere_list, Ray(pe, vector_from_to(pe, light.point)))
        final_list.append((s,p,pe, dot_prod, ray_to_light, spec_inten))
      closest_tuple = final_list[0]
      for (s, p, pe, dot_prod, ray_to_light, spec_inten) in final_list:
         if length_vector(vector_from_to(ray.pt, p)) <= length_vector(vector_from_to(ray.pt, closest_tuple[1])):
            closest_tuple = (s, p , pe, dot_prod, ray_to_light, spec_inten)
         else: 
            closest_tuple = closest_tuple
      amb = closest_tuple[0].finish.ambient
      obs_color = Color(closest_tuple[0].color.red*amb*color.red, 
                        closest_tuple[0].color.green*amb*color.green, 
                        closest_tuple[0].color.blue*amb*color.blue)
      if closest_tuple[3] <= 0 or closest_tuple[4] != []:
         return obs_color
      else:
         diffuse = closest_tuple[0].finish.diffuse
         obs_color_2 =  Color(obs_color.red + (closest_tuple[3]*light.color.red*closest_tuple[0].color.red*diffuse), 
                              obs_color.green + (closest_tuple[3]*light.color.green*closest_tuple[0].color.green*diffuse), 
                              obs_color.blue + (closest_tuple[3]*light.color.blue*closest_tuple[0].color.blue*diffuse))
         if closest_tuple[5] <= 0: 
            return obs_color_2
         else:
            specular = (closest_tuple[0].finish.specular) * ((closest_tuple[5])**(1/closest_tuple[0].finish.roughness))
            return Color(obs_color_2.red + ((light.color.red) * specular), 
                         obs_color_2.green + ((light.color.green) * specular), 
                         obs_color_2.blue + ((light.color.blue) * specular))
   else:
      return Color(1.0, 1.0, 1.0)

def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, color, light, file):
   file = open("image.ppm", "w")
   file.write("P3" + "\n" + str(width) + " " + str(height) + "\n" + "255" + "\n" + "\n" )
   ray_list = []
   left_upper_corners = find_points_to_test(min_x, max_x, min_y, max_y, width, height)
   for point in left_upper_corners:
      ray_list.append(Ray(eye_point, vector_from_to(eye_point, point)))
   for ray in ray_list:
      result = cast_ray(ray, sphere_list, color, light)
      if result  == Color(1.0, 1.0, 1.0):
         file.write(str(int(255*1.0)) + " " + str(int(255*1.0)) + " " + str(int(255*1.0)) + "\n")
      else:
         red = result.red*255
         green = result.green*255
         blue = result.blue*255
         if result.red <= 1.0 and result.green <= 1.0 and result.blue <= 1.0:
            file.write(str(int(red)) + " " + str(int(green)) + " " + str(int(blue)) + "\n") 
         else:
            if red > 255:
               red = 255
            if green > 255:
               green = 255
            if blue > 255:
               blue = 255
            file.write(str(int(red)) + " " + str(int(green)) + " " + str(int(blue)) + "\n") 
   


def find_points_to_test(min_x, max_x, min_y, max_y, width, height):
   x1 = float(min_x)
   x2 = float(max_x)
   y1 = float(min_y)
   y2 = float(max_y)
   width_int = int(width)
   height_int = int(height)
   change_in_x = (x2 - x1)/width
   change_in_y = (y2 - y1)/height
   reference = Point(x1, y2, 0.0)
   list = []
   for spot_y in range(height_int):
      for spot_x in range(width_int):
         list.append(Point(reference.x + spot_x*(change_in_x), reference.y - spot_y*(change_in_y), 0.0))
   return list


