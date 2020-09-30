from IC import IC
#parser
# leer archivo
class Parser(IC):
  def __init__(self, filename):
    lines=[]
    file = open(filename, 'r') 
    lines_original = file.readlines()

    for i in range(len(lines_original)): 
      #print (i,lines_original[i])

      first_char = lines_original[i][0]
      if first_char != ";":
        lineok = lines_original[i].rstrip("\n")
        lines.append(lineok)
      
    self.lines = lines ##atributo que contiene la lista de instrucciones 'limpias' sin comentarios ni \n
  def lista(self):
    return self.lines

  #Retorna la línea que se le solicita
  def fetch(self, line): 
    return self.lines[line]


m = Parser("programa1.cpufm")

print(m.fetch(0))