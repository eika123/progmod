# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 20:43:39 2017

@author: 1008kjei
"""

# forlengs derivasjonsskjema
def forward_difference(f, x0, h):
    return (f(x0 + h) - f(x0))/h


# baklengs derivasjonsskjema
def backward_difference(f, x1, h):
    return (f(x1) - f(x1 - h))/h
    

## midtpunktsskjema
def central_difference(f, x0, h):
    return (f(x0 + h) - f(x0 - h))/(2*h)


## thetaskjema. Legg merke til hvordan variabelen
## theta redifineres til navnet o slik at det er 
## samsvar mellom kode og matematikk
def theta_difference(f, x0, h, theta):
    o = theta
    df = f(x0 + o*h) - f(x0 - (1 - o)*h)
    dh = o*h + (1 - o)*h
    return df/(o*h + (1 - o)*h)
    
    
if __name__ == '__main__':
    
    thetas = {0: backward_difference, 1: forward_difference, 0.5: central_difference}
    
    def f(x): 
        return x**2
    
    h = 1E-5
    x0 = 5.0
    
    for theta in thetas:
        
        scheme = thetas[theta]
        diff = scheme(f, x0, h)
        thetadiff = theta_difference(f, x0, h, theta)
        
        print(diff, "thetadiff: ", thetadiff)
        
        
        """
        scheme(f, x0, h)
        theta_difference(f, x, h, theta)
        """

        
        
        
    
    