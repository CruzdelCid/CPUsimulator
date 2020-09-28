
#parser
# leer archivo
class Parser():
  def __init__(self, filename):
    lines=[]
    file = open('programa1.cpufm', 'r') 
    lines_original = file.readlines()

    for i in range(len(lines_original)): 
      #print (i,lines_original[i])

      first_char = lines_original[i][0]
      if first_char != ";":
        lineok = lines_original[i].rstrip("\n")
        lines.append(lineok)
      
    self.lines = lines ##atributo que contiene la lista de instrucciones 'limpias' sin comentarios ni \n

  #Retorna la línea que se le solicita
  def get_line(self, line): 
    return self.lines[line]

class Data():
  def __init__(self, filenam): 
     pass
  pass

"""
progra1 = Parser('programa1.cpufm')
print(progra1.lines)
print(progra1.lines[3])
print(progra1.get_line(3))
"""