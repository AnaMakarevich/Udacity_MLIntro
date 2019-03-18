#!/usr/bin/python
import warnings
import matplotlib
import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

warnings.filterwarnings("ignore")
matplotlib.use('agg')


def pretty_picture(clf, x_test, y_test, figure_name='figures/clf_result.png', to_file=False):
    x_min = 0.0
    x_max = 1.0
    y_min = 0.0
    y_max = 1.0

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, m_max]x[y_min, y_max].
    h = .01  # step size in the mesh
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    z = z.reshape(xx.shape)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.pcolormesh(xx, yy, z, cmap=pl.cm.seismic)

    # Plot also the test points
    grade_sig = [x_test[ii][0] for ii in range(0, len(x_test)) if y_test[ii] == 0]
    bumpy_sig = [x_test[ii][1] for ii in range(0, len(x_test)) if y_test[ii] == 0]
    grade_bkg = [x_test[ii][0] for ii in range(0, len(x_test)) if y_test[ii] == 1]
    bumpy_bkg = [x_test[ii][1] for ii in range(0, len(x_test)) if y_test[ii] == 1]

    plt.scatter(grade_sig, bumpy_sig, color="b", label="fast")
    plt.scatter(grade_bkg, bumpy_bkg, color="r", label="slow")
    plt.legend()
    plt.xlabel("bumpiness")
    plt.ylabel("grade")
    plt.show()
    if to_file:
        plt.savefig(figure_name)
