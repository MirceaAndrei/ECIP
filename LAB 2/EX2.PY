import matplotlib.pyplot as plt

r = 3.9  
x = 0.1  
history = [x]

for _ in range(100):
    x = r * x * (1 - x)
    history.append(x)

plt.plot(history, marker='o', markersize=3)
plt.title(f"Chaotic Population Growth (r = {r})")
plt.xlabel("Generation")
plt.ylabel("Population Ratio")
plt.grid(True)
plt.savefig('chaotic_growth.png')