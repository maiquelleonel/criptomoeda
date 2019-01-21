import hashlib
import time
import binascii

class Block:
    def __init__(self, index, previousHash, timestamp, data, hash, difficulty, nonce):
        self.index = index
        self.previousHash = previousHash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash
        self.difficulty = difficulty
        self.nonce = nonce

class Blockchain:
    def __init__(self, genisisBlock):
        self.__chain = []
        self.__chain.append(genesisBlock)
        self.DIFFICULTY_AJUSTMENT = 10
        self.BLOCK_INTERVAL = 120

    def getLatestBlock(self):
        return self.__chain[len(self.__chain) - 1]

    def generateNextBlock(self, data):
        previousBlock = self.getLatestBlock()
        nextIndex = previousBlock.index + 1
        nextPreviousHash = previousBlock.hash
        nextTimestamp = int(round(time.time() * 1000))
        nextHash = calculateHash(nextIndex, nextPreviousHash, nextTimestamp, data)
        newBlock = Block(nextIndex, nextPreviousHash, nextTimestamp, data, nextHash)

        if validateBlock(newBlock) == True:
            self.__chain.append(newBlock)

    def validateBlock(self, newBlock):
        previousBlock = getLatestBlock()
        if previousBlock.index + 1 != newBlock.index:
            return False
        elif previousBlock.hash != newBlock.hash:
            return False
        return True

    def hashMatchesDifficulty(self, hash, difficulty):
        hashBin = binascii.unhexlify(hash)
        requiredPrefix = '0' * int(difficulty)
        return hashBin.startsWith(requiredPrefix)

    def findBlock(self, index, previousHash, timestamp, data, difficulty):
        nonce = 0
        while True:
            hash = calculateHash(index, previousHash, timestamp, data, difficulty, nonce)
            if self.hashMatchesDifficulty(hash, difficulty):
                block = Block(index, previousHash, timestamp, data, difficulty, nonce)
                return Block
            nonce = nonce + 1

    def getDiffculty(self):
        latestBlock = self.getLatestBlock()
        if latestBlock.index % self.DIFFICULTY_AJUSTMENT == 0 and latestBlock.index > 0:
            return self.getAjustedDifficulty()
        else:
            return latestBlock.difficulty

    def getAjustedDifficulty(self):
        latestBlock = self.getLatestBlock()
        prevAjustmentBlock = self.__chain[len(self.__chain - self.DIFFICULTY_AJUSTMENT)]
        timeExpected = self.BLOCK_INTERVAL * self.DIFFICULTY_AJUSTMENT
        timeTaken = latestBlock.timestamp - prevAjustmentBlock.timestamp
        if timeTaken < timeExpected * 2:
            return prevAjustmentBlock.difficulty + 1
        elif timeTaken > timeExpected * 2:
            return prevAjustmentBlock.difficulty - 1
        else:
            return prevAjustmentBlock.difficulty


def calculateHash(index, previousHash, timestamp, data, difficulty, nonce):
    hashData = (str(index) + previousHash + str(timestamp) + data + str(difficulty) + str(nonce)).encode('utf-8')
    return hashlib.sha256(hashData).hexdigest()

ts = int(round(time.time() * 1000))
genesisBlock = Block(0, "", ts, "Genesis Block!", calculateHash(0, "", ts, "Genesis Block!", 1, 0), 1, 0)
