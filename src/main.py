from window import *

def main():
    print("Maze solver")
    
    win = Window(800, 600)
    maze = Maze(100, 100, 10, 10, 50, 50, win)
    win.wait_for_close()

main()