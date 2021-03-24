import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

np.random.seed(seed=1)
x_min = 4
x_max = 30
x_n = 16
X = 5 + 25*np.random.rand(x_n)
prm_c = [170, 108, 0.2]
T = prm_c[0] - prm_c[1]*np.exp(-prm_c[2]*X) + 4*np.random.randn(x_n)
np.savez('ch5_data.npz', X=X, x_min=x_min, x_max=x_max, x_n=x_n, T=T)

print(np.round(X,2))
print(np.round(T,2))

plt.figure(figsize=(4,4))
plt.plot(X, T, 'ko')
plt.grid(True)
plt.xlabel('Age')
plt.ylabel('Height')
plt.show()
