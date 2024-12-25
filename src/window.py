from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.root = Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.title("Main Tkinter Window")
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()
        self.window_running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.window_running = True
        while self.window_running == True:
            self.redraw()

    def close(self):
        self.window_running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)



class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point_1, point_2):
        self.p1 = point_1
        self.p2 = point_2
    
    def draw(self, canvas, fill_color):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y

        canvas.create_line(
            x1, y1, x2, y2, fill=fill_color, width=2
        )