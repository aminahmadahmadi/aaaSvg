from svg import Svg
import math

# Test Code ----------------------------------------
myfile = Svg('myfile', 500, 500)
myfile.addStyle('st0', 'stroke: #bbb; fill: none;')
myfile.addStyle('st1', 'stroke: #f00; fill: none;')
myfile.addStyle('st2', 'stroke: #00f; fill: none;')
myfile.addStyle('st3', 'stroke: #0f0; fill: none;')
myfile.addStyle('st4', 'stroke: #0ff; fill: none;')
no = 10
myfile.openGroup()
for i in range(no):
    myfile.addLine(0, i*(myfile.height/no), myfile.width,
                   i*(myfile.height/no), class_='st0')
    myfile.addLine(i*(myfile.width/no), 0, i*(myfile.width/no),
                   myfile.height, class_='st0')
myfile.closeGroup()

points = []

for i in range(22):
    points.append((round(math.cos(i)*i*10+250, 5),
                   round(math.sin(i)*i*10+250, 5)))

myfile.addBezier(points,  class_='st1')
myfile.addBezier(points, 'q', class_='st2')
myfile.addBezier(points, '', 'smooth', class_='st3')
myfile.addBezier(points, 'q', 'smooth', class_='st4')

myfile.addPolyline(points, class_='st0')
# myfile.addCircle(250, 250, 200, class_='st1')
# myfile.addNormalArc(250, 250, 190, 190, 30, 150, class_='st1')
myfile.save('D:\\KND\\svg')
