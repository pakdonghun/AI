X_test = X[:int(X_n/4+1)]
T_test = T[:int(X_n/4+1)]
X_train = X[int(X_n/4+1):]
T_train = T[int(X_n/4+1):]

plt.figure(figsize=(10,2.5))
plt.subplots_adjust(wspace=0.3)
M = [2, 4, 7, 9]
for i in range(len(M)):
    plt.subplot(1, len(M), i+1)
    W = fit_gauss_func(X_train, T_train, M[i])
    show_gauss_func(W)
    plt.plot(X_train, T_train, 'ko', label='training')
    plt.plot(X_test, T_test, 'b^', label='test')
    plt.legend(loc='lower right', fontsize=10, numpoints=1)
    plt.xlim(X_min, X_max)
    plt.ylim(130, 180)
    plt.grid(True)
    mse=mse_gauss_func(X_test, T_test, W)
    plt.title("M={0:d}, SD={1:.1f}".format(M[i], np.sqrt(mse)))
    
plt.show()
