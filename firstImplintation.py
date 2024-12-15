import random

# Define the problem constraints
EMPLOYEES = ["Emp1", "Emp2", "Emp3", "Emp4", "Emp5"]
HOURS = 24  # Total hours to cover in a day
MAX_HOURS_PER_EMPLOYEE = 8  # Maximum hours an employee can work in a day
MIN_HOURS_PER_EMPLOYEE = 4  # Minimum hours an employee should work in a day
POPULATION_SIZE = 100  # Number of schedules in a generation
GENERATIONS = 500  # Number of generations to evolve
MUTATION_RATE = 0.1  # Probability of mutation

# Generate initial population
def generate_schedule():
    schedule = {}
    for employee in EMPLOYEES:
        schedule[employee] = random.randint(MIN_HOURS_PER_EMPLOYEE, MAX_HOURS_PER_EMPLOYEE)
    return schedule

def generate_population():
    return [generate_schedule() for _ in range(POPULATION_SIZE)]

# Fitness function
def fitness(schedule):
    total_hours = sum(schedule.values())
    fairness = len(set(schedule.values()))  # Higher is better
    if total_hours < HOURS:
        return 0  # Penalize schedules that don't cover all hours
    return 1 / (1 + abs(total_hours - HOURS)) + fairness

# Selection function
def select_population(population):
    weighted_population = [(schedule, fitness(schedule)) for schedule in population]
    weighted_population.sort(key=lambda x: x[1], reverse=True)
    return [schedule for schedule, _ in weighted_population[:POPULATION_SIZE // 2]]

# Crossover function
def crossover(parent1, parent2):
    child = {}
    for employee in EMPLOYEES:
        child[employee] = random.choice([parent1[employee], parent2[employee]])
    return child

# Mutation function
def mutate(schedule):
    if random.random() < MUTATION_RATE:
        employee = random.choice(EMPLOYEES)
        schedule[employee] = random.randint(MIN_HOURS_PER_EMPLOYEE, MAX_HOURS_PER_EMPLOYEE)

# Genetic algorithm implementation
def genetic_algorithm():
    population = generate_population()

    for generation in range(GENERATIONS):
        selected_population = select_population(population)
        new_population = []

        # Crossover
        while len(new_population) < POPULATION_SIZE:
            parent1 = random.choice(selected_population)
            parent2 = random.choice(selected_population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

        # Check for the best solution in the current generation
        best_schedule = max(population, key=fitness)
        print(f"Generation {generation + 1}: Best Fitness = {fitness(best_schedule):.2f}")

        if fitness(best_schedule) > 0.99:  # Early stopping condition
            break

    return best_schedule

# Run the genetic algorithm
best_schedule = genetic_algorithm()
print("\nBest Schedule Found:")
for employee, hours in best_schedule.items():
    print(f"{employee}: {hours} hours")