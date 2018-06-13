# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:43:39 2017

@author: 1008kjei
"""

# forlengs derivasjonsskjema
def forward_differentiation(f, x0, h):
    return (f(x0 + h) - f(x0))/h


# baklengs derivasjonsskjema
def backward_differentiation(f, x1, h):
    return (f(x1) - f(x1 - h))/h
    

## midtpunktsskjema
def central_difference(f, x0, h):
    return (f(x0 + h) - f(x0 - h))/(2*h)