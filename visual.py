import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Style Settings
sns.set_style("whitegrid")
sns.set_palette("Set2")

# -----------------------------
# Load Dataset
data = pd.read_csv("parental_leavee.csv", encoding='latin1')

# Replacing N/A with NaN for analysis
data.replace("N/A", pd.NA, inplace=True)

# Converting numeric columns
cols = ["Paid Maternity Leave", "Unpaid Maternity Leave",
        "Paid Paternity Leave", "Unpaid Paternity Leave"]

for col in cols:
    data[col] = pd.to_numeric(data[col], errors='coerce')


# Filter Industries
industries_to_keep = ['Accounting', 'Business', 'Consulting', 'Educational', 'Advertising']
data = data[data['Industry'].isin(industries_to_keep)]


# Basic Information
print("\nFirst 5 Rows:\n")
print(data.head())
print("\nDataset Info:\n")
print(data.info())


# Visualization 1
# Average Paid Maternity Leave

avg_leave = data.groupby("Industry")["Paid Maternity Leave"].mean().sort_values()
plt.figure(figsize=(10,6))
avg_leave.plot(kind="barh", color="skyblue")
plt.title("Average Paid Maternity Leave by Industry", fontsize=14)
plt.xlabel("Weeks of Leave")
plt.ylabel("Industry")
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()


# Visualization 2
# Distribution of Maternity Leave

plt.figure(figsize=(8,5))
sns.histplot(data["Paid Maternity Leave"], bins=15, kde=True)
plt.title("Distribution of Paid Maternity Leave", fontsize=14)
plt.xlabel("Weeks")
plt.ylabel("Number of Companies")
plt.tight_layout()
plt.savefig("histogram.png")
plt.show()


# Visualization 3
# Maternity vs Paternity Leave
plt.figure(figsize=(8,5))
sns.scatterplot(
    x="Paid Maternity Leave",
    y="Paid Paternity Leave",
    hue="Industry",
    data=data,
    s=100
)
plt.title("Paid Maternity Leave vs Paid Paternity Leave", fontsize=14)
plt.xlabel("Paid Maternity Leave (Weeks)")
plt.ylabel("Paid Paternity Leave (Weeks)")
plt.tight_layout()
plt.savefig("scatter_plot.png")
plt.show()


# Visualization 4
# Industry Count
plt.figure(figsize=(8,5))
ax = sns.countplot(
    y="Industry",
    data=data,
    order=data["Industry"].value_counts().index
)
plt.title("Number of Companies by Industry", fontsize=14)
plt.xlabel("Number of Companies")
plt.ylabel("Industry")
# Add numbers on bars
for container in ax.containers:
    ax.bar_label(container)
plt.tight_layout()
plt.savefig("countplot.png")
plt.show()


# Visualization 5
# Correlation Heatmap
plt.figure(figsize=(8,6))
corr = data.corr(numeric_only=True)
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=0.5
)
plt.title("Correlation Heatmap for Parental Leave Data", fontsize=14)
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()

# Visualization 6
sns.pairplot(data[[
    "Paid Maternity Leave",
    "Unpaid Maternity Leave",
    "Paid Paternity Leave",
    "Unpaid Paternity Leave"
]])
plt.savefig("pairplot.png")
plt.show()


top_companies = data.sort_values(
    by="Paid Maternity Leave", ascending=False
).head(10)
print("\nTop Companies with Highest Paid Maternity Leave:\n")
print(top_companies[["Company", "Industry", "Paid Maternity Leave"]])