import Memory
class Registers(Memory.Memory):
  val = [0]*4

  def __init__(self, newVal = [0]*4):
    self.val = newVal