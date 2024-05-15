import matplotlib.pyplot as plt

def plot_item(item):
    plt.plot(item.x,item.y,item.color)

def generate_window():
    plt.figure("main window",figsize=(20,10))
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.show()
