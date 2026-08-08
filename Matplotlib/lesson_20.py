import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(100, 100)

fig, ax = plt.subplots(figsize=(7, 6), dpi=120)

image = ax.imshow(data, cmap="coolwarm")

fig.colorbar(image, ax=ax)

ax.set_title("Random Intensity Map")
ax.set_label("Intensity")
ax.axis("off")
plt.show()