# ================================= Error Bars ===================================== #
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(9, 5), dpi=120)
epochs = [1, 2, 3, 4, 5]
loss = [0.82, 0.60, 0.45, 0.32, 0.25]
loss_error = [0.05, 0.04, 0.03, 0.02, 0.02]

ax.errorbar(
    epochs,
    loss,
    yerr=loss_error,
    fmt='o-',
    capsize=5,
    color='crimson'
)

ax.set_title('Training Loss')
ax.set_xlabel('Epoch')
ax.set_ylabel('Loss')
ax.grid()
plt.show()

