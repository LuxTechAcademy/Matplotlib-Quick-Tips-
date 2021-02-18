# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import random

# plotting plot
fig=plt.figure(figsize=(5,8))

X=list(range(10))
Y=[x+(x*random.random()) for x in X]

plt.plot(X,Y)

plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show() 


"""" Changing the Plot Size """
fig=plt.figure(figsize=(8,3))

plt.plot(X,Y)

plt.title('Line Plot')
plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.show()