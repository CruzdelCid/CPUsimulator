import Memory
class Register(Memory.Memory):

  val = 0

  def __init__(self, value):
    self.val = value

  def getVal(self):
    return self.val

  def modiVal(self, newVal):
    self.valor = newVal