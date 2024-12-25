from window import *

def main():
    print("Maze solver")
    
    win = Window(800, 600)
    maze = Maze(100, 100, 10, 10, 50, 50, win)

    # Modify the entrance and exit immediately after the maze is created
    maze._break_entrance_and_exit()
    
    # Start the window loop after making all necessary changes
    win.wait_for_close()

main()