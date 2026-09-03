import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuBuGn, s=25)

ax.set_title('Cubes Numbers', fontsize=25)
ax.set_xlabel('Value', fontsize=15)
ax.set_ylabel('Cubes', fontsize=15)

ax.tick_params(labelsize=12)

ax.axis([0, 5100, 0, 130_000_000_000])
ax.ticklabel_format(style='plain')

# plt.show()
plt.savefig('try_it_yourself_15_1-2.png', bbox_inches='tight')
