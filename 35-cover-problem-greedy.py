# suppose you’re starting a radio show. You want to
# reach listeners in all 50 US states. You have to decide
# what stations to play on to reach all those listeners. It costs
# money to be on each station, so you’re trying to minimize the
# number of stations you play on. You have a list of stations.
# Each station covers a region, and there’s
# overlap.
# How do you figure out the smallest set of
# stations you can play on to cover all 50
# states? Sounds easy, doesn’t it? Turns out
# it’s extremely hard. Here’s how to do it.
# List every possible subset of stations.
# This is called the power set. There are 2n
# possible subsets.



stations = {}
stations["k_one"] = set(["id", "nv", "ut"])
stations["k_two"] = set(["wa", "id", "mt"])
stations["k_three"] = set(["or", "nv", "ca"])
stations["k_four"] = set(["nv", "ut"])
stations["k_five"] = set(["ca", "az"])

states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])
final_stations = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
            
    states_needed -= states_covered
    final_stations.add(best_station)


