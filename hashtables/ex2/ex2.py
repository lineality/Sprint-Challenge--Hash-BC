#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


# overall plan:
# use a hash-table to O(1)_time look up connecting flights
# to reconstruct the travel
def reconstruct_trip(tickets, number_of_flights):

    # Step 1: make and populate a dictionary/hashtable
    # make custom hash-table
    trip_dict = HashTable(number_of_flights)

    # put tickets in the hash table(dictionary)
    for trip in tickets:
        # add items to custom hash-table
        hash_table_insert(trip_dict, trip.source, trip.destination)

    # Step 2: re-create your travel list
    # make travel list
    travel_sequence_list = []

    # start with None source, first leg of trip
    last_flight = hash_table_retrieve(trip_dict, "NONE")

    for i in range(number_of_flights - 1):
        # add flight to list
        travel_sequence_list.append(last_flight)

        # iterate
        last_flight = hash_table_retrieve(trip_dict, last_flight)

    return travel_sequence_list
