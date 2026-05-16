# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(1000)
plt.hist(data, bins=20, range=(0, 1), edgecolor='black')
plt.savefig('uniform_histogram.png')