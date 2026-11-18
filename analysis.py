
# ==============================
# Task 1: Histogram (Binning Trap)
# ==============================

import numpy as np
import matplotlib.pyplot as plt

# Generate two normal distributions
data1 = np.random.normal(30, 5, 250)
data2 = np.random.normal(70, 5, 250)

# Combine both arrays
data = np.concatenate((data1, data2))

# Create 1x3 subplots
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# Compare different bin sizes
axes[0].hist(data, bins=5)
axes[0].set_title("Bins = 5")

axes[1].hist(data, bins=30)
axes[1].set_title("Bins = 30")

axes[2].hist(data, bins=200)
axes[2].set_title("Bins = 200")

plt.tight_layout()
plt.show()


# ==============================
# Task 2: Scatter Plot
# ==============================

import numpy as np
import matplotlib.pyplot as plt

# Generate house data
np.random.seed(42)

Area = np.random.randint(80, 250, 150)
Price = Area * 3000 + np.random.randint(50000, 200000, 150)
Distance = np.random.randint(1, 30, 150)
Age = np.random.randint(1, 40, 150)

# Create scatter plot
plt.figure(figsize=(9, 6))

plt.scatter(
    Area,
    Price,
    s=Distance * 10,
    c=Age,
    cmap="viridis",
    alpha=0.7
)

# Add labels and colorbar
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("House Data Analysis")
plt.colorbar(label="House Age")

plt.show()


# ==============================
# Task 3: Function Comparison
# ==============================

import numpy as np
import matplotlib.pyplot as plt

# Generate x values
x = np.linspace(-2*np.pi, 2*np.pi, 1000)

# Calculate mathematical functions
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.arctan(x)

# Remove extreme tan values
y3[np.abs(y3) > 5] = np.nan

# Create 2x2 subplots
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot sin
axes[0, 0].plot(x, y1)
axes[0, 0].set_title("Sin(x)")

# Plot cos
axes[0, 1].plot(x, y2)
axes[0, 1].set_title("Cos(x)")

# Plot tan
axes[1, 0].plot(x, y3)
axes[1, 0].set_title("Tan(x)")
axes[1, 0].set_ylim(-5, 5)

# Plot arctan
axes[1, 1].plot(x, y4)
axes[1, 1].set_title("Arctan(x)")

plt.tight_layout()
plt.show()


# ==============================
# Task 4: Pie-to-Bar Rescue
# ==============================

import matplotlib.pyplot as plt

# Define companies and market shares
companies = ["A", "B", "C", "D", "E", "F", "G", "H"]
shares = [18, 17, 15, 14, 12, 10, 8, 6]

# Sort data in ascending order
sorted_data = sorted(zip(companies, shares), key=lambda x: x[1])

sorted_companies = [x[0] for x in sorted_data]
sorted_shares = [x[1] for x in sorted_data]

# Find the third ranked company
third_company = sorted(companies, key=lambda x: shares[companies.index(x)], reverse=True)[2]

# Create 1x2 subplots
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Draw pie chart
axes[0].pie(shares, labels=companies, autopct="%1.1f%%")
axes[0].set_title("Pie Chart")

# Draw horizontal bar chart
axes[1].barh(sorted_companies, sorted_shares)
axes[1].set_title("Market Share")
axes[1].set_xlabel("Market Share")

# Display third ranked company
plt.suptitle("3rd Ranked Company: " + third_company)

plt.tight_layout()
plt.show()


# ==============================
# Task 5: Correlation Heatmap
# ==============================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)

A = np.arange(1, 101)
B = A * 2 + np.random.normal(0, 5, 100)
C = -A + np.random.normal(0, 5, 100)
D = np.random.normal(50, 10, 100)

# Create DataFrame
df = pd.DataFrame({
    "A": A,
    "B": B,
    "C": C,
    "D": D
})

# Calculate correlation matrix
corr = df.corr()

# Draw heatmap
plt.figure(figsize=(7, 5))
plt.imshow(corr, cmap="coolwarm")
plt.colorbar()

# Add column names
plt.xticks(range(4), corr.columns)
plt.yticks(range(4), corr.columns)

# Display correlation values
for i in range(4):
    for j in range(4):
        plt.text(j, i, round(corr.iloc[i, j], 2),
                 ha="center", va="center")

plt.title("Correlation Heatmap")
plt.show()


# ==============================
# Task 6: Publication Export
# ==============================

import matplotlib.pyplot as plt

# Define categories and values
categories = ["A", "B", "C", "D", "E"]
values = [20, 45, 30, 60, 40]

# Create bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(categories, values)

# Find maximum value and its index
max_value = max(values)
max_index = values.index(max_value)

# Remove top and right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Highlight maximum value with an arrow
ax.annotate(
    "Maximum Value",
    xy=(max_index, max_value),
    xytext=(max_index + 0.5, max_value + 10),
    arrowprops=dict(arrowstyle="->")
)

# Add labels and title
ax.set_title("Maximum Value Analysis")
ax.set_xlabel("Categories")
ax.set_ylabel("Values")

# Save chart with high resolution
plt.savefig("chart.png", dpi=300, bbox_inches="tight")

plt.show()




