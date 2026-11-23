import matplotlib.pyplot as plt

x=[1,2,3,3,4,4,5]
y=[2,3,5,6,7,8,9]
plt.barh(x,y, color="green")
plt.xlabel("X-cordinate")
plt.ylabel("Y-coordinate")
plt.title("X vs Y")
plt.show()