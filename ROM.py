import Registers
from RAM import Parser
from RAM import Data
from IC import IC

#INSTANCIA DE REGISTROS DE PRUEBA
regis = Registers()

class ROM(IC): 
  def __init__(self): 
    self.linea = ""
    self.comando = ""
    self.numero = ""

  #Convierte los números binario a decimal. 
  def convert(self, numero): 

    pass
  
  
  """
  Obtiene el valor de un resgistro, numero = a la dirección de registro en formato de dos bits 
  ejemplo: numero = "00" para el registro R0
  """
  def get_reg(self, numero): 
    fact = 0
    if (numero == "00"): 
      fact = regis[0].get_val
    elif(numero == "01"): 
      fact = regis[1].get_val
    elif(numero == "02"): 
      fact = regis[2].get_val
    elif(numero == "03"): 
      fact = regis[3].get_val
    return fact

  #Setea los valores en los registros
  def set_reg(self, numero, val): #La entrada de esto será en binario, por ejemplo, "00" para registro 0 (R0)
    val = self.numero
    if (numero == "00"):
      regis[0].modi_val(val)
    elif(numero == "01"): 
      regis[1].modi_val(val)
    elif(numero == "02"): 
      regis[2].modi_val(val)
    elif(numero == "03"): 
      regis[3].modi_val(val)


  #Recibe la línea y separa el comando (op_code) del número (input)
  def execute_i(self, line): 
    separador = line
    count = len(separador)
    if (count < 5 or separador == "SYS_INFO" or separador == "SYS_INFO "):
      self.comando = separador.strip()
      self.numero = "0000"
    else: 
      corte = count - 4 
      self.comando = separador[0:corte].strip()
      self.numero = separador[corte:]
      comando = self.comando
    
    self.format(comando)

  #Decoder - para poder detectar instrucción válida e inválida
  #array asociativo
  def format(self, comando): 
    instrucciones={}
    instrucciones['0000']='0000'
    instrucciones['OUT']='0000'
    instrucciones['OUTPUT']='0000'

    instrucciones['0001']='0001'
    instrucciones['LOAD_R0']='0001'
    instrucciones['LD_R0']='0001'
    
    instrucciones['0010'] = '0010'
    instrucciones['LOAD_R1'] = '0010'
    instrucciones['LD_R1'] = '0010'

    instrucciones['0011'] = '0011'
    instrucciones['AND'] = '0011'

    instrucciones['0100'] = '0100'
    instrucciones['ILD_R0'] = '0100'
    
    instrucciones['0101'] = '0101'
    instrucciones['STORE_R0'] = '0101'
    instrucciones['STR_R0'] = '0101'

    instrucciones['0110'] = '0110'
    instrucciones['STORE_R1'] = '0110'
    instrucciones['STR_R1'] = '0110'

    instrucciones['0111'] = '0111'
    instrucciones['OR'] = '0111'

    instrucciones['1000'] = '1000'
    instrucciones['ILD_R1'] = '1000'

    instrucciones['1001'] = '1001'
    instrucciones['ADD'] = '1001'

    instrucciones['1010'] = '1010'
    instrucciones['SUB'] = '1010'

    instrucciones['1011'] = '1011'
    instrucciones['JUMP'] = '1011'
    instrucciones['JMP'] = '1011'

    instrucciones['1100'] = '1100'
    instrucciones['JUMP_NEG'] = '1100'
    instrucciones['JMP_N'] = '1100'

    #Pendiente de definir
    instrucciones['1101'] = '1101'
    instrucciones['SYS_INFO'] = '1101'

    #Pendiente de definir
    instrucciones['1110'] = '1110'
    instrucciones['COPY'] = '1110'

    instrucciones['1111'] = '1111'
    instrucciones['HALT'] = '1111'
    instrucciones['HLT'] = '1111'

    try:
      self.comando = instrucciones[comando]
    except KeyError:
      self.comando = None
      print('ERROR: comando invalido' )
    comando = self.comando
    self.execute_f(comando)

  #Aquí está definido el intruction set table
  def out(self, numero): 
    print("0")

  def ld_r0(self, numero): 
    print("1")

  def ld_r1(self, numero):
    print("2")

  def and_(self, numero): 
    print("3")

  def ild_r0(self, numero):
    print("4")
  
  def str_r0(self, numero): 
    print("5")

  def str_r1(self, numero): 
    print("6")

  def or_(self, numero): 
    print("7")

  def ild_r1(self, numero): 
    print("8")

  def add(self, numero): 
    print("9")

  def sub(self, numero): 
    print("10")

  def jmp(self, numero): 
    print("11")

  def jmp_n(self, numero): 
    print("12")

  def sys_info(self, numero): 
    print("13")

  def copy(self, numero): 
    print("14")

  def halt(self):
    print("15")


  #Aquí ejecutan todas las instrucciones después de ser llamadas por el execute_f, final
  def execute_f(self, comando):
    numero = self.numero
    if (comando == "0000"):
      self.out(numero)

    elif (comando == "0001"):
      self.ld_r0(numero)

    elif (comando == "0010"): 
      self.ld_r1(numero)

    elif (comando == "0011"): 
      self.and_(numero)

    elif (comando == "0100"): 
      self.ild_r0(numero)

    elif (comando == "0101"): 
      self.str_r0(numero)

    elif (comando == "0110"): 
      self.str_r1(numero)

    elif (comando == "0111"): 
      self.or_(numero)

    elif (comando == "1000"): 
      self.ild_r1(numero)

    elif (comando == "1001"): 
      self.add(numero)

    elif (comando == "1010"): 
      self.sub(numero)

    elif (comando == "1011"): 
      self.jmp(numero)

    elif (comando == "1100"): 
      self.jmp_n(numero)

    elif (comando == "1101"): 
      self.sys_info(numero)
    
    elif (comando == "1110"): 
      self.copy(numero)
      
    elif (comando == "1111"): 
      self.halt()
    else:
      print()

class Bios():
  pass

rom = ROM()
line = "COPY 0100"
rom.execute_i(line)
