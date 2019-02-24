import hashlib
import binascii

class Transaction
    def __init__(self):
        self.id = None
        self.inputs = None
        self.outputs = None

class Output:
    def __init__(self, address, amount):
        self.address = address
        self.amount = amount

class Input:
    def __init__(self):
        self.outputId = None
        self.outputIndex = None
        self.signature = None

class UnspentOutput:
    def __init__(self, outputId, outputIndex, address, amount):
        self.outputId = outputId
        self.outputIndex = outputIndex
        self.address = address
        self.amount = amount

class UnspentOutputs:
    def __init__(self):
        self.__uxto = []
        
    def updateListUtxo(self, list):
        self.__utxo = list

    def newUnspentOutputs(self, transactions):
        list = []
        for transaction in transactions:
            for inpt in transaction.input:
                utxo = UnspentOutput(transaction.id, inpt.outputId, inpt.outputIndex, inpt.address, inpt.amount)
                list.append(utxo)
        self.updateListUtxo(list)

def findUnspentOutput(outputId, outputIndex, listUnspentOutputs):
    for utxo in listUnspentOutputs:
        if utxo.outputId == outputId and utxo.outputIndex == outputIndex:
            return True
    return False

def idTransaction(transaction):
    inputContents = ""
    outputContents = ""
    for input in transaction.inputs:
        inputContents += (input.outputId + input.outputIndex)
    for output in transaction.output:
        outputContents += (output.address + output.amount)
    newIndexContent = (str(inputContents) + str(outputContents)).encode('utf-8')
    return hashlib.sha256(newIndexContent).hexdigest()
