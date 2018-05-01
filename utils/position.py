def in_rectangle(lines, point):
    if lines['top_line']['function'](point[0], point[1])>=0 and\
       lines['right_line']['function'](point[0], point[1])>=0 and\
       lines['down_line']['function'](point[0], point[1])>=0 and\
       lines['left_line']['function'](point[0], point[1])>=0: return True
    else: return False