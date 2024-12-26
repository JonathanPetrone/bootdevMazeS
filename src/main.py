from window import *

def main():
    # Define variables for size and window
    num_rows, num_cols = 10, 10
    cell_size = 50
    window = Window(num_cols * cell_size + 20, num_rows * cell_size + 20)

    # Create the maze with x1, y1 as starting positions
    maze = Maze(0, 0, num_rows, num_cols, cell_size, cell_size, window)

    # Invoke the draw function
    maze.draw_maze()
  
    window.wait_for_close()

if __name__ == "__main__":
    main()