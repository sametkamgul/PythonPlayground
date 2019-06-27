from random import choices
from tqdm import tqdm # use it for observing the progress through to console!

# variable defs
population = [1, 2, 3, 4, 5, 6]
weights = [0.4, 0.2, 0.2, 0.1, 0.05, 0.05]
results = [0, 0, 0, 0, 0, 0]
result = 0
sample_amount = 100000

for x in tqdm(range(sample_amount)):
	result = choices(population, weights)[0]
	results[result - 1] = int(results[int(result) - 1]) + 1 # increase the result

print()
print('[results]')
for r in results:
	print('item:', results.index(r)+1, ',', 'result:', r,  ',', 'probability:', (weights[results.index(r)])*100, '%')

# or use it for printing to the console
print('[results]')
for y in range(len(population)):
	print('item', population[y], ',', 'result:', results[y], ',', 'probability:' ,weights[y]*100, '%')