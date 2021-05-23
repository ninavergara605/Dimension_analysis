import numpy as np
from find_intersection import euc_distance
from _plot import get_trans_seq
from walk_path import walk_path
import pandas as pd
from _plot import plot
from _plot import plots
import matplotlib.pyplot as plt

def seg_analysis(xy, start_node, min_step,max_step):
    lengths = np.linspace(min_step,max_step,num=10)
    #lengths = np.linspace(0.3,1,num=20)
    distances = np.zeros((len(lengths), 2)) 
    xy_trans = get_trans_seq(xy) 
    all_inter = []
    
    titles = ['step length: {}'.format(np.round(r, 3)) for r in lengths]
    for i,r in enumerate(lengths):
        intersects, tail = walk_path(xy, r, start_node=start_node)
        distances[i,0] = np.log(r)
        
        distances[i,1] = len(intersects)*r+tail
        all_inter.append([xy[0],*intersects])
        #plot([xy_trans,[]], points=intersects, show_plot=True)

    inter_trans = [get_trans_seq(inter) for inter in all_inter]
    trans = [xy_trans for _ in range(len(lengths))]
    #plots(list(zip(trans, inter_trans)), all_inter, titles, (5,2))
    return distances

def get_step_size(xy):
    xy_trans = get_trans_seq(xy, keep_first=True)
    adjacent_distances = euc_distance(xy_trans[:,0], xy_trans[:,1],xy_trans[:,2],xy_trans[:,3])
    average_dist = np.average(adjacent_distances)
    #min_step = min(adjacent_distances)/2
    min_step = average_dist/3
    max_step = min_step*2#min_step+min_step/2
    return min_step, max_step

def pick_rand_dim(xy):
    xy_trans = get_trans_seq(xy, keep_first=True)
    lines = np.array([[np.linspace(x0,x1, num=20), np.linspace(y0,y1,num=20)] for x0,y0,x1,y1 in xy_trans])
    rand_lines = np.random.randint(0, len(lines) -1, size=50)
    rand_points = [np.random.randint(0,len(lines[i]) - 1) for i in rand_lines]
    return zip(rand_lines, rand_points),lines


def use_rand_start_nodes(xy,n):
    min_step, max_step =get_step_size(xy)
    rand_dim, rand_points = pick_rand_dim(xy)
    for i,j in rand_dim:
        start_node = rand_points[i,0][j], rand_points[i,1][j]
        forward = xy[i:] #wrong?
        distance_forward = seg_analysis(forward, start_node,min_step,max_step)
        distance_backwards = seg_analysis(np.flip(xy[:i], axis=0),start_node,min_step,max_step)
        return distance_forward, distance_backwards

if __name__ == "__main__":
    r = 3
    import cProfile
    np.seterr(divide='warn', invalid='warn')
    with cProfile.Profile() as pr:
    # ... do something ...


        #subj_points = pd.read_excel('/Users/ninavergara/Desktop/fractal dim/sample_fixations.xlsx',dtype = 'float64', usecols=['x','y'],nrows = 10).values
        subj_points = pd.read_csv('koch_curve.csv', dtype = 'float64', nrows=50, skiprows=0, delim_whitespace=True).values
        #subj_trans = get_trans_seq(np.round(subj_points, 8))
        '''
        subj_points = np.array([(-5,-10)
                    ,(5,10)
                    ,(3,2)
                    ,(8,9)])
        '''
        points_reversed = np.flip(subj_points,axis=0)
        
        subj_trans = np.array([[-5,-10,5,10]
                        ,[5,10,3,2]
                        ,[3,2,8,9]])
        
        min_step, max_step =get_step_size(subj_points)
        
        dist_forward = seg_analysis(subj_points,(), min_step, max_step)
        dist_backwards = seg_analysis(points_reversed,(),min_step,max_step)
        average = np.log(dist_forward[:,1] + dist_backwards[:,1] / 2)
        paired_avg = list(zip(dist_forward[:,0], average))
        #slope = paired_avg[-2][1] - paired_avg[0][1]/ paired_avg[-2][0] - paired_avg[0][1]
        #print(paired_avg)
        plt.scatter(dist_forward[:,0], average)
      
        trans = get_trans_seq(np.array(list(zip(dist_forward[:,0], average))), keep_first=True)
        
        slopes = (trans[:,3] - trans[:,1])/ (trans[:,2] - trans[:,0])
        print(slopes)
        #print(slopes, slopes + 1, slopes-1)
        #plt.scatter(list(range(len(slopes))), 1-slopes)

        #plt.scatter(dist_forward[:,0], np.log(dist_forward[:,1]), c='blue')
        #plt.scatter(dist_backwards[:,0], np.log(dist_backwards[:,1]), c='red', alpha=0.5)
  

        
        plt.show()
        
        
        #plt.show()
    #pr.print_stats()