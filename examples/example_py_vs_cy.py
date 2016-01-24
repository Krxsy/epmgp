"""
comparing the python version with cython
"""
import time
import numpy as np
from information_gain import joint_min
import information_gain_cy as cy

# selecting mu and the covariance
x = [-2.1, -1,  4.3]
y = [3,  1.1,  0.12]
av_x = np.average(x)
av_y = np.average(y)
mu = np.array([av_x, av_y])
matrix = np.vstack((x,y))
cov = np.cov(matrix)


print('Starting python script')
start = time.time()
py_result = joint_min(mu,cov)
py_elapsed = (time.time() - start)

print('The minimum is %s' % py_result)
print('Python needed %f secs' % py_elapsed)


print('Starting cython script')
start = time.time()
cy_result = cy.joint_min(mu,cov)
cy_elapsed = (time.time() - start)

print('The minimum is %s ' % cy_result)
print('Cython needed %f secs' % cy_elapsed)
