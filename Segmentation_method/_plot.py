import matplotlib.pyplot as plt
import numpy as np

def get_trans_seq(xy,keep_first=False):
    if keep_first:
        first_sec = np.hstack([xy[0], xy[1]])
        return np.vstack((np.hstack((xy[:-1], xy[1:])),first_sec))
    return np.hstack((xy[:-1], xy[1:]))

def add_lines(points,color, ax):
    for pair in points:
        linex = np.linspace(pair[0], pair[2],num= 100)
        liney = np.linspace(pair[1], pair[3], num=100)
        try:
            ax.scatter(linex, liney,c=color,s=1)
        except:
            plt.scatter(linex, liney,c=color,s=1)

def plot(line_points, points=np.array([]), ax=None, show_plot=False):
    colors = ['black', 'red']
    for _set, color in zip(line_points, colors):
        if len(_set):
            add_lines(_set, color, ax)
    if len(points)>0:
        for point in points:
            try:  
                ax.scatter(point[0], point[1], c='b', s=8)    
            except:
                plt.scatter(point[0], point[1], c='b', s=8)    
    if show_plot:
        plt.show()

def plots(line_points, points,titles,shape):
    fig, axs =plt.subplots(*shape)
    for ax_lines, ax_points,ax,title in zip(line_points, points, axs.flatten(), titles):
        plot(ax_lines, points=ax_points, ax=ax)
        ax.set_title(title)
    fig.tight_layout()
    plt.show()
