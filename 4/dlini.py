
start_point = (10, 30)
sx, sy = start_point

points = [
    (20, 0),
    (40, 0),
    (40, 20)
]

import math
# корень = math.sqrt(x)


#dlini = [ math.sqrt(pow(abs(sx-x), 2) + pow(abs(sy-y), 2)) for x, y in points ]

dlini_1 = [ math.sqrt(pow(sx-x, 2) + pow(sy-y, 2)) for x, y in points ]

dlini_2 = [ math.hypot(sx-x, sy-y) for x, y in points ]



print( dlini_1 )

print( dlini_2 )