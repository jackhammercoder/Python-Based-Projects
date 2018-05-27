from sys import *
from cast import *
def get_spheres(file):
   try:
      file = open(argv[1], "r")
   except:
      print "come on Paul! your gonna have to do better than that! that file doesn't exist" + "\n" + "usage: python ray_caster.py <filename> [-eye x, y, z] [-view min_x max_x min_y max_y width height] [-light x y z r g b] [-ambient r g b]"
      exit()
   spot = 1
   list = []
   for line in file:
      values = line.split()
      if len(values) == 11:
         try:
            sphere = Sphere(Point(float(values[0]),float(values[1]), float(values[2])),float(values[3]), Color(float(values[4]),float(values[5]), float(values[6])), Finish(float(values[7]), float(values[8]), float(values[9]), float(values[10])))
            list.append(sphere)
            spot += 1
         except:
            print "malformed sphere on line" + " " + str(spot) + " " + "...skipping"
            spot += 1
      else:
         print "malformed sphere on line" + " " + str(spot) + " " + "...skipping"
         spot += 1
   return list

def get_cmd_line_params(argv):
   param = []
   if "-eye" in argv:
      i = argv.index("-eye")
      try:
         e = argv[i+3]
         try:
            e1 = float(argv[i+1])
         except:
            e1 = 0.0
            print "the x value of the eyepoint you entered is not a float/int type ... using the defualt value of 0.0"
         try:
            e2 = float(argv[i+2])
         except: 
            e2 = 0.0
            print "the y value of the eyepoint you entered is not a float/int type ... using the defualt value of 0.0"
         try:
            e3 = float(e)
         except:
            e3 = -14.0
            print "the z value of the eyepoint you entered is not a float/int type ... using defualt value of -14.0"
         eye_point = Point(e1,e2,e3)
      except:
         eye_point = Point(0,0,-14)
         print "your user defined eyepoint was missing a z component ... using the default eyepoint"
      param.append(eye_point)
   else: 
      eye_point = Point(0,0,-14)
      print "-eye flag not found, so using default eye: Point(0,0,-14)"
      param.append(eye_point) 

   if "-view" in argv:
      j= argv.index("-view")
      try:
         v = argv[j+6]
         try:
            param.append(float(argv[j+1]))
         except:
            param.append(-10.0)
            print "the min_x value of the view window  you entered is not a float/int type ... using the defualt value of -10"
         try:
            param.append(float(argv[j+2]))
         except: 
            param.append(10.0)
            print "the max_x value of the view window you entered is not a float/int type ... using the defualt value of 10.0"
         try:
            param.append(float(argv[j+3]))
         except:
            param.append(-7.5)
            print "the min_y value of the view window  you entered is not a float/int type ... using defualt value of -7.5"
         try:
            param.append(float(argv[j+4]))
         except:
            param.append(7.5)
            print "the max_y value of the view window  you entered is not a float/int type ... using defualt value of 7.5"
         try:
            param.append(int(argv[j+5]))
         except:
            param.append(512)
            print "the width of the view window  you entered is not a float/int type ... using defualt value of 512"
         try:
            param.append(int(v))
         except:
            param.append(384)
            print "the height of the view window  you entered is not a float/int type ... using defualt value of 384"
      except:
         param.append(-10.0)
         param.append(10.0)
         param.append(-7.5)
         param.append(7.5)
         param.append(512)
         param.append(384)
         print "your user defined window was missing a value ... using the default window"
   else: 
       param.append(-10.0)
       param.append(10.0)
       param.append(-7.5)
       param.append(7.5)
       param.append(512)
       param.append(384)
       print "no -view flag found using defualt window"

   if "-light" in argv:
      k= argv.index("-light")
      try:
         l = argv[k+6]
         try:
            l1 = float(argv[k+1])
         except:
            l1 = -100.0
            print "the x  value of the light position  you entered is not a float/int type ... using the defualt value of -100.0"
         try:
            l2 = float(argv[k+2])
         except: 
            l2 = 100.0
            print "the y value of the light position you entered is not a float/int type ... using the defualt value of 100.0"
         try:
            l3 = float(argv[k+3])
         except:
            l3 = -100.0
            print "the z value of the light posistion you entered is not a float/int type ... using defualt value of -100.0"
         try:
            r = float(argv[k+4])
         except:
            r = 1.5
            print "the red value of the color light  you entered is not a float/int type ... using defualt value of 1.5"
         try:
            g = float(argv[k+5])
         except:
            g = 1.5
            print "the green value of the color light  you entered is not a float/int type ... using defualt value of 1.5"
         try:
            b = float(l)
         except:
            b = 1.5
            print "the blue value of the color light you entered is not a float/int type ... using defualt value of 1.5"
         light = Light(Point(l1,l2,l3),Color(r,g,b))
      except:
         light = Light(Point(-100.0, 100.0, -100.0), Color(1.5,1.5,1.5))
         print "your user defined window was missing a value ... using the default light source"
      param.append(light)  
   else: 
       light = Light(Point(-100.0, 100.0, -100.0), Color(1.5,1.5,1.5))
       param.append(light)
       print "no -light found using defualt light source"

   if "-ambient" in argv:
      q = argv.index("-ambient")
      try:
         a = argv[q+3]
         try:
            a1 = float(argv[q+1])
         except:
            a1 = 1.0
            print "the red value of the ambient light you entered is not a float/int type ... using the defualt value of 1.0"
         try:
            a2 = float(argv[q+2])
         except: 
            a2 = 1.0
            print "the green value of the ambient light you entered is not a float/int type ... using the defualt value of 1.0"
         try:
            a3 = float(a)
         except:
            a3 = 1.0
            print "the blue value of the ambient light you entered is not a float/int type ... using defualt value of 1.0"
         ambient = Color(a1,a2,a3) 
      except:
         ambient = Color(1.0,1.0,1.0)
         print "your user defined ambient light  was missing a value ... using the default ambient light"
      param.append(ambient)
   else: 
      ambient = Color(1.0,1.0,1.0)
      print "-ambient flag not found, so using default ambient light: Color(1.0,1.0,1.0)" 
      param.append(ambient)

   return param
      
     
         
