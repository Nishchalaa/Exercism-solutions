def equilateral(sides):
    a,b,c = sides
    return a == b == c !=0 and a + b >= c and b + c >= a and a + c >= b


def isosceles(sides):
    a, b, c = sides
    return (a == b or b == c or c == a) and a + b >= c and a + c >= b and b + c >= a



def scalene(sides):
    a,b,c = sides
    return a!=b and b!=c and c!=a and a + b >= c and a + c >= b and b + c >= a
