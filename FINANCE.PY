import pandas as pd # for data processing
import matplotlib.pyplot as plt # for data visualization

# Correct the file path and make sure the file exists at this location
data = pd.read_csv(r'c:\Users\vjsai\3D Objects\Financial Budget.csv')

# Assuming 'Department /Ministry' is the column you want to analyze
sizes = data['Department /Ministry'].value_counts()
labels = sizes.index  # Get the unique labels from the index of the value_counts series

explode = (0.2,) + (0,) * (len(labels) - 1)  # Explode the first slice


# Create a pie chart
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels = labels, autopct='',
        shadow=True, startangle=90)

# Ensure that pie chart is drawn as a circle
ax1.axis()

# Add a title to the pie chart
plt.title('Pie Chart')

# Display the pie chart
plt.show()