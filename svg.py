from typing import MutableMapping


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


# Test Code ----------------------------------------
myfile = Svg('myfile', 100, 100)
myfile.addStyle('st1', 'stroke: #f00; fill: #00f;')
myfile.addCircle(50, 50, 20, class_='st1', id='salam', fill='none')
