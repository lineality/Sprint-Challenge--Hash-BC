import hashlib
import requests
import random
import sys

# from uuid import uuid4
from timeit import default_timer as timer


def proof_of_work(last_proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last five digits of hash(p) are equal
    to the first five digits of hash(p')
    - IE:  last_hash: ...AE912345, new hash 12345888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """

    start = timer()

    print("Searching for next proof")
    proof = str(random.random())

    #  TODO: Your code here
    # block_string = json.dumps(block, sort_keys=True)

    while not valid_proof(last_proof, proof):
        # proof += 1
        proof = str(random.random())

    print("Proof found: " + str(proof) + " in " + str(timer() - start))

    return proof


def valid_proof(last_hash, proof):
    """
    Multi-Ouroboros of Work Algorithm
    - Find a number p' such that the last five digits of hash(p) are equal
    to the first five digits of hash(p')
    - IE:  last_hash: ...AE912345, new hash 12345888...
    - p is the previous proof, and p' is the new proof
    - Use the same method to generate SHA-256 hashes as the examples in class
    """
    last_proof = f"{last_hash}".encode()
    last_proof_hash = hashlib.sha256(last_proof).hexdigest()
    new_proof = f"{proof}".encode()
    new_proof_hash = hashlib.sha256(new_proof).hexdigest()
    # print(last_proof_hash)
    # print(new_proof_hash)
    return new_proof_hash[:5] == str(last_proof_hash)[-5:]


if __name__ == "__main__":
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "https://lambda-coin.herokuapp.com/api"
        # testing
        # node = "https://lambda-coin-test-1.herokuapp.com/api"

    coins_mined = 0

    # Load or create ID
    f = open("my_id.txt", "r")
    id = f.read()
    print("ID is", id)
    f.close()

    if id == "NONAME\n":
        print("ERROR: You must change your name in `my_id.txt`!")
        exit()
    # Run forever until interrupted
    while True:
        # Get the last proof from the server
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get("proof"))

        post_data = {"proof": new_proof, "id": id}

        r = requests.post(url=node + "/mine", json=post_data)
        data = r.json()
        if data.get("message") == "New Block Forged":
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get("message"))
