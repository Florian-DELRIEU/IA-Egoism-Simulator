import matplotlib.pyplot as plt
from window import generate_window, plot_item
from classes import Character2D

generate_window()

C1 = Character2D(0,0,1,0)
plt.pause(1)
plot_item(C1)
plt.show()

for i in range(10):
    plt.pause(1)
    C1.move(1)
