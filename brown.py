import numpy as np
import matplotlib.pyplot as plt

# Задаем параметры модели
mu = 0.1       # Средняя доходность (например, 10% годовых)
sigma = 0.2    # Волатильность (например, 20%)
S0 = 100       # Начальная цена акции
T = 1.0        # Время моделирования (1 год)
dt = 1/252     # Шаг времени (1 торговый день, 252 дня в году)
N = int(T / dt)  # Количество временных шагов

# Генерация броуновского движения
np.random.seed(42)  # Для воспроизводимости
W = np.random.normal(0, np.sqrt(dt), N)  # Приращения броуновского движения
W = np.cumsum(W)  # Кумулятивная сумма для моделирования пути W(t)

# Моделирование траектории цены акции с использованием GBM
t = np.linspace(0, T, N)  # Временная шкала
S = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)  # Модель GBM

# Построение графика траектории цены акции
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Simulated Stock Price')
plt.xlabel('Time (Years)')
plt.ylabel('Stock Price')
plt.title('Geometric Brownian Motion (GBM) Simulation of Stock Price')
plt.legend()
plt.grid(True)
plt.show()