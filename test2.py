from mpl_toolkits.mplot3d import Axes3D

def mse_line(x, t, w):
    y = w[0]*x + w[1]
    mse = np.mean((y-t)**2)
    return mse

xn = 100
w0_range = [-10, 10]
w1_range = [110, 170]
x0 = np.linspace(w0_range[0], w0_range[1], xn)
x1 = np.linspace(w1_range[0], w1_range[1], xn)
xx0, xx1 = np.meshgrid(x0,x1)
J = np.zeros((len(x0),len(x1)))

for i0 in range(xn):
    for i1 in range(xn):
        J[i1,i0] = mse_line(X, T, (x0[i0], x1[i1]))

plt.figure(figsize=(9.5,4))
plt.subplots_adjust(wspace=0.5)

ax = plt.subplot(1, 2, 1, projection='3d')
ax.plot_surface(xx0, xx1, J, rstride=10, cstride=10, alpha=0.3, color='blue', edgecolor='black')
ax.set_xticks([-20, 0, 20])
ax.set_yticks([120, 140, 160])
ax.view_init(60,-60)
ax.set_xlabel('w0')
ax.set_ylabel('w1')
ax.set_zlabel('MSE, J')

plt.subplot(1,2,2)
cont=plt.contour(xx0, xx1, J, 30, levels=[100, 1000, 10000, 100000])
cont.clabel(fmt='%1.0f', fontsize=8)
plt.xlabel('w0')
plt.ylabel('w1')
plt.grid(True)
plt.show()
