import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
def bubble_sort(data):
    n = len(data)
    swapped = True
    while swapped:
        swapped = False
        for i in range(n-1):
            if data[i]>data[i+1]:
                data[i], data[i+1] = data[i+1], data[i] 
                swapped = True
                yield data
def generate_data(size):
    return [random.randint(1,100) for _ in range(size)]
def update_bars(data):
    bars = plt.bar(range(len(data)), data, color = "blue")
    return bars
def update_fig(data):
    for bar, val in zip(bars, data):
        bar.set_height(val)
def main():
    size = 30
    data = generate_data(size)
    fig, ax = plt.subplots()
    global bars  
    bars = update_bars(data)
    ax.set_xlim(0, len(data))
    ax.set_ylim(0, max(data) + 10)

    def animate(frame):
        update_fig(frame)

    ani = animation.FuncAnimation(fig, animate, frames=bubble_sort(data.copy()), repeat=False)
    plt.show()

if __name__ == "__main__":
    main()