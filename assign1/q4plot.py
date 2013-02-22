#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt


def f(M):
	return ((M*(M-1))/(4*(M+1))) - 2*np.log(M+2)
t = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t, f(t)) 


