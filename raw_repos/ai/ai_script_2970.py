import matplotlib.pyplot as plt

# Make a data frame from the given data
df = pd.DataFrame({'year': year, 'number_of_sales': number_of_sales})

# Plot a line chart
plt.plot(df['year'], df['number_of_sales'], linewidth=3)
plt.title("Car Sales in the UK from 2008 to 2019")
plt.xlabel("Year")
plt.ylabel("Number of sales")

# Show the plot
plt.show()