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

#2.散点图
x=[1,2,3,4,5]
y=[2,4,6,8,10]
plt.scatter(x,y,color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()

#多条线对比
x=[1,2,3,4,5]
y1=[2,4,6,8,10]
y2=[1,3,5,7,9]
plt.plot(x,y1,color='blue',label='y1')
plt.plot(x,y2,color='green',label='y2')
plt.xlabel('x')
plt.ylabel('y')
plt.title('y1 vs y2')
plt.grid(True)
plt.show()
