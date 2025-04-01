from turtle import *
from turtlesc import *


def draw_cube(size=100, border='black', top='#E7E7E7', right='#A4A4A4', left='#C6C6C6', skip_left_size=False):
    # Top side:
    sc(f'''
        pc {border}, fc {top}, pd, bf, r 30, f {size}, r 120, f {size}
        r 60, f {size}, r 120, f {size}, r 30, ef
        ''')
    
    # Right side:
    sc(f'''
        pu, r 30, f {size}, pd, fc {right}, bf, r 60, f {size}, r 60, f {size}, r 120, f {size}, r 60, f {size}, ef
        ''')
    
    if not skip_left_size:
        # Left side: 
        sc(f'''
            pu, b {size}, r 120, fc {left}, pd, bf, f {size}, r 120, f {size}, r 60, f {size}, r 120, f {size}, ef
            ''')
    
    # Return to top point:
    sc(f'''
        pu, b {size}, l 60, f {size}, r 30
        ''')

def draw_omöjlig_figur(size=100, border='black', top='#E7E7E7', right='#A4A4A4', left='#C6C6C6'):
    sc(f'pu, l 30, f {int(size * 1.5)}, r 30') # move from bottom cube to neighboring right cube's top point.
    sc(f'pu, l 30, f {int(size * 1.5)}, r 30')
    draw_cube(size=size, border=border, top=top, right=right, left=left)
    sc(f'pu, l 30, b {int(size * 1.5)}, r 30')

    # left side of cubes
    for i in range(3):
        draw_cube(size=size, border=border, top=top, right=right, left=left)
        sc(f'pu, l 90, f {int(size * 1.5)}, r 90')


    # top right side of cubes
    for i in range(3):
        draw_cube(size=size, border=border, top=top, right=right, left=left)
        sc(f'pu, r 30, f {int(size * 1.5)}, l 30')
    draw_cube(size=size)

    # bottom right side of cubes
    sc(f'l 30, b {int(size * 1.5)}, r 30')
    draw_cube(size=size, border=border, top=top, right=right, left=left, skip_left_size=True)

    # left off at 60 north of right, top point
    sc(f'pu, r 30, b {size}, pd, r 60, fc {left}, bf, f {size}, r 60, f {size}')
    sc(f'r 120, f {int(size * 0.5)}, r 60, f {int(size * 0.5)}, l 60, f {int(size * 0.5)}, r 60, f {int(size * 0.5)}, ef')

    sc(f'pu, r 60, b {size * 2}, r 30')


sc('t 1 0, pu, b 300, l 90, b 150, r 90') # put turtle into position of bottom cube's top point
draw_omöjlig_figur()
done()

