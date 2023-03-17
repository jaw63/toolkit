import matplotlib.pyplot as plt

# data to display on plots 
x = [3, 1, 3]
y = [3, 2, 1]
z = [1, 3, 1]
 
# Creating figure object
plt.figure()
 
# adding first subplot
plt.subplot(121)
plt.plot(x, y, color="pink", marker="*")
 
# adding second subplot
plt.subplot(122)
plt.plot(z, y, color="cyan", marker="+")

plt.show()
