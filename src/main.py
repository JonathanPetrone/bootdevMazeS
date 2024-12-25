from window import *

def main():
    print("Maze solver")
    # Step 1: Create points
    start_point = Point(5, 5)
    end_point = Point(5, 25)

    # Step 2: Create a line
    line = Line(start_point, end_point)
    line2 = Line(Point(5, 5), Point(25, 5))

    # Step 3: Create a window
    window = Window(500, 500)

    # Step 4: Draw the line
    window.draw_line(line, 'blue')
    window.draw_line(line2, 'blue')

    # Step 5: Wait for close
    window.wait_for_close()

main()