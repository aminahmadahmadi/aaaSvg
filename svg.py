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


# Test Code ----------------------------------------
myfile = Svg('myfile', 100, 100)
myfile.addStyle('bg', 'stroke: #00f; fill: #00f;')
