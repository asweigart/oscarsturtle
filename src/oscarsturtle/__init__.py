from turtle import *
from turtlesc import *
from random import *


def draw_cube(size=100, border='black', top_color='#E7E7E7', right_color='#A4A4A4', left_color='#C6C6C6', skip_left_side=False):
    # Top side:
    sc(f'''
        pc {border}, fc {top_color}, pd, bf, r 30, f {size}, r 120, f {size}
        r 60, f {size}, r 120, f {size}, r 30, ef
        ''')
    
    # Right side:
    sc(f'''
        pu, r 30, f {size}, pd, fc {right_color}, bf, r 60, f {size}, r 60, f {size}, r 120, f {size}, r 60, f {size}, ef
        ''')
    
    if not skip_left_side:
        # Left side: 
        sc(f'''
            pu, b {size}, r 120, fc {left_color}, pd, bf, f {size}, r 120, f {size}, r 60, f {size}, r 120, f {size}, ef
            ''')
    
    # Return to top point:
    sc(f'''
        pu, b {size}, l 60, f {size}, r 30
        ''')


def draw_omojlig_figur(size=100, border='black', top_color='#E7E7E7', right_color='#A4A4A4', left_color='#C6C6C6'):
    sc(f'pu, l 30, f {int(size * 1.5)}, r 30') # move from bottom cube to neighboring right cube's top point.
    sc(f'pu, l 30, f {int(size * 1.5)}, r 30')
    draw_cube(size=size, border=border, top_color=top_color, right_color=right_color, left_color=left_color)
    sc(f'pu, l 30, b {int(size * 1.5)}, r 30')

    # left side of cubes
    for i in range(3):
        draw_cube(size=size, border=border, top_color=top_color, right_color=right_color, left_color=left_color)
        sc(f'pu, l 90, f {int(size * 1.5)}, r 90')


    # top right side of cubes
    for i in range(3):
        draw_cube(size=size, border=border, top_color=top_color, right_color=right_color, left_color=left_color)
        sc(f'pu, r 30, f {int(size * 1.5)}, l 30')
    draw_cube(size=size, border=border, top_color=top_color, right_color=right_color, left_color=left_color)

    # bottom right side of cubes
    sc(f'l 30, b {int(size * 1.5)}, r 30')
    draw_cube(size=size, border=border, top_color=top_color, right_color=right_color, left_color=left_color, skip_left_side=True)

    # left off at 60 north of right, top point
    sc(f'pu, r 30, b {size}, pd, r 60, fc {left_color}, bf, f {size}, r 60, f {size}')
    sc(f'r 120, f {int(size * 0.5)}, r 60, f {int(size * 0.5)}, l 60, f {int(size * 0.5)}, r 60, f {int(size * 0.5)}, ef')

    sc(f'pu, r 60, b {size * 2}, r 30')

def draw_one_plain_omojlig_figur():
    hideturtle()
    sc('h, t 1 0, pu, b 300, l 90, b 150, r 90') # put turtle into position of bottom cube's top point
    draw_omojlig_figur()
    done()

def random_color():
    return f'{round(random(), 2)} {round(random(), 2)} {round(random(), 2)}'

def draw_scene_omojlig_figur():
    hideturtle()
    tracer(10000, 0)
    for i in range(30):
        penup()
        goto(randint(-200, 200), randint(-200, 200))
        left(randint(0,360))
        draw_omojlig_figur(size=randint(20, 60), top_color=random_color(), left_color=random_color(), right_color=random_color())

    update()
    done()

if __name__ == '__main__':
    #draw_one_plain_omojlig_figur()
    draw_scene_omojlig_figur()
    