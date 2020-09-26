
class IC:
  def __init__ (self):
    self.manufacturer=""
    self.buildDate = ""
    self.purpose = ""

class Memory(IC):
  def __init__ (self):
    self.purpose="Memory"
    self.data=[None]*16   #4 bit CPU ~ 16 posiciones

class ALU(IC):
  def __init__ (self):
    self.purpose="ALU" 
    self.Zero = None
    self.Overflow = None
    self.Negative = None
    self.OP_code = None
    self.Input = None
      

  def Add(self):
    return ("La suma")

  def Substraction(self):
    return ("La resta")

  def Sub(self):
    return ("Resta pidiendo prestado")

  def OneComplements(self):
    return ("one's complement")

  def TwoComplements(self):
    return ("Two's complement")

  def AND(self):
    return ("AND")

  def OR(self):
    return ("OR")

  def BSO(self):
    return ("bit shift operations")

  
  
  
  ##TODO def de todas las funciones:
  ##... it must have all the arithmetic /logic operations supported as functions.
  ## def ()


class CU(IC):
  def __init__ (self):
    self.purpose='Control Unit'

    ##todo def de todas las funciones indicadas en el documento:
    ##.....Fetch, Decode , Execute (send instruction decoded to ALU if needed).

class Register(IC):
  def __init__ (self):
    self.purpose='Register'
    self.data=None

    ##todo def de todas las funciones indicadas en el documento:
    ##.....Fetch, Decode , Execute (send instruction decoded to ALU if needed).
