import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit

# data generation
n = 50
x= np.random.random(size=(n))*10
m= 5
c= 7
y= x**m-c*x**(m//2) -c*x

# fit the regression model
# calculate polynomial
z = np.polyfit(x, y, 3)#get x,y , degree
f = np.poly1d(z)#represent equation

# calculate new x's and y's
y_fit = f(x)

plt.plot(x, y_fit, '*r', label='regression', markersize=10)
plt.plot(x,y, 'o', label='data', markersize=5)
plt.title("nonlinear regression ")
plt.ylabel("dependent")
plt.xlabel("independent")
plt.legend()
plt.show()


####################################

#nonlinear regression 


""""
x= np.arange(-5.0,5.0,0.1)
y=2*x+3
y_noise=2*np.random.normal(size=x.size)
y_data=y+y_noise

plt.plot(x,y_data,"bo")
plt.plot(x,y,"r")
plt.title("linear regression ")
plt.ylable("dependent")
plt.xlable("independent")
plt.show()
"""

