from math import sin, cos, radians


class Svg:
    count = 0

    def __init__(self, name, w, h):
        self.name = name
        self.width = w
        self.height = h
        self.styles = []
        self.objects = []
        Svg.count += 1

    def addStyle(self, className, css):
        self.styles.append(f'.{className} {{{css}}}')
        print(self.styles[-1])

    def addObjectText(self, objText):
        self.objects.append(objText)

    def save(self, direction):
        self.svg = [
            f'<svg width="{self.width}" height="{self.height}" version="1.1" xmlns="http://www.w3.org/2000/svg">',
            '<style type="text/css" >',
            '\n'.join(self.styles),
            '</style>',
            '<g>',
            '\n'.join(self.objects),
            '</g>',
            '</svg>',
        ]
        svgFile = open(direction+'\\'+self.name + '.svg', "w")
        svgFile.write('\n'.join(self.svg))
        svgFile.close()

    def manageAttrs(attrs):
        _attrs = ''
        for key in attrs.keys():
            if key == 'class_':
                _attrs += f'class="{attrs[key]}" '
            else:
                _attrs += f'{key}="{attrs[key]}" '

        return _attrs

    def managePoints(points):
        _points = ''
        for point in points:
            _points += f'{point[0]},{point[1]} '

        return _points

    def addCircle(self, cx, cy, r, **attrs):
        circleStr = f'<circle cx="{cx}" cy="{cy}" r="{r}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(circleStr)

    def addRect(self, x, y, w, h, **attrs):
        rectStr = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(rectStr)

    def addEllipse(self, cx, cy, rx, ry, **attrs):
        ellipseStr = f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(ellipseStr)

    def addLine(self, x1, y1, x2, y2, **attrs):
        lineStr = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(lineStr)

    def addPolygon(self, points, **attrs):
        polygonStr = f'<polygon points="{Svg.managePoints(points)}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(polygonStr)

    def addPolyline(self, points, **attrs):
        polylineStr = f'<polyline points="{Svg.managePoints(points)}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(polylineStr)

    def addNormalArc(self, cx, cy, rx, ry, startDegree, endDegree, **attrs):
        _start = (cx + rx * cos(radians(startDegree)),
                  cy - ry * sin(radians(startDegree)))
        _end = (cx + rx * cos(radians(endDegree)),
                cy - ry * sin(radians(endDegree)))
        sweepFlag = 0 if endDegree > startDegree else 1
        largeArcFlag = 0 if endDegree - startDegree < 180 else 1
        print(startDegree, ' --> ', endDegree, ' | ', endDegree > startDegree,
              sweepFlag, endDegree-startDegree > 180, largeArcFlag)
        arcStr = f'<path d="M {_start[0]},{_start[1]} A {rx},{ry} 0 {largeArcFlag} {sweepFlag} {_end[0]},{_end[1]}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(arcStr)


# Test Code ----------------------------------------
myfile = Svg('myfile', 500, 500)
myfile.addStyle('st1', 'stroke: #f00; fill: none;')
myfile.addCircle(250, 250, 200, class_='st1')
myfile.addNormalArc(250, 250, 190, 190, 30, 150, class_='st1')
myfile.save('C:\\Users\\Amin\\Desktop\\svg')
