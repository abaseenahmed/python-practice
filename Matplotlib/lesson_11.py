# ================================== Histogram in Matplotlib ==========================#
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6), dpi=120)

heights = [
    150, 152, 155, 157, 160,
    162, 165, 166, 168, 170,
    171, 173, 175, 176, 178,
    180, 182, 185, 188, 190
]

plt.hist(
    heights,
    # bins=6,
    # bins=4,
    bins=10,
    color="lightgreen",
    edgecolor="black"
)

plt.title("Height Distribution")
plt.xlabel("Height (cm)")
plt.ylabel("Frequency")
plt.grid(axis="y")
plt.show()

# when bins = 10 or bins = 4 the graph was not looking so proffessional and most of the bars had same height. therefor it is better to use the intermediatory numbr of bins.
