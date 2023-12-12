import numpy as np

# Mantiqiy AND masalasi
def logical_and(x):
    return int((x[0] or x[1]) and x[2])

# Genetik algoritm funksiyalari
def initialize_population(population_size, gene_length):
    return np.random.uniform(-1, 1, size=(population_size, gene_length))

def step(z):
    if z>0:
        return 1
    return 0
def neuron(input,weight,bias ):
    net=input[0]*weight[0]+input[1]*weight[1]+input[2]*weight[2]+bias
    return step(net)
def evaluate_fitness(population, input_data, target_output):
    fitness_scores = []
    for individual in population:
          # Neironning kirish vazirliklari

        predictions = np.array([neuron(x,individual,0) for x in input_data])

        fitness = np.mean((predictions-target_output) ** 2)

        fitness_scores.append(fitness)
    return np.array(fitness_scores)

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    child = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
    return child

def mutate(individual, mutation_rate):
    mask = np.random.rand(len(individual)) < mutation_rate
    #print('mask', mask)
    #print(individual[mask])
    individual[mask] += np.random.uniform(-0.1, 0.1, size=np.sum(mask))
    return individual

# Mantiqiy AND masalasiga oid ma'lumotlar
input_data = np.array([[1, 0, 1], [0, 1, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]])
target_output = np.array([logical_and(x) for x in input_data])

# Genetik algoritmni boshlash
population_size = 100
gene_length = 3  # Neironning kirish vazirliklari (weights) va  bias
mutation_rate = 0.5
generations = 10

population = initialize_population(population_size, gene_length)
print(population)
for generation in range(generations):
    fitness_scores = evaluate_fitness(population, input_data, target_output)
    best_indices = np.argsort(fitness_scores)[:10]  # Tanlangan eng yaxshi 10 ta xramasoma
    best_individuals = population[best_indices]

    # Yangi populyatsiyani yaratish
    new_population = [best_individuals[np.random.randint(10)] for _ in range(population_size)]

    # Crossover
    for _ in range(population_size // 2):
        parent1 = best_individuals[np.random.randint(10)]
        parent2 = best_individuals[np.random.randint(10)]
        child1 = crossover(parent1, parent2)
        child2 = crossover(parent2, parent1)
        new_population.append(child1)
        new_population.append(child2)

    # Mutatsiya
    for i in range(population_size):
        new_population[i] = mutate(new_population[i], mutation_rate)

    population = np.array(new_population)

#print(evaluate_fitness(population, input_data, target_output))
# Eng yaxshi xramasoma
best_individual = population[np.argmin(evaluate_fitness(population, input_data, target_output))]
print("Eng yaxshi xramasomaning vazni:", evaluate_fitness(np.array([best_individual]), input_data, target_output)[0])
print("Eng yaxshi xramasoma:", best_individual)
