import math

a = input('Enter numeric argument:')
a_float = float(a)


a_sin = math.sin(a_float)
a_cos = math.cos(a_float)

c = a_sin**2 +a_cos**2
print(c)

# actually we don't need sys module in this case. 
