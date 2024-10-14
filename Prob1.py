############################################################
# Name: Jonah Luhrsen
# Name(s) of anyone worked with: None
# Est time spent (hr): 1r
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    gw = GWindow(WIDTH, HEIGHT)
    
    r = GRect(0,0,600,600)
    r.set_filled(True)
    r.set_fill_color("blue")
    r.set_color("blue")
    gw.add(r) 
    
    r = GRect(200,300,200,100)
    r.set_filled(True)
    r.set_fill_color("red")
    r.set_color("red")
    gw.add(r) 

    r = GRect(200,280,100,100)
    r.set_filled(True)
    r.set_fill_color("red")
    r.set_color("red")
    gw.add(r) 
    
    r = GRect(220,300,60,50)
    r.set_filled(True)
    r.set_fill_color("lightblue")
    gw.add(r) 

    o = GOval(340,400,40,40)
    o.set_filled(True)
    o.set_fill_color("black")
    gw.add(o)

    o = GOval(220,400,40,40)
    o.set_filled(True)
    o.set_fill_color("black")
    gw.add(o)

    r = GRect(0,440,600,220)
    r.set_filled(True)
    r.set_fill_color("grey")
    r.set_color("grey")
    gw.add(r) 

    o = GOval(20,20,80,80)
    o.set_filled(True)
    o.set_fill_color("yellow")
    o.set_color("orange")
    gw.add(o)

    l = GLine(0, 520, 600, 520)
    gw.add(l)

    lb = GLabel("Dream Car", 200, 240)
    gw.add(lb)

if __name__ == '__main__':
    draw_image()



if __name__ == '__main__':
    draw_image()
