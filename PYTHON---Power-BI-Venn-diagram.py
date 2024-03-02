import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import pandas as pd

# Assuming you have loaded your data into a Pandas DataFrame named df
# Replace df with your actual DataFrame name

# Example data
data1 = df['Column1'].tolist()
data2 = df['Column2'].tolist()

# Convert data to sets
set1 = set(data1)
set2 = set(data2)

# Calculate intersection and unique elements
venn_data = {
    '10': len(set1 - set2),
    '01': len(set2 - set1),
    '11': len(set1 & set2)
}

# Create Venn diagram
plt.figure(figsize=(8, 6))
venn = venn2(subsets=venn_data, set_labels=('Set 1', 'Set 2'))

# Add title
plt.title('Venn Diagram')

# Display the diagram
plt.show()
