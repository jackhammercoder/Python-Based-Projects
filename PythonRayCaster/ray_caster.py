from sys import *
from cast import *
from commandline import *

def main():
   try:
      sphere_list = get_spheres(file)
      cmd = get_cmd_line_params(argv)
      cast_all_rays(cmd[1], cmd[2], cmd[3], cmd[4], cmd[5], cmd[6], cmd[0], sphere_list, cmd[8], cmd[7], file)

   except:
      print "error - make sure you specified an input file in the command file"
      exit()


if __name__ == "__main__":
   main()















