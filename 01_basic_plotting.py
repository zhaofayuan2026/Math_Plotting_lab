import matplotlib.pyplot as plt
import numpy as np

#1，折线图
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.plot(x,y,label='y=2x')
plt.xlabel('x')
plt.ylabel('y')

x=np.linspace(1,5,100)
y=x**2
plt.plot(x,y,label='y=x**2')
plt.grid(True)
plt.legend()
plt.show()