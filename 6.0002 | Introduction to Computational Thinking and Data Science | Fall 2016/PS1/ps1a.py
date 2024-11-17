"""
  @author: Daniel Faltynowski
"""

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    response = {}
    with open(filename) as file:
        for line in file:
            separated = line.split(sep=',')
            response[separated[0]] = int(separated[1])
    return response


# Problem 2
def max_cow(cows):
    cowName = ''
    cowWeight = 0
    for name, weight in cows.items():
        if weight > cowWeight:
            cowName = name
            cowWeight = weight
    return cowName


def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    herd = cows.copy()
    trips = []
    while herd != {}:
        currentTrip = []
        currentHerd = herd.copy()
        currentLimit = limit
        while currentLimit > 0 and currentHerd != {}:
            currentCow = max_cow(currentHerd)
            if currentLimit - currentHerd[currentCow] >= 0:
                currentTrip.append(currentCow)
                currentLimit = currentLimit - currentHerd[currentCow]
                del herd[currentCow]
            del currentHerd[currentCow]
        trips.append(currentTrip)
    return trips
    



# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


if __name__ == '__main__':
    cows1 = load_cows('ps1_cow_data.txt')
    cows2 = load_cows('ps1_cow_data_2.txt')
    print(greedy_cow_transport(cows1))
