def points_to_lines(all_points):
    
    def line(p1, p2):
        def pre_line(x,y):
            return (p1[1]-p2[1])*x + (p2[0]-p1[0])*y + (p1[0]*p2[1]-p2[0]*p1[1])
        return pre_line
    
    top_line = line(all_points[0][0], all_points[0][1])
    down_line = line(all_points[0][2], all_points[0][3])
    right_line = line(all_points[0][1], all_points[0][2])
    left_line = line(all_points[0][3], all_points[0][0])
    red_up_line = line(all_points[1][0], all_points[1][1])
    blue_down_line = line(all_points[2][0], all_points[2][1])
    
    return {'top_line': {'function': top_line, 'coordinates':[(all_points[0][0]),(all_points[0][1])]}, 
            'down_line': {'function': down_line, 'coordinates':[(all_points[0][2]),(all_points[0][3])]},
            'right_line': {'function': right_line, 'coordinates':[(all_points[0][1]),(all_points[0][2])]},
            'left_line': {'function': left_line, 'coordinates':[(all_points[0][3]),(all_points[0][0])]},
            'red_up_line': {'function': red_up_line, 'coordinates':[(all_points[1][0]),(all_points[1][1])]},
            'blue_down_line': {'function': blue_down_line, 'coordinates':[(all_points[2][0]),(all_points[2][1])]}}

def rect_to_point_for_line(rectangle):
        w = abs(rectangle[0][0] - rectangle[1][0])
        h = abs(rectangle[0][1] - rectangle[1][1])
        tlpoint = rectangle[0]
        trpoint = (rectangle[0][0] + w, rectangle[0][1])
        dlpoint = (rectangle[1][0] - w, rectangle[1][1])
        drpoint = rectangle[1]
        return [tlpoint, trpoint, drpoint, dlpoint]