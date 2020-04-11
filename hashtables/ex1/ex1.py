#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)

#
# Problem:
# you have several boxes, but can only send 2 that combine to a set max weight.
# Find the indicies of those two.
#
# Overall strategy:
# # use the weight_limit - box_weight as the fast-lookup key, and the index as the value.
# # you only have to look up one match and then use the indices from those two as your two boxes.

#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (
    HashTable,
    hash_table_insert,
    hash_table_remove,
    hash_table_retrieve,
    hash_table_resize,
)


def get_indices_of_item_weights(weights, length, limit):
    # ignore length
    ht = HashTable(16)
    index_counter = 0

    # edge case if fewer than 2 boxes
    if len(weights) < 2:
        return None

    else:
        # populate hash table {key:value}
        # box_weight is key
        # value is (limit - box_weight)
        for i in weights:
            hash_table_insert(ht, limit - i, index_counter)
            index_counter += 1

        # iterate though weights
        # look for where weight difference
        # is also in the inventory
        weights_list = []
        new_index_counter = 0

        # traverse once through the original weights list
        # does each item match needed weight gap?
        # which is not itself.
        for i in weights:

            # get weight difference
            # weight_difference = hash_table_retrieve(ht, i)

            # look to see if weight difference is in the list
            if hash_table_retrieve(ht, i):

                # check for being the same item:
                if hash_table_retrieve(ht, i) != new_index_counter:

                    # add index to the list
                    mask1 = hash_table_retrieve(ht, i)
                    # add counter to list
                    mask2 = new_index_counter
                    break

            new_index_counter += 1

        # while there may be two or more valid combos, only one is needed
        # return the indexes, largest first
        answer_tuple = (mask1, mask2)

        return answer_tuple


# def print_answer(answer):
#     if answer is not None:
#         print(str(answer[0]), " ", str(answer[1]))
#         # print(answer[0])
#     else:
#         print("None")


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
