class Result:
    def __init__(self):
        self.circles = []
        self.qrcodes = []

    def add_qr(self, text, p1, p2, p3, p4):
        qr = {'text': text, 'points': [p1, p2, p3, p4]}
        self.qrcodes.append(qr)

    def add_circle(self, center, radius):
        circle = {'center': center, 'radius': radius}
        self.circles.append(circle)
