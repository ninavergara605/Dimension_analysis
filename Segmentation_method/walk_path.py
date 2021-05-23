import numpy as np
from find_intersection import find_circle_intersection
from find_intersection import euc_distance
from find_intersection import find_point_on_line
from _plot import get_trans_seq
from _plot import plot


def walk_path(subj_points,r,start_node=()):
    intersections = []
    subj_trans = get_trans_seq(subj_points, keep_first=True)
    i = 1
    if len(start_node)<1:
        current_node = subj_points[0]
    else:
        current_node = start_node
    while i <= len(subj_points)-1:
        while (dist:=euc_distance(*current_node, *subj_points[i])) >r:
            current_node = find_point_on_line(*current_node, *subj_points[i], r)
            intersections.append(current_node)
        
        if i+1 <= len(subj_points)-1:
            best_intersect = find_circle_intersection(current_node,subj_points[i], subj_points[i+1],r)
            if best_intersect.size>1:
                intersections.append(best_intersect)
                current_node = best_intersect
        i +=1
    path_tail = euc_distance(*current_node, *subj_points[-1])
    return intersections, path_tail