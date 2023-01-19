a=float(input("Enter the side:"))
s_area=lambda a : a * a
print("area of square:",s_area(a))
l=float(input("Enter the length:"))
w=float(input("Enter the width:"))
r_area=lambda l,w : l * w
print("area of rectangle:",r_area(l,w))
b=float(input("Enter the base:"))
h=float(input("Enter the height:"))
t_area=lambda b,h : (h * b)/2
print("area of triangle:",t_area(b,h))
