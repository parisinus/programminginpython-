import sys

a = sys.argv[1]
b = sys.argv[2]

a_int = int(a)
b_int = int(b)

if (a_int % b_int) == 0 or (b_int % a_int) == 0:
    print("True")
else:
    print("False")
