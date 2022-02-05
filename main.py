from dataclasses import dataclass
import hashlib

class block:
    def __init__(self, data):
        self.data = data
        self.prevHash = "0"
        self.hash = ""

    def getHash(self):
        S = self.data + self.prevHash
        return hashlib.sha256(S.encode()).hexdigest()

    def setHash(self,diff):

       # flag = True
        #while flag:
        #    flag = False
        #    self.hash = self.getHash()
        #    print(self.hash)
        #    for i in range(diff):
        #        if self.hash[i] != '0':
        #            flag = True
        #    
        #        #print(i)
        self.hash = self.getHash()

    def printBlock(self):
        print("-----------------------------------------------------------------------------")
        print("Data : " + self.data)
        print("Hash : " + self.hash)
        print("PrevHash : " + self.prevHash)
        print("-----------------------------------------------------------------------------")

class blockChain:
    chain = []
    def __init__(self):
        b = self.genesis()
        b.setHash(2)
        self.chain.append(b)

    def genesis(self):
        return block("This is genesis block")

    def getLastBlock(self):
        return self.chain[len(self.chain)-1]
    
    def addBlock(self, block):
        block.prevHash = self.getLastBlock().hash
        block.setHash(2)
        self.chain.append(block)

    def printBlockChain(self):
        for i in self.chain:
            i.printBlock()

    def validate(self):
        i = len(self.chain)-1
        #print(i)
        while i > 0 :
            #print(i-1 ,i-2)
            #print(self.chain[i-1].data, )
            if self.chain[i].prevHash != self.chain[i-1].hash:
                #print("1")
                return False
            if self.chain[i].hash != self.chain[i].getHash():
                #print("2")
                return False
            i -= 1
        return True

bitcoin = blockChain()
bitcoin.addBlock(block("HELLO"))
bitcoin.addBlock(block("DOGAR"))
bitcoin.printBlockChain()
print("Blockchain is Valid: ",  bitcoin.validate())
bitcoin.chain[1].data = "HI"
bitcoin.printBlockChain()
print("Blockchain is Valid: ",bitcoin.validate())
