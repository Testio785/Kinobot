import matplotlib.pyplot as plt

# Функция для построения линии
def draw_line(x1, y1, x2, y2):
    plt.plot([x1, x2], [y1, y2])
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Line Plot')
    plt.grid(True)
    plt.show()

# Вызов функции с конкретными координатами
draw_line(150, 365, 156, 555)
