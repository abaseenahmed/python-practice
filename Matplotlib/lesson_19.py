# =========================== Different Color Maps in Matplotlib ================================ #
import numpy as np
import matplotlib.pyplot as plt

data = np.linspace(0, 1, 100).reshape(1, -1)

fig, ax = plt.subplots(2, 2, figsize=(10, 5), dpi=120)

ax[0,0].imshow(data, cmap="viridis", aspect="auto")
ax[0,0].set_title("Viridis Colormap")
ax[0,0].axis("off")

ax[0,1].imshow(data, cmap="plasma", aspect="auto")
ax[0,1].set_title("Plasma Colormap")
ax[0,1].axis("off")

ax[1,0].imshow(data, cmap="inferno", aspect="auto")
ax[1,0].set_title("Inferno Colormap")
ax[1,0].axis("off")

ax[1,1].imshow(data, cmap="gray", aspect="auto")
ax[1,1].set_title("Gray Colormap")
ax[1,1].axis("off")

plt.show()