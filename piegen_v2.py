import argparse
import matplotlib.pyplot as plt
import tkinter as tk
from math import cos, sin, radians
from PIL import Image


def cosine(degree):
    return cos(radians(degree))

def sine(degree):
    return sin(radians(degree))

def _create_circle(self, x, y, r, **kwargs):
    return self.create_oval(x-r, y-r, x+r, y+r, **kwargs)
tk.Canvas.create_circle = _create_circle

def _create_circle_arc(self, x, y, r, offset, **kwargs):
    if "start" in kwargs and "end" in kwargs:
        kwargs["extent"] = kwargs["end"] - kwargs["start"]
        kwargs['start'] = kwargs["start"] - offset
        del kwargs["end"]
    return self.create_arc(x-r, y-r, x+r, y+r, **kwargs)

def main():

    def save_as_png(canvas,fileName):
        # save postscipt image 
        canvas.postscript(file = fileName + '.eps') 

    parser = argparse.ArgumentParser(description='Pie Generator. Generates only SVG images.')
    parser.add_argument('-c','--colors',help='List of colors(hexcode without \'#\') for the pie.',nargs='+',required=True)
    parser.add_argument('-t','--types',help='List of colors(hexcode without \'#\') for the pie.',nargs='+',required=True)
    parser.add_argument('-o','--out',help='Outfile path.',required=True)

    args = parser.parse_args()

    colors = ['#'+col for col in args.colors]
    types = args.types

    if len(colors) != len(types):
        exit(1)

    root = tk.Tk()
    canvas = tk.Canvas(root, width=450, height=450, borderwidth=0, highlightthickness=0, bg=None)
    canvas.grid()
    tk.Canvas.create_circle_arc = _create_circle_arc

    total_colors = len(colors)
    step = int(360.0/total_colors)
    width = 2.5
    center_x, center_y = 225, 225
    radius = 200
    sub_step = 30

    canvas.create_circle(center_x, center_y, radius, fill="", outline="#DDD", width=0)
    
    for i, (color, color_type) in enumerate(zip(colors, types)):
        
        if color_type=='d':
            
            canvas.create_circle_arc(center_x, center_y, radius, 90 - step, fill=color, outline="", start=i*step, end=i*step + sub_step-width)
            canvas.create_circle_arc(center_x, center_y, radius, 90 - step, fill=color, outline="", start=(i + 1)*step - sub_step + width, end=(i+1)*step)

            num_sub_steps = int(step/30.0)
            for j in range(1, num_sub_steps-1):
                canvas.create_circle_arc(center_x, center_y, radius, 90 - step, fill=color, outline="", start=i*step+j*sub_step+width, end=i*step+(j+1)*sub_step-width)
        else:
            canvas.create_circle_arc(center_x, center_y, radius, 90 - step, fill=color, outline="", start=i*step, end=(i+1)*step)
    canvas.pack()
    root.wm_title("Circles and Arcs")
    #root.mainloop()

    canvas.update()
    save_as_png(canvas, args.out)
    root.mainloop()

if __name__ == '__main__':
    main()