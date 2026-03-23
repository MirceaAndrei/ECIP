import random
import matplotlib.pyplot as plt

states = ['a', 'b', 'c']
weights = {'a': 1.5, 'b': 2, 'c': 3.3}
transitions = {
    'a': {'b': 0.4, 'c': 0.6},
    'b': {'a': 0.5, 'b': 0.5},
    'c': {'a': 0.2, 'c': 0.6, 'b': 0.2}
}

current_state = 'a'
S = [current_state]

for _ in range(14):
    options = list(transitions[current_state].keys())
    probs = list(transitions[current_state].values())
    current_state = random.choices(options, weights=probs)[0]
    S.append(current_state)

r_values = [weights[s] for s in S]
x = 0.5
population_history = [x]

for r in r_values:
    x = r * x * (1 - x)
    population_history.append(x)

print("Sequence S:", S)
print("Growth Factors (r):", r_values)
print("Population at step 15:", population_history[-1])

plt.figure(figsize=(10, 5))
plt.step(range(len(S)), S, where='post', color='orange', label='State (Markov)')
plt.ylabel('State')
plt.twinx()
plt.plot(population_history, color='blue', marker='o', label='Population')
plt.ylabel('Population Size')
plt.title('Markov States vs. Logistic Population Growth')
plt.show()  