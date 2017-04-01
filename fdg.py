import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))

#Estimación de medias y Covarianzas
Mu1 = np.mean(X2[:50,:], axis=0)
Sigma1 = np.cov((X2[:50,:]).T)
Mu2 = np.mean(X2[51:,:], axis=0)
Sigma2 = np.cov((X2[51:,:]).T)
Z = np.zeros((100,100))

#Evaluando las fdp's en una malla de valores
for i in range(100):
    for j in range(100):
        tem = np.array([xx[1,i],yy[j,1]] - Mu1)[np.newaxis]
        p1 = (1/(2*pi*math.sqrt(np.linalg.det(Sigma1))))*math.exp(-0.5*tem*inv(np.matrix(Sigma1))*tem.T)
        tem = np.array([xx[1,i],yy[j,1]] - Mu2)[np.newaxis]
        p2 = (1/(2*pi*math.sqrt(np.linalg.det(Sigma2))))*math.exp(-0.5*tem*inv(np.matrix(Sigma2))*tem.T)
        
        if p1 >= p2:
            Z[i,j] = 1
        else:
            Z[i,j] = 0
plt.figure()
plt.pcolormesh(xx, yy, Z.T, cmap=cmap_light)
plt.scatter(X2[:,0], X2[:,1], c=y2)