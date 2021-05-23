import numpy as np
from circle_segments import generate_circle
from _plot import plot
from _plot import get_trans_seq

def find_point_on_line(x0,y0,x1,y1,d):
    vx,vy = x1-x0, y1-y0
    u_den = np.sqrt(vx**2 + vy**2)
    ux,uy = vx/u_den, vy/u_den
    x = x0 + d*ux
    y = y0 + d*uy
    return [x,y]

def calc_line_equation(p1, p2):
    if p1.ndim == 1:
        m = (p2[1] - p1[1])/ (p2[0] - p1[0])
        b = -(m * p1[0]) + p1[1]
    else:
        m = (p2[:,1] - p1[:,1])/ (p2[:,0] - p1[:,0])
        b = -(m * p1[:,0]) + p1[:,1]
    return m,b

def euc_distance(x0,y0,x1,y1):
    if isinstance(x0,np.float):
        return np.sqrt((x1-x0)**2 + (y1-y0)**2)
    return np.sqrt(np.add(np.subtract(x1,x0)**2 , np.subtract(y1,y0)**2))

def calc_intersect(p0,p1,q0,q1):
    res = np.zeros((len(p0), 2))
    m1, b1 = calc_line_equation(np.array(p0), np.array(p1))
    m2,b2 = calc_line_equation(np.array(q0), np.array(q1))
    m = m1-m2
    b= b2 - b1
    res[:,0] = b/m
    res[:,1] = (m1*res[:,0]) + b1
    return res

def get_orientation(p0, p1, q0,q1):
    orientations = np.zeros((len(p0), 2))
    orientations[:,0] = (p1[:,0] - q0[0]) * (p0[:,1] - q0[1]) - (p0[:,0] - q0[0]) * (p1[:,1] - q0[1])
    orientations[:,1] =(p1[:,0] - q1[0]) * (p0[:,1] - q1[1]) - (p0[:,0] - q1[0]) * (p1[:,1] - q1[1])
    return orientations

def calc_squared_error(xy1, xy2, end_point):
    error_1 = np.sqrt(np.square(xy1[:,0] - end_point[0]) + np.square(xy1[:,1] - end_point[1]))
    error_2 = np.sqrt(np.square(xy2[:,0] - end_point[0]) + np.square(xy2[:,1] - end_point[1]))
    error_sum = error_1 + error_2
    return error_sum

def get_intersect_distances(start_node, end_node, intersections):
    distances = np.zeros((len(intersections), 3))
    distances[:,0] = euc_distance(*start_node, intersections[:,0], intersections[:,1])
    distances[:,1]= euc_distance(*end_node, intersections[:,0], intersections[:,1])
    line_distance = euc_distance(*start_node, *end_node)
    distances[:,2] = np.repeat(line_distance, len(intersections))
    return distances

def find_points_in_boundary(x0,y0,x1,y1, intersx, intersy):
    filtered = []
    for b1,b2,arr in [[x0,x1,intersx], [y0,y1,intersy]]:
        if b1 > b2:
            _filter = np.where((arr < b1) & (arr > b2))
        else:
            _filter = np.where((arr > b1) & (arr < b2))
        filtered.append(_filter)
    return np.intersect1d(*filtered)
        
def find_circle_intersection(current_node,next_start,next_end, r):
    trans_seq = get_trans_seq([current_node, next_start, next_end])
    circle_segs = generate_circle(*current_node, r)
    '''
    orient = get_orientation(_circle_segs[:,:2], _circle_segs[:,2:], start_node, end_node)
    orient_filter = np.where(((orient[:,0] < 0) & (orient[:,1] > 0)) | ((orient[:,0] < 0) & (orient[:,1] > 0)))
    circle_segs = _circle_segs[orient_filter]
    '''
    intersections = calc_intersect(circle_segs[:,:2], circle_segs[:,2:], next_start, next_end)
    distances = get_intersect_distances(next_start, next_end, intersections)
    on_line_filter = np.where((distances[:,0] + distances[:,1] == distances[:,2]))
    
    '''
    in_boundary_filter = find_points_in_boundary(*current_node, *next_start, intersections[:,0], intersections[:,1])
    print(in_boundary_filter)
    idx = np.intersect1d(on_line_filter,in_boundary_filter) 
    '''
    idx = on_line_filter
    filt_inters, filt_dist = intersections[idx], distances[idx],
    dist_error = np.sqrt(np.square(filt_dist[:,0] - r)).flatten()
    #plot([trans_seq,circle_segs], points=filt_inters, show_plot=True)
    
    if dist_error.size>0:
        best_point = np.where(dist_error == min(dist_error))
        res = np.average(filt_inters[best_point], axis=0)
       
        return res
    return np.array([])