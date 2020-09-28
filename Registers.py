import Memory
class Registrers(Memory.Memory):
  val = [0]*4

  def __init__(self, newVal = [0]*4):
    self.val = newVal

  def getVal(self):
    return self.val

  def modiVal(self, new):
    self.val = new