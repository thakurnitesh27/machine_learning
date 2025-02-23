



# def my_first_method():
#     k=1
#     for i in range(1,10):
#         k*=i
#     print(k)
#
# my_first_method()


import numpy as np
import matplotlib.pyplot as plt

# Data: Years and World Population (in billions)
years = np.array([1800, 1900, 1950, 2000, 2023])
population = np.array([1.0, 1.6, 2.5, 6.1, 8.0])

# Create the figure and axes
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Linear Scale Plot
axs[0].plot(years, population, marker='o', linestyle='-', color='b')
axs[0].set_title("World Population (Linear Scale)")
axs[0].set_xlabel("Year")
axs[0].set_ylabel("Population (Billions)")

# Logarithmic Scale Plot
axs[1].plot(years, population, marker='o', linestyle='-', color='r')
axs[1].set_yscale('log')  # Logarithmic scale for Y-axis
axs[1].set_title("World Population (Logarithmic Scale)")
axs[1].set_xlabel("Year")
axs[1].set_ylabel("Population (Billions)")

# Show the plots
plt.tight_layout()
plt.show()
