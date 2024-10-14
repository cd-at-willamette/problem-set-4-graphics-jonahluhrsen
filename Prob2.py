########################################
# Name: Jonah Luhrsen
# Collaborators: None
# Estimated time spent (hrs): 2
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT)

    # i was struggling with this problem and i consulted chatgpt for help
    # chatgpt was helpful in almost every aspect of this problem and showed me how to correctly determine the starting point
    # as well as drawing the rows correctly
    starting_x = (WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH)) / 2
    starting_y = HEIGHT - BRICK_HEIGHT - 10

    # draw the pyramid row by row
    for row in range(BRICKS_IN_BASE):
        bricks_in_row = BRICKS_IN_BASE - row
        x_center = starting_x + (row * BRICK_WIDTH) / 2

        for brick in range(bricks_in_row):
            x = x_center + brick * BRICK_WIDTH
            y = starting_y - row * BRICK_HEIGHT
            brick_rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            gw.add(brick_rect)

if __name__ == '__main__':
    draw_pyramid()














if __name__ == '__main__':
    draw_pyramid()
