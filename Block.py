import hashlib
import time

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


def calculateHash(index, previousHash, timestamp, data):
    return hashlib.sha256(index + previousHash + timestamp + data).hexdigest()

timestamp = int(round(time.time() * 1000))
genesisBlock = Block(0, "", timestamp, "Genesis Block!",
                calculateHash(0, "", timestamp, "Genesis Block!"))
