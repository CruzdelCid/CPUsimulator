from IC import IC

class ALU(IC):

    def __init__ (self):
        self.fact1 = 0
        self.fact2 = 0
        self.purpose="ALU" 
        self.Zero = None
        self.Overflow = None
        self.Negative = None
        self.OP_code = None
        self.Input = None
        self.result = 0

    def result(self, resultado):
        self.resultado = resultado
        if(self.resultado == 0): 
            self.Zero = True
            return 0
        elif(self.resultado < 0): 
            self.Negative = True
            return self.resultado * -1
        elif(self.resultado > 15): 
            self.Overflow = True
            return self.resultado - 15
        else: 
            return self.resultado

    def And(self, fact1, fact2):
        self.fact1 = fact1
        self.fact2 = fact2
        return self.result(self.fact1 and self.fact2)

    def Or(self, fact1, fact2):
        self.fact1 = fact1
        self.fact2 = fact2
        return self.result(self.fact1 or self.fact2)
        
    def Add(self, fact1, fact2):
        self.fact1 = fact1
        self.fact2 = fact2
        return self.result(self.fact1 + self.fact2)
    
    def Sub(self, fact1, fact2):
        self.fact1 = fact1
        self.fact2 = fact2
        return self.result(self.fact1 + self.fact2)

    def Xor(self, fact1, fact2):
        self.fact1 = fact1
        self.fact2 = fact2
        return 
    
    def Not(self, fact1, fact2):
        self.fact1 = fact1
        self.fact2 = fact2
        return self.result(0)


