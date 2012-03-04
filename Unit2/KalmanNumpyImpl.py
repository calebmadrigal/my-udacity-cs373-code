#!/usr/bin/env python
#
# DESCRIPTION
#    Implementation of the Kalman filter algorithm for a 2 dimensional space where the
#    state is made up of (x position, y position, x velocity, y velocity).
#
#    This is a slight modification to the code used in class which uses the NumPy library
#    instead of the matrix class used in class.
#
# NOTES
#    Measurement update first, then motion (predict)
#    P init to for x & y is 0, but for velocity is 1000
#    H only observes x & y
#    R is 2x2 which 0.1 as main diagonal (measurement uncertainty matrix)
#    I is identity matrix

from math import *
from numpy import *

def filter(x, P):
    for n in range(len(measurements)):
        
        # prediction
        x = (F * x) + u
        P = F * P * F.getT()
        
        # measurement update
        Z = matrix([measurements[n]])
        y = Z.getT() - (H * x)
        S = H * P * H.getT() + R
        K = P * H.getT() * S.getI()
        x = x + (K * y)
        P = (I - (K * H)) * P
    
    print 'x= '
    print x
    print 'P= '
    print P

print "### 4-dimensional example ###"

measurements = [[5., 10.], [6., 8.], [7., 6.], [8., 4.], [9., 2.], [10., 0.]]
initial_xy = [4., 12.]

# measurements = [[1., 4.], [6., 0.], [11., -4.], [16., -8.]]
# initial_xy = [-4., 8.]

# measurements = [[1., 17.], [1., 15.], [1., 13.], [1., 11.]]
# initial_xy = [1., 19.]

dt = 0.1

x = matrix([[initial_xy[0]], [initial_xy[1]], [0.], [0.]]) # initial state (location and velocity)
u = matrix([[0.], [0.], [0.], [0.]]) # external motion

P =  matrix([ [0,0,0,0], [0,0,0,0], [0,0,1000.,0], [0,0,0,1000.] ])            # initial uncertainty
F =  matrix([ [1., 0, dt, 0], [0, 1., 0, dt], [0, 0, 1., 0], [0, 0, 0, 1.]  ]) # next state function
H =  matrix([ [1, 0, 0, 0], [0, 1, 0, 0] ])                                    # measurement function
R =  matrix([ [dt, 0], [0, dt] ])                                              # measurement uncertainty
I =  matrix([ [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1] ])        # identity matrix

filter(x, P)

