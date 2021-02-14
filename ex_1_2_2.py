import sys # import sys module for using argv function.
import math # import math module for using sin and cos function. 

a_input = math.sin(int(sys.argv[1])/math.pi) 
b_input = math.cos(int(sys.argv[1])/math.pi)

a = float(a_input)
b = float(b_input)
c = a**2 + b**2

print(c)
