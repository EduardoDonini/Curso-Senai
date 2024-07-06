import numpy as np 


r = np.linspace(1,6,10)
print(r)


aleatorio = np.random.randint(10)

aleatorio2 = np.arange(1,21)
aleatorio2a = np.arange(1,21)

print(aleatorio2)
print(aleatorio2a)

aleatorio3 = np.random.randint(1,200, (10,10,10))

mult = np.dot(aleatorio2,aleatorio2a)
mult2 = aleatorio2 * aleatorio2a
print(mult2)

# print(aleatorio)
# print(aleatorio2)
# print(aleatorio3)