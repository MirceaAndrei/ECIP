# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=30)
plt.savefig('histogram.png')