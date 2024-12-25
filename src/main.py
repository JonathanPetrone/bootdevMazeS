from window import *

def main():
    print("Maze solver")
    # Create a window instance
    win = Window(400, 400)

    # Define points for your cells
    top_left = Point(50, 50)
    bottom_right = Point(100, 100)

    # Create one or more cell instances
    cell1 = Cell(top_left, bottom_right, win)
    cell2 = Cell(Point(100, 50), Point(150, 100), win)

    # Draw your cell(s) on the canvas
    cell1.draw()
    cell2.draw()

    # Hold the window open until closed by the user
    win.wait_for_close()

main()