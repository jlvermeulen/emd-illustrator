import tkinter as tk

from geometry import *

class Visualiser(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.canvas = tk.Canvas(self, bg = 'white')
        self.canvas.pack(fill = 'both', expand = 1)

    def draw_point_(self, point, r, colour):
        self.canvas.create_oval(point.x - r, point.y - r, point.x + r, point.y + r, fill = colour)

    def draw_point(self, point):
        self.draw_point_(point, 2, 'black')

    def draw_segment_(self, segment, r, colour):
        self.canvas.create_line(segment.start.x, segment.start.y, segment.end.x, segment.end.y, fill = colour)
        if r > 0:
            self.draw_point_(segment.start, r, colour)
            self.draw_point_(segment.end, r, colour)

    def draw_segment(self, segment):
        self.draw_segment_(segment, 1, 'black')

    def draw_flow(self, source, sink):
        self.draw_segment_(Segment(source, sink), 0, 'red')

    def clear(self):
        self.canvas.delete('all')