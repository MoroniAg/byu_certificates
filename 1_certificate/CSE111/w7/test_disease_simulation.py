import random
import pytest
from disease_simulation import initialize_population, infect_individual, spread_infection, count_states, update_recovery

SEED_PROBLEM = 42


def test_initialize_population():
    population = initialize_population(5)
    assert isinstance(population, list), \
        f"initialize_population must return a list, found {type(population)}"
    assert len(population) == 5, "initialize_population returned wrong size"
    assert all(person['state'] == 'S' and person['days_infected'] == 0 for person in population), \
        "every individual must start as susceptible with 0 days_infected"


def test_infect_individual():
    population = initialize_population(5)
    infect_individual(population, 2)
    assert population[2]['state'] == 'I', "infect_individual did not set state to 'I'"
    assert population[2]['days_infected'] == 0, "infect_individual must set days_infected to 0"


def test_spread_infection():
    random.seed(SEED_PROBLEM)
    population = initialize_population(5)
    infect_individual(population, 0)
    spread_infection(population, infection_rate=1.0)
    infected_total = sum(1 for person in population if person['state'] == 'I')
    state_counts = count_states(population)
    assert infected_total == 5, f"expected 5 infected but found {infected_total}"
    assert state_counts['I'] == 5, f"count_states reports {state_counts['I']} infected"


def test_count_states():
    population = initialize_population(4)
    infect_individual(population, 1)
    population[1]['days_infected'] = 1
    state_counts = count_states(population)
    assert state_counts['I'] == 1, f"expected 1 infected but found {state_counts['I']}"
    assert state_counts['S'] == 3, f"expected 3 susceptible but found {state_counts['S']}"
    assert state_counts['R'] == 0, f"expected 0 recovered but found {state_counts['R']}"


def test_update_recovery():
    population = initialize_population(3)
    infect_individual(population, 0)
    population[0]['days_infected'] = 2
    assert population[0]['state'] == 'I', "precondition: person should be infected before recovery"
    assert population[0]['days_infected'] == 2, "precondition: days_infected should be 2"
    update_recovery(population, recovery_time=2)
    assert population[0]['state'] == 'R', "update_recovery did not set state to 'R' when expected"


def test_initialize_population_from_csv():
    csv_file = "sample_population.csv"
    population = initialize_population(str(csv_file))
    assert isinstance(population, list)
    assert len(population) == 4
    assert population[1]['state'] == 'I' and population[1]['days_infected'] == 2


pytest.main(["-v", "--tb=line", "-rN", __file__])
