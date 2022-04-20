import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.DataFrame(np.random.randn(20, 10))
fig, _ = plt.subplots()
print(type(fig))