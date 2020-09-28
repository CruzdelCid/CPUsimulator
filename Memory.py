from IC import IC
class Memory(IC):
    def __init__ (self):
        self.purpose="Memory"
        self.buildDate = ""
        self.data=[None]*16   #4 bit CPU ~ 16 posiciones