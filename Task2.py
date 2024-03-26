# Завдання 2. Обчислення визначеного інтеграла.

# Обчисліть значення інтеграла функції за допомогою методу Монте-Карло, інакше кажучи, 
# знайдіть площу під цим графіком (сіра зона).
# Перевірте правильність розрахунків, щоб підтвердити точність методу Монте-Карло, 
# шляхом порівняння отриманого результату та аналітичних розрахунків або результату виконання функції quad. 
# Зробіть висновки.

import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np
import random

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

def monte_carlo(f, a, b, experiments):
    Sa = 0 #середнє значення площі
    a = b - a
    b = f(b)
    for i in range(experiments):
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        inside_points = [point for point in points if is_inside(f, point[0], point[1])]
        N = len(points)
        M = len(inside_points)

        Sa += (M / N) * (a * b)  # Площа за методом Монте-Карло
    Sm = Sa / experiments
    return Sm

def is_inside(f, x, y):
    return y <= f(x)

def main():
    a = 0
    b = 2

    result, error = spi.quad(f, a, b)
    result_m = monte_carlo(f, a, b, 100)
    print("Інтеграл quad: ", result)
    print("Інтеграл Monte-Carlo: ", result_m)

    

    # Створення діапазону значень для x
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    # Створення графіка
    fig, ax = plt.subplots()

    # Малювання функції
    ax.plot(x, y, 'r', linewidth=2)

    # Заповнення області під кривою
    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    # Налаштування графіка
    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    # Додавання меж інтегрування та назви графіка
    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')
    ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()