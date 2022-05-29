import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,decomposition,manifold

def load_data():
    iris=datasets.load_iris()
    return iris.data,iris.target

def test_MDS(*data):
    X,Y=data
    for n in [4,3,2,1]:
        mds=manifold.MDS(n_components=n)
        mds.fit(X)
        print("stress(n_components=%d):%s"%(n,str(mds.stress_)))

def plot_MDS(*data):
    X,Y=data
    mds=manifold.MDS(n_components=2)
    X_r=mds.fit_transform(X)
 #   print(X_r)

    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    colors=((1,0,0),(0,1,0),(0,0,1),(0.5,0.5,0),(0,0.5,0.5),(0.5,0,0.5),(0.4,0.6,0),(0.6,0.4,0),(0,0.6,0.4),(0.5,0.3,0.2),)
    for label,color in zip(np.unique(Y),colors):
        position=Y==label
        ax.scatter(X_r[position,0],X_r[position,1],label="target=%d"%label,color=color)
    ax.set_xlabel("X[0]")
    ax.set_ylabel("Y[0]")
    ax.legend(loc="best")
    ax.set_title("MDS")
    plt.show()

X,Y=load_data()
test_MDS(X,Y)
plot_MDS(X,Y)