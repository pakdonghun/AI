import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

np.random.seed(seed=1)
X_min = 4
X_max = 30
X_n = 16
X = 5 + 25*np.random.rand(X_n)
prm_c = [170, 108, 0.2]
T = prm_c[0] - prm_c[1]*np.exp(-prm_c[2]*X) + 4*np.random.randn(X_n)
np.savez('ch5_data.npz', X=X, X_min=X_min, X_max=X_max, X_n=X_n, T=T)

def gauss(x, mu, s):
    return np.exp(-(x-mu)**2/(2*s**2))

M=4
plt.figure(figsize=(8,8))
mu = np.linspace(5,30,M)
s=mu[1] - mu[0]
xb = np.linspace(X_min,X_max,100)
for j in range(M):
    y = gauss(xb, mu[j], s)
    plt.plot(xb, y, linewidth=3)
    
plt.grid(True)
plt.xlim(X_min, X_max)
plt.ylim(0, 1.2)
plt.show()
