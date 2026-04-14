import random
import math
import csv
SEED_PROBLEM = 42


def initialize_population(size_or_path, source='auto'):
    if source not in ('auto', 'count', 'csv'):
        raise ValueError("source must be one of 'auto','count','csv'")

    if source == 'count':
        try:
            count = int(size_or_path)
        except Exception:
            raise TypeError('size must be an integer for source="count"')
        return [{'state': 'S', 'days_infected': 0} for _ in range(count)]

    if source == 'auto':
        if isinstance(size_or_path, str) and size_or_path.isdigit():
            return [{'state': 'S', 'days_infected': 0} for _ in range(int(size_or_path))]
        if isinstance(size_or_path, int):
            return [{'state': 'S', 'days_infected': 0} for _ in range(size_or_path)]

    csv_filename = size_or_path
    population = []
    try:
        with open(csv_filename, "r", newline='') as file:
            reader = csv.reader(file)
            first_row = next(reader, None)
            if first_row is None:
                return population
           
            first_cell = first_row[0].strip().lower() if first_row and first_row[0] else ''
            if not (first_cell in ('status', 'state')):
                row = first_row
                if row:
                    state_value = row[0].strip() if len(row) > 0 else 'S'
                    days_value = row[1].strip() if len(row) > 1 else '0'
                    try:
                        days_int = int(float(days_value))
                    except Exception:
                        days_int = 0
                    population.append({'state': state_value, 'days_infected': days_int})
            for row in reader:
                if not row:
                    continue
                state_value = row[0].strip() if len(row) > 0 else 'S'
                days_value = row[1].strip() if len(row) > 1 else '0'
                try:
                    days_int = int(float(days_value))
                except Exception:
                    days_int = 0
                population.append({'state': state_value, 'days_infected': days_int})
    except FileNotFoundError:
        raise
    return population


def infect_individual(population, index):
    if index < 0 or index >= len(population):
        raise IndexError('index out of range')
    population[index]['state'] = 'I'
    population[index]['days_infected'] = 0


def count_states(population):
    counts = {'S': 0, 'I': 0, 'R': 0}
    for person in population:
        state = person.get('state')
        if state in counts:
            counts[state] += 1
    return counts


def spread_infection(population, infection_rate):
    infected_indices = [i for i, p in enumerate(population) if p['state'] == 'I']
    if not infected_indices:
        return
    for person in population:
        if person['state'] != 'S':
            continue
        for _ in infected_indices:
            if random.random() < infection_rate:
                person['state'] = 'I'
                person['days_infected'] = 0
                break


def update_infection_days(population):
    for person in population:
        if person['state'] == 'I':
            person['days_infected'] += 1


def update_recovery(population, recovery_time):
    for person in population:
        if person['state'] == 'I' and person['days_infected'] >= recovery_time:
            person['state'] = 'R'


def simulate_day(population, infection_rate, recovery_time):
    spread_infection(population, infection_rate)
    update_infection_days(population)
    update_recovery(population, recovery_time)
    return count_states(population)


def run_simulation(days, population_size=None, infection_rate=0.05, recovery_time=14, initial_infected=1, population=None):
    if population is None:
        if population_size is None:
            raise ValueError('population_size or population must be provided')
        population = initialize_population(population_size)
    results = []
    for i in range(min(initial_infected, len(population))):
        infect_individual(population, i)
    for _ in range(days):
        stats = simulate_day(population, infection_rate, recovery_time)
        results.append(stats.copy())
    return results


def get_user_parameters():
    defaults = {
        'days': 30,
        'population_size': 100,
        'infection_rate': 0.05,
        'recovery_time': 14,
        'initial_infected': 1,
    }
    try:
        days_input = input(f"Days to simulate (default {defaults['days']}): ").strip()
        days = int(days_input) if days_input != '' else defaults['days']
    except Exception:
        days = defaults['days']
    try:
        population_size_input = input(f"Population size (default {defaults['population_size']}): ").strip()
        population_size = int(population_size_input) if population_size_input != '' else defaults['population_size']
    except Exception:
        population_size = defaults['population_size']
    try:
        infection_rate_input = input(f"Infection rate (0-1) (default {defaults['infection_rate']}): ").strip()
        infection_rate = float(infection_rate_input) if infection_rate_input != '' else defaults['infection_rate']
    except Exception:
        infection_rate = defaults['infection_rate']
    try:
        recovery_time_input = input(f"Recovery time in days (default {defaults['recovery_time']}): ").strip()
        recovery_time = int(recovery_time_input) if recovery_time_input != '' else defaults['recovery_time']
    except Exception:
        recovery_time = defaults['recovery_time']
    try:
        initial_infected_input = input(f"Initially infected (default {defaults['initial_infected']}): ").strip()
        initial_infected = int(initial_infected_input) if initial_infected_input != '' else defaults['initial_infected']
    except Exception:
        initial_infected = defaults['initial_infected']
    return {
        'days': days,
        'population_size': population_size,
        'infection_rate': infection_rate,
        'recovery_time': recovery_time,
        'initial_infected': initial_infected,
    }


def display_results(results):
    for day, stats in enumerate(results, start=1):
        print(f"Day {day}: S={stats['S']} I={stats['I']} R={stats['R']}")


def save_results_csv(results, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Day', 'S', 'I', 'R'])
        for day, stats in enumerate(results, start=1):
            writer.writerow([day, stats.get('S', 0), stats.get('I', 0), stats.get('R', 0)])

def main():
    params = get_user_parameters()
    random.seed(SEED_PROBLEM)
    choice = input("Run with (N)umber or (C)SV? [N/C]: ").strip().lower()
    population = None
    population_size = None
    if choice == 'c':
        path = input("Enter CSV file path: ").strip()
        population = initialize_population(path, source='csv')
        population_size = len(population)
    else:
        population_size_input = input(f"Enter population size (default {params['population_size']}): ").strip()
        if population_size_input == '':
            population_size = params['population_size']
        else:
            try:
                population_size = int(population_size_input)
            except Exception:
                print("Invalid number, using default.")
                population_size = params['population_size']

    results = run_simulation(params['days'], population_size=population_size, infection_rate=params['infection_rate'], recovery_time=params['recovery_time'], initial_infected=params['initial_infected'], population=population)
    display_results(results)
    save_name = input("Enter filename to save results as CSV (leave blank to skip): ").strip()
    if save_name:
        try:
            save_results_csv(results, save_name)
            print(f"Results saved to {save_name}")
        except Exception as e:
            print(f"Failed to save results: {e}")



if __name__ == "__main__":
    main()