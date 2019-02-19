class Point:
    pass

def print_point(p):
    print(p.x, p.y)

class Rectangle():
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0
box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0


def find_center(Rectangle):
    p = Point()
    p.x = Rectangle.corner.x + Rectangle.width/2.0
    p.y = Rectangle.corner.y + Rectangle.height/2.0
    return p

center = find_center(box)
print_point(center)

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight

grow_rectangle(box, 50, 100)
print(box.width)
print(box.height)
