import matplotlib.pyplot as plt

months = [x[0] for x in data]
values = [x[1] for x in data]

plt.bar(months, values)
plt.xlabel("Month") 
plt.ylabel("Number") 
plt.show()