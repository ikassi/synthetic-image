import numpy as np
def synthetic_sphere(light):
    # sphere radius
    r = 200
    # sphere grid 
    [x,y] = np.mgrid[-1.3*r*10:1.3*r*10,-1.3*r*10:1.3*r*10]
    # using finner grid to enchance resolution
    [x,y] = [0.1*x.astype(float),0.1*y.astype(float)]
    # albedo
    albedo = 0.5
    # illumination direction
    l = light
    # partial derivatives in x and y direction
    p = -x/np.sqrt(r*r-(x*x+y*y))
    q = -y/np.sqrt(r*r-(x*x+y*y))
    # calculate brightness
    E = albedo/np.sqrt(1+p*p + q*q) * (-l[0]*p - l[1]*q + l[2])
    # remove points not in the sphere
    E *= (r*r - (x*x + y*y)) >= 0
    # set negarive and nan brightness to 0
    E[E<0] = 0
    E[np.isnan(E)] = 0
    # normalize
    E /= E.max()
    return E