from Bios import Bios
from IC import IC

#bios
#carga configuración y la deja lista para el programa
##https://pypi.org/project/PyYAML/ para descarga yaml
# fátima avila 

##todo cargar instrucciones al ROM
instrucciones={}
instrucciones['0000']='0000'
instrucciones['OUT']='0000'
instrucciones['OUTPUT']='0000'
instrucciones['0001']='0001'
instrucciones['LOAD_R0']='0001'
instrucciones['LD_R0']='0001'
instrucciones['0010']='0010'
instrucciones['LOAD_R1']='0010'
instrucciones['LD_R1']='0010'
instrucciones['0011']='0011'
instrucciones['AND']='0011'
instrucciones['0100']='0100'
instrucciones['ILD_R0']='0100'
instrucciones['0101']='0101'
instrucciones['STR_R0']='0101'
instrucciones['STORE_R1']='0101'
instrucciones['0111']='0111'
instrucciones['OR']='0111'
instrucciones['1000']='1000'
instrucciones['ILD_R1']='1000'
instrucciones['1001']='1001'
instrucciones['ADD']='1001'
instrucciones['1010']='1010'
instrucciones['SUB']='1010'
instrucciones['1011']='1011'
instrucciones['JMP']='1011'
instrucciones['JUMP']='1011'
instrucciones['1100']='1100'
instrucciones['JMP_N']='1100'
instrucciones['JUMP_NEG']='1100'
instrucciones['1101']='1101'
instrucciones['SYS_INFO']='1101'
instrucciones['BIOS_INFO']='1110'
instrucciones['1111']='1111'
instrucciones['HALT']='1111'
instrucciones['HLT']='1111'
##-----------



class CU(IC):
  def __init__(self, filename):
    self.lines = [] ##atributo que contiene la lista de instrucciones 'limpias' sin comentarios ni \n
    self.lines_original = [] ##atributo que tiene la linea original del programa
    self.parse(filename)

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

      #Decoder
  # decodificar la linea e identificar comando y atributos o error si comando no identificado
  def decode (self,comando):
    cmd_parts=str.split(comando)
    try:
      instruccion = instrucciones[cmd_parts[0]]
    except KeyError:
      instruccion=None
      print('ERROR: comando invalido')

    try:
      arg1 = cmd_parts[1] ##devuelve en la posición 1 del return el arg1 si existe o NONE
    except IndexError:
      arg1=None

    try:
      arg2 = cmd_parts[2] ##devuelve en la posición 1 del return el arg1 si existe o NONE
    except IndexError:
      arg2=None
     
    return [instruccion,arg1,arg2]

import time #para poder hacer el sleep
bios=Bios('bios.yaml')
programa=CU('programa1.cpufm')
##todo con ROM para pasar las instrucciones / diccionario

##inicia recorrido de las lineas
for i in range(len(programa.lines)):
  #fetch
    line2execute = programa.fetch(i) ##método del parser que carga la linea
    print ('Paso',i)
    print ('Fetch ',i,line2execute)
    time.sleep(bios.clock*2/.5)
  #decode
    comando=programa.decode(line2execute)
    cmd=comando[0]
    if cmd==None: ##error
        print ('Comando no reconocido :: ',programa.lines_original[programa.lines[i][0]],':: linea ',programa.lines[i][0])
        exit(0)
    
    arg1 = comando[1]
    arg2 = comando[2]
    print ('Decode',comando)
    time.sleep(bios.clock*2/.5)
    #execute
    ##TODO los ifs etc, operaciones ALU etc
   
   
    #  print('posición linea original',line2execute[0])
  #  print ('linea original',programa.lines_original[line2execute[0]])
    ##
    
    print('----------') 
    ##fin recorrido de las lineas

