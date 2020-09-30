from Bios import Bios
from IC import IC
from ROM import ROM
from RAM import Parser

import time #para poder hacer el sleep
bios=Bios('bios.yml')
rom=ROM()
#bios
#carga configuración y la deja lista para el programa
##https://pypi.org/project/PyYAML/ para descarga yaml
# fátima avila 

toString = []

class CU(IC):
  def __init__(self, filename):

    self.lines = Parser(filename) #[] ##atributo que contiene la lista de instrucciones 'limpias' sin comentarios ni \n

  def tamano(self): 
    lines = self.lines.lista()
    return len(lines)

  def fetch(self, line): 
    lines = self.lines.lista()
    return lines[line]
    """
    self.lines_original = [] ##atributo que tiene la linea original del programa
    self.parse(filename)
    """

  """
  #parser
  # leer archivo
  def parse (self,filename):
    lines=[]
    file = open(filename, 'r') 
    lines_original = file.readlines()
 
    for i in range(len(lines_original)): 
      #print (i,lines_original[i])

      first_char = lines_original[i][0]
      if first_char != ";":
        lineok = lines_original[i].rstrip("\n")
        lines.append([i,lineok])
      
    self.lines = lines ##atributo que contiene la lista de instrucciones 'limpias' sin comentarios ni \n
    self.lines_original = lines_original
    
  def fetch (self,pos):
    return self.lines[pos][1]  ##devuelve la instrucción de la linea (pos 1)
  """
  
  """
      #Decoder
  # decodificar la linea e identificar comando y atributos o error si comando no identificado
  def decode (self,comando):
    cmd_parts=str.split(comando)
    try:
      instruccion = rom.format(cmd_parts[0])
    except KeyError:
      instruccion=None
      print('ERROR: comando invalido')
    
    ## inicialmente en el decode se habia probado parsear la linea, identificar el comando y los argumento, pero el grupo decidio de aca parsear
    try:
      arg1 = cmd_parts[1] ##devuelve en la posición 1 del return el arg1 si existe o NONE
    except IndexError:
      arg1=None

    try:
      arg2 = cmd_parts[2] ##devuelve en la posición 1 del return el arg1 si existe o NONE
    except IndexError:
      arg2=None
     
    return comando
  """

  ############  inicio de programa ################
  def exec(self, debug = False):

    programa=CU('programa1.cpufm')  
    for i in range(programa.tamano()):
    #fetch
      line2execute = programa.fetch(i) ##método del parser que carga la linea
    al = 'Paso',i
    toString.append(al)
    print ('Paso',i)
    el = 'Fetch ',i,line2execute
    toString.append(el)
    print ('Fetch ',i,line2execute)
    time.sleep(bios.clock*2/.5)
    """
  #decode
    comando=programa.decode(line2execute)
    #arg1 = comando[1]
    #arg2 = comando[2]
    print ('Decode',comando)


    """
    if bios.clock > 0: 
      time.sleep(bios.clock*2/.5)
      rom.execute_i(line2execute)
    else:
      il = "Presione ENTER para continuar:"
      toString.append(il)
      print("Presione ENTER para continuar:")
      foo = input()
      rom.execute_i(line2execute)

    """
    #execute ???
  

    ##TODO los ifs etc, operaciones ALU etc
   
   
    #  print('posición linea original',line2execute[0])
  #  print ('linea original',programa.lines_original[line2execute[0]])
    ##
    """
    ol = '----------' 
    toString.append(ol)
    print('----------') 
    return toString
    ##fin recorrido de las lineas


##todo con ROM para pasar las instrucciones / diccionario

##inicia recorrido de las lineas



