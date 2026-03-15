import numpy as np
import matplotlib.pyplot as plt

# Ось времени
years = np.arange(0, 2101)

# Границы эпох
epochs = [0, 1500, 1800, 1945, 2000, 2025, 2100]

# Коэффициенты роста по эпохам
rates_power = [0.0001, 0.0002, 0.0006, 0.001, 0.0012, 0.001]
rates_money = [0.0001, 0.0003, 0.0008, 0.0015, 0.002, 0.0018]
rates_knowledge = [0.0001, 0.0005, 0.001, 0.002, 0.004, 0.003]

def generate_series(rates):
    values = []
    current = 1.0
    idx = 0
    for year in years:
        if idx < len(rates) - 1 and year >= epochs[idx + 1]:
            idx += 1
        current *= np.exp(rates[idx])
        values.append(current)
    return np.array(values)

print("rates_power =", rates_power)
print("len =", len(rates_power))

power = generate_series(rates_power)
money = generate_series(rates_money)
knowledge = generate_series(rates_knowledge)

plt.figure(figsize=(14, 7))
plt.plot(years, power, label='Сила')
plt.plot(years, money, label='Деньги')
plt.plot(years, knowledge, label='Знания')

# Логарифмический масштаб по Y
plt.yscale('log')

# Вертикальные линии эпох
for x in [1500, 1800, 1945, 2000, 2025]:
    plt.axvline(x, color='gray', linestyle='--', alpha=0.5)

plt.xlabel('Год')
plt.ylabel('Относительный уровень (логарифмическая шкала)')
plt.title('Рост силы, денег и знаний человечества (логарифмическая шкала, модельные данные)')
plt.legend()
plt.grid(axis='y', which='both')

plt.tight_layout()
plt.savefig('growth_power_money_knowledge_log.png', dpi=200)
plt.show()
power = generate_series(rates_power)
money = generate_series(rates_money)
knowledge = generate_series(rates_knowledge)

plt.figure(figsize=(12, 6))
plt.plot(years, power, label="Сила")
plt.plot(years, money, label="Деньги")
plt.plot(years, knowledge, label="Знания")

plt.xlabel("Годы")
plt.ylabel("Рост")
plt.title("Экспоненциальный рост ценностей по эпохам")
plt.legend()
plt.grid(True)
plt.show()
