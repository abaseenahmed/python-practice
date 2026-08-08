#============================== Creating Random Image in Matplotlib ============================== #
import numpy as np
import matplotlib.pyplot as plt

image = np.random.rand(100, 100)
image2 = np.random.rand(100, 100)

fig, ax = plt.subplots(1, 2, figsize=(10, 5), dpi=120)

ax[0].imshow(image, cmap='gray')
ax[0].set_title('Random Grayscale Image')
ax[0].axis('off')

ax[1].imshow(image2, cmap='rainbow')
ax[1].set_title('Colourful Image')
ax[1].axis('off')

plt.show()