#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 12:10:35 2017
Cookie problem.
@author: tsalo
"""
from __future__ import division
import numpy as np

# V = 0; C = 1
cookie_types = {0: 'vanilla', 1: 'chocolate'}
data = np.zeros((10000))
data[8928:] = 1
data = data.astype(int)
#data = [0, 1, 1, 1, 0, 1, 0, 0, 0, 0, ]

pCOOKIEgB = np.array([[0.75, 0.5],
                      [0.25, 0.5]])

pB = [0.5, 0.5]  # prior

for cookie_type in data:
    #print('You drew a {0} cookie!'.format(cookie_types[cookie_type]))
    pDgB = pCOOKIEgB[cookie_type, :]  # likelihood
    unnormalized_posterior = pDgB * pB
    pD = np.sum(unnormalized_posterior)  # evidence
    pBgD = unnormalized_posterior / pD  # posterior
    pB = pBgD[:]  # make your posterior into the prior for the next datapoint

print('Probability of bag given data: ')
print('\tBag 1: {0:.02f}'.format(pBgD[0]))
print('\tBag 2: {0:.02f}'.format(pBgD[1]))