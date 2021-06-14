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
            if key == 'style':
                _attrs += f'class="{attrs[key]}" '
            else:
                _attrs += f'{key}="{attrs[key]}" '

        return _attrs

    def addCircle(self, cx, cy, r, **attrs):
        print(attrs)
        circleStr = f'<circle cx="{cx}" cy="{cy}" r="{r}" {Svg.manageAttrs(attrs)}/>'

        print(circleStr)
        self.addObjectText(circleStr)


# Test Code ----------------------------------------
myfile = Svg('myfile', 100, 100)
myfile.addStyle('style', 'stroke: #00f; fill: #00f;')
myfile.addCircle(50, 50, 20, style='style', id='salam', fill='none')
