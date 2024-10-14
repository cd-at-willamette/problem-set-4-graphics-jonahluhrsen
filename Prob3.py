########################################
# Name: Jonah Luhrsen
# Collaborators: None
# Estimate time spent (hrs): 2
########################################

from pgl import GWindow, GRect, GLabel
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 40                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score

def clicky_box():
    score = 0  # set score to 0

    # create the game window
    gw = GWindow(GW_WIDTH, GW_HEIGHT)

    # create pink square in center
    square = GRect(SQUARE_SIZE, SQUARE_SIZE)
    gw.add(square)
    square.set_location(225, 225)
    square.set_filled(True)
    square.set_fill_color("pink")

    # display the score
    score_label = GLabel(f"{score}")
    score_label.set_font(SCORE_FONT)
    score_label.set_location(SCORE_DX, SCORE_DY + 450)
    gw.add(score_label)

    def on_mouse_down(event): # had help from chatgpt in this aspect, it was very helpful in finding whether the mouse was in the squares coordinates
                              # as well as changing the score
        nonlocal score  #allow access to the score variable

        # get mouse click coordinates
        mouse_x = event.get_x()
        mouse_y = event.get_y()

        # check if the click is within the square
        if (square.get_x() <= mouse_x <= square.get_x() + SQUARE_SIZE and
            square.get_y() <= mouse_y <= square.get_y() + SQUARE_SIZE):
            # move square to a new random location
            new_x = random.randint(0, GW_WIDTH - SQUARE_SIZE)
            new_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
            square.set_location(new_x, new_y)
            score += 1
            score_label.set_label(f"{score}")
        else:
            square.set_location(225, 225)
            score = 0
            score_label.set_label(f"{score}")

    # attach the mouse event listener to the window
    gw.add_event_listener("mousedown", on_mouse_down)

if __name__ == '__main__':
    clicky_box()










if __name__ == '__main__':
    clicky_box()
