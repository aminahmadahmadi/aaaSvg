from math import sin, cos, radians
import numpy as np


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

    def addObjectText(self, objText):
        self.objects.append(objText)

    def openGroup(self):
        self.addObjectText('<g>')

    def closeGroup(self):
        self.addObjectText('</g>')

    def save(self, direction):
        self.svg = [
            f'<svg width="{self.width}" height="{self.height}" version="1.1" xmlns="http://www.w3.org/2000/svg">',
            '<style type="text/css" >',
            '\n'.join(self.styles),
            '</style>',
            '\n'.join(self.objects),
            '</svg>',
        ]
        svgFile = open(direction+'\\'+self.name + '.svg', "w")
        svgFile.write('\n'.join(self.svg))
        svgFile.close()

    def clearAttrs(attrs):
        for _ in range(20):
            if '_attrs' in attrs.keys():
                attrs = attrs['_attrs']
            else:
                break
        return attrs

    def manageAttrs(attrs):
        attrs = Svg.clearAttrs(attrs)

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
        arcStr = f'<path d="M {_start[0]},{_start[1]} A {rx},{ry} 0 {largeArcFlag} {sweepFlag} {_end[0]},{_end[1]}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(arcStr)

    def addArc(self, x1, y1, rx, ry, xAxisRotation, largeArcFlag, sweepFlag, x2, y2, **attrs):
        arcStr = f'<path d="M {x1},{y1} A {rx},{ry} {xAxisRotation} {largeArcFlag} {sweepFlag} {x2},{y2}" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(arcStr)

    def addBezier(self, points, *data, **attrs):
        if len(data) == 0:
            data = ('', '')
        elif len(data) == 1:
            data = (data[0], '')

        bezierStr = '<path d="'
        if data[0] == 'q':
            if data[1] == 'smooth':  # quadric smooth
                for i in range(len(points)):
                    if i == 0:
                        bezierStr += f'M {points[i][0]},{points[i][1]}'
                    elif i == 1:
                        bezierStr += f' Q {points[i][0]},{points[i][1]}'
                    elif i == 2:
                        bezierStr += f' {points[i][0]},{points[i][1]}'
                    else:
                        bezierStr += f' T {points[i][0]},{points[i][1]}'

            else:  # quadric normal
                for i in range(len(points)):
                    if i == 0:
                        bezierStr += f'M {points[i][0]},{points[i][1]}'
                    elif i % 2 == 1:
                        bezierStr += f' Q {points[i][0]},{points[i][1]}'
                    else:
                        bezierStr += f' {points[i][0]},{points[i][1]}'

        else:
            if data[1] == 'smooth':  # cubic smooth
                for i in range(len(points)):
                    if i == 0:
                        bezierStr += f'M {points[i][0]},{points[i][1]}'
                    elif i == 1:
                        bezierStr += f' C {points[i][0]},{points[i][1]}'
                    elif i == 2:
                        bezierStr += f' {points[i][0]},{points[i][1]}'
                    elif i == 3:
                        bezierStr += f' {points[i][0]},{points[i][1]}'
                    elif i % 2 == 0:
                        bezierStr += f' S {points[i][0]},{points[i][1]}'
                    else:
                        bezierStr += f' {points[i][0]},{points[i][1]}'

            else:  # cubic normal
                for i in range(len(points)):
                    if i == 0:
                        bezierStr += f'M {points[i][0]},{points[i][1]}'
                    elif i % 3 == 1:
                        bezierStr += f' C {points[i][0]},{points[i][1]}'
                    elif i % 3 == 2:
                        bezierStr += f' {points[i][0]},{points[i][1]}'
                    else:
                        bezierStr += f' {points[i][0]},{points[i][1]}'

        bezierStr += f'" {Svg.manageAttrs(attrs)}/>'
        self.addObjectText(bezierStr)

    def addCurve(self, points, **attrs):
        if (len(points) < 2):
            return

        scl = 0.25
        if 'scl' in attrs.keys():
            scl = attrs['scl']
        controlPoints = []

        for i in range(len(points)):
            if (i == 0):  # first
                p1 = np.array(points[i])
                p2 = np.array(points[i+1])

                tangent = p2 - p1
                q1 = p1 + scl * tangent

                controlPoints.append(p1)
                controlPoints.append(q1)

            elif (i == len(points) - 1):  # last
                p0 = np.array(points[i-1])
                p1 = np.array(points[i])

                tangent = (p1 - p0)
                q0 = p1 - scl * tangent

                controlPoints.append(q0)
                controlPoints.append(p1)

            else:
                p0 = np.array(points[i - 1])
                p1 = np.array(points[i])
                p2 = np.array(points[i + 1])

                tangent = (p2 - p0)/np.linalg.norm(p2 - p0)
                q0 = p1 - scl * tangent * np.linalg.norm(p1 - p0)
                q1 = p1 + scl * tangent * np.linalg.norm(p2 - p1)

                controlPoints.append(q0)
                controlPoints.append(p1)
                controlPoints.append(q1)

        controlPoints = controlPoints[3:-3]
        self.addBezier(controlPoints, _attrs=attrs)

    def addCloseCurve(self, points, **attrs):
        if points[0] == points[-1]:
            points = [points[-2]] + points + [points[1]]
        else:
            points = points[-2:] + points + points[:2]

        self.addCurve(points, _attrs=attrs)
