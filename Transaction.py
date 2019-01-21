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

def idTransaction(transaction):
    inputContents = ""
    outputContents = ""
    for input in transaction.inputs:
        inputContents += (input.outputId + input.outputIndex)
    for output in transaction.output:
        outputContents += (output.address + output.amount)
    newIndexContent = (str(inputContents) + str(outputContents)).encode('utf-8')
    return haslib.sha256(newIndexContent).hexdigest()
