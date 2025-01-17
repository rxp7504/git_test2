import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# Create a NumPy array
array = np.random.rand(20, 3)  # 10 rows, 3 columns of random numbers
print("NumPy Array:\n", array)

# View the array in SciView
# Right-click on 'array' in the console and select "View as Array" in PyCharm.

# Convert the array to a Pandas DataFrame
df = pd.DataFrame(array, columns=['A', 'B', 'C'])
print("\nPandas DataFrame:\n", df)
