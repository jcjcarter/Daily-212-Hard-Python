import re
from itertools import chain

height = int(input())
lines = [input().strip() for n in range(height)]
width = max(len(x) for x in lines)


routes = {(x,y)
          for x in range(width)
          for y in range(height)
          if lines[y][x].isspace()
    }

raw_path = input().strip()
path = list(chain.from_iterable(
    
    {'l': lambda _: [lambda x, y, dx, dy: (x,y,dy, -dx)],
     'r': lambda _:[lambda x,y, dx,dy: (x,y,-y, dx)]}
    .get(entry, lambda ct: [lambda x, y, dx, dy: (x +dx,
                                                  y + dy,
                                                  dx, dy)] * int(ct))
    (entry)
    for entry in re.findall('[rl]|[0-9]+', raw_path)
    ))

for start_x, start_y in routes:
    for dx, dy in ((0,1), (1,0), (0,-1), (-1,0)):
        x = start_x
        y = start_y
        for instruction in path:
            x, y, dx, dy = instruction(x, y, dx, dy)
            if (x,y) not in routes:
                break
            else:
                print('From ({},{}) to ({}, {})'.format(start_x,
                                                        start_y,
                                                        x,y))