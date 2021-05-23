
import numpy as np

def get_trans_seq_circle(xy):
    first_last = np.hstack([xy[0], xy[-1]])
    segs = np.vstack((np.hstack((xy[:-1], xy[1:])), first_last))
    return segs

def generate_circle(centerx,centery,r, n = 1001):
    coords = np.zeros((n,2))
    t = np.linspace(0, 2*np.pi, n, endpoint=False)
    coords[:,0] = r * np.cos(t)  + centerx
    coords[:,1] = r * np.sin(t) + centery
    transitions = get_trans_seq_circle(coords)
    return transitions