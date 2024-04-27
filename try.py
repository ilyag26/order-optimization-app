from scipy.optimize import minimize

def delta(z):
    a = 2 #коефіцієнти, які визначають вплив обсягу замовлення на вартість
    b = 3
    return a*z+b

# Задання початкових значень для параметрів
T = 12
K = 12
z = 12
C = lambda z, y: z * y
h = 12
I = 12

# Визначення функції, яку потрібно мінімізувати
def objective_function(x):
    print(x)
    return sum(x[1] * x[3] + C(12, 12) + x[5] * x[6] for _ in range(1, T + 1))

# Початкове наближення для значень параметрів
initial_guess = [12.0,12.0,12.0,12.0,12.0,12.0,12.0]

# Виклик функції minimize для знаходження мінімуму
result = minimize(objective_function, initial_guess, method='BFGS')

# Отримання оптимального значення
optimal_value = result.fun

print("Оптимальне значення функції:", optimal_value)
