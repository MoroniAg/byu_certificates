import random
import pytest
from disease_simulation import initialize_population, infect_individual, spread_infection, count_states, update_recovery


def test_initialize_population():
    pop = initialize_population(5)
    assert isinstance(pop, list), \
        f"initialize_population must return a list, found {type(pop)}"
    assert len(pop) == 5, "initialize_population returned wrong size"
    assert all(p['state'] == 'S' and p['days_infected'] == 0 for p in pop), \
        "every individual must start as susceptible with 0 days_infected"


def test_infect_individual():
    pop = initialize_population(5)
    infect_individual(pop, 2)
    assert pop[2]['state'] == 'I', "infect_individual did not set state to 'I'"
    assert pop[2]['days_infected'] == 0, "infect_individual must set days_infected to 0"


def test_spread_infection():
    random.seed(0)
    pop = initialize_population(5)
    infect_individual(pop, 0)
    # with infection_rate=1.0 all susceptibles should become infected
    spread_infection(pop, infection_rate=1.0)
    infected_count = sum(1 for p in pop if p['state'] == 'I')
    assert infected_count == 5, f"expected 5 infected but found {infected_count}"


def test_count_states():
    pop = initialize_population(4)
    infect_individual(pop, 1)
    pop[1]['days_infected'] = 1
    counts = count_states(pop)
    assert counts['I'] == 1 and counts['S'] == 3 and counts['R'] == 0, \
        f"unexpected state counts: {counts}"


def test_update_recovery():
    pop = initialize_population(3)
    infect_individual(pop, 0)
    pop[0]['days_infected'] = 2
    update_recovery(pop, recovery_time=2)
    assert pop[0]['state'] == 'R', "update_recovery did not set state to 'R' when expected"


def test_initialize_population_from_csv(tmp_path):
    csv_file = tmp_path / "pop.csv"
    csv_file.write_text("state,days_infected\nS,0\nI,2\nR,0\nS,1\n")
    pop = initialize_population(str(csv_file))
    assert isinstance(pop, list)
    assert len(pop) == 4
    assert pop[1]['state'] == 'I' and pop[1]['days_infected'] == 2


# Allow running tests directly like the other test files in the repo
pytest.main(["-v", "--tb=line", "-rN", __file__])
