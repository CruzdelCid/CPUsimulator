from Registers import Registers
from IC import IC
from ALU import ALU
import sys


#PRUEBA 
import yaml

#INSTANCIA DE REGISTROS DE PRUEBA
regis = Registers()
alu = ALU()

#INSTANCIA DE DATA DE PRUEBA
bios = yaml.safe_load(open("bios.yml"))
data = bios['RAM']['data'] 



class ROM(IC): 
  def __init__(self): 
    self.linea = ""
    self.comando = ""
    self.numero = ""

    self.instrucciones={}
    self.instrucciones['0000']='0000'
    self.instrucciones['OUT']='0000'
    self.instrucciones['OUTPUT']='0000'

    self.instrucciones['0001']='0001'
    self.instrucciones['LOAD_R0']='0001'
    self.instrucciones['LD_R0']='0001'
    
    self.instrucciones['0010'] = '0010'
    self.instrucciones['LOAD_R1'] = '0010'
    self.instrucciones['LD_R1'] = '0010'

    self.instrucciones['0011'] = '0011'
    self.instrucciones['AND'] = '0011'

    self.instrucciones['0100'] = '0100'
    self.instrucciones['ILD_R0'] = '0100'
    
    self.instrucciones['0101'] = '0101'
    self.instrucciones['STORE_R0'] = '0101'
    self.instrucciones['STR_R0'] = '0101'

    self.instrucciones['0110'] = '0110'
    self.instrucciones['STORE_R1'] = '0110'
    self.instrucciones['STR_R1'] = '0110'

    self.instrucciones['0111'] = '0111'
    self.instrucciones['OR'] = '0111'

    self.instrucciones['1000'] = '1000'
    self.instrucciones['ILD_R1'] = '1000'

    self.instrucciones['1001'] = '1001'
    self.instrucciones['ADD'] = '1001'

    self.instrucciones['1010'] = '1010'
    self.instrucciones['SUB'] = '1010'

    self.instrucciones['1011'] = '1011'
    self.instrucciones['JUMP'] = '1011'
    self.instrucciones['JMP'] = '1011'

    self.instrucciones['1100'] = '1100'
    self.instrucciones['JUMP_NEG'] = '1100'
    self.instrucciones['JMP_N'] = '1100'

    #Custom Command 1
    self.instrucciones['1101'] = '1101'
    self.instrucciones['SYS_INFO'] = '1101'

    #Custom Command 2
    self.instrucciones['1110'] = '1110'
    self.instrucciones['COPY'] = '1110'

    self.instrucciones['1111'] = '1111'
    self.instrucciones['HALT'] = '1111'
    self.instrucciones['HLT'] = '1111'

    
  #Convierte los números binario a decimal. 
  def convert(self, numero): 
    b_num = list(numero)
    value = 0

    for i in range(len(b_num)):
        digit = b_num.pop()
        if digit == '1':
          value = value + pow(2, i)
    return value
  
  
  """
  Obtiene el valor de un resgistro, numero = a la dirección de registro en formato de dos bits 
  ejemplo: numero = "00" para el registro R0
  """
  def get_reg(self, posicion):
    fact = 0
    if (posicion == "00"): 
      fact = regis.val[0]
    elif(posicion == "01"): 
      fact = regis.val[1]
    elif(posicion == "02"): 
      fact = regis.val[2]
    elif(posicion == "03"): 
      fact = regis.val[3]
    return fact

  #Setea los valores en los registros
  def set_reg(self, posicion, valor): #La entrada de esto será en binario, por ejemplo, "00" para registro 0 (R0)
    if (posicion == "00"):
      regis.val[0] = valor
    elif(posicion == "01"): 
      regis.val[1] = valor
    elif(posicion == "02"): 
      regis.val[2] = valor
    elif(posicion == "03"): 
      regis.val[3] = valor

  #Obtiene los valores de la data cuando se les da su posición
  def get_data(self, posicion): 
    fact = data[posicion]
    return fact

  #define los valores de la data cuando se les da su posición y el nuevo valor
  def set_data(self, posicion, val): 
    data[posicion] = val


  #Recibe la línea y separa el comando (op_code) del número (input)
  def execute_i(self, line): 
    separador = line
    count = len(separador)
    if (count < 5 or separador == "SYS_INFO" or separador == "OUTPUT" or separador == "OUT" or separador == "HALT" or separador == "HLT"):
      self.comando = separador.strip()
      self.numero = "0000"
    else: 
      corte = count - 4 
      self.comando = separador[0:corte].strip()
      self.numero = separador[corte:]
    
    self.format(self.comando)

  #Decoder - para poder detectar instrucción válida e inválida
  #array asociativo
  def format(self, p_comando): 
    
    try:
      comando = self.instrucciones[p_comando]
    except KeyError:
      comando = None
      print('ERROR: comando invalido' )
      #comando = comando
    self.execute_f(comando)   ##ejecutar desde el decoder?

  #Aquí está definido el intruction set table
  def out(self, numero): 
    print(self.get_reg("00"))

  def ld_r0(self, numero):
    direccion = self.convert(numero)
    valor = self.get_data(direccion)
    self.set_reg("00", valor)

  def ld_r1(self, numero):
    direccion = self.convert(numero)
    valor = self.get_data(direccion)
    self.set_reg("01", valor)

  def and_(self, numero):
    num1 = numero[:2]
    num2 = numero[2:]
    fact1 = self.get_reg(num1)
    fact2 = self.get_reg(num2)
    rel = alu.And(fact1, fact2)
    self.set_reg(num2, rel)

  def ild_r0(self, numero):
    direccion = self.convert(numero)
    valor = self.get_data(direccion)
    self.set_reg("00", valor)
  
  def str_r0(self, numero):
    direccion = self.convert(numero)
    valor = self.get_reg("00")
    self.set_data(direccion, valor)

  def str_r1(self, numero):
    direccion = self.convert(numero)
    valor = self.get_reg("01")
    self.set_data(direccion, valor) 

  def or_(self, numero): 
    num1 = numero[:2]
    num2 = numero[2:]
    fact1 = self.get_reg(num1)
    fact2 = self.get_reg(num2)
    rel = alu.Or(fact1, fact2)
    self.set_reg(num2, rel)

  def ild_r1(self, numero): 
    direccion = self.convert(numero)
    valor = self.get_data(direccion)
    self.set_reg("01", valor)

  def add(self, numero): 
    num1 = numero[:2]
    num2 = numero[2:]
    fact1 = self.get_reg(num1)
    fact2 = self.get_reg(num2)
    rel = alu.Add(fact1, fact2)
    self.set_reg(num2, rel)

  def sub(self, numero): 
    num1 = numero[:2]
    num2 = numero[2:]
    fact1 = self.get_reg(num1)
    fact2 = self.get_reg(num2)
    rel = alu.Sub(fact1, fact2)
    self.set_reg(num2, rel)

  def jmp(self, numero): 
    print("11")

  def jmp_n(self, numero): 
    print("12")

  def sys_info(self, numero): 
    print("INFORMACIÓN DEL CPU")
    print(F"Frabricado por: {self.manufacturer}")
    print(F"Fecha de construcción: {self.build_date}")
    print(F"Función {self.purpose}")

  def copy(self, numero):
    num1 = numero[:2]
    num2 = numero[2:]
    valor = self.get_reg(num1)
    self.set_reg(num2, valor)

  def halt(self):
    print("Ejecución terminada, gracias por usar nuestro CPU :)")
    sys.exit(0)
    


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

"""

rom = ROM()
line = ["LOAD_R0 0000", "LOAD_R1 0001", "ADD 0001", "STORE_R1 0011", "OUTPUT", "SYS_INFO", "JUMP 0000"]
rom.execute_i(line[0])
rom.execute_i(line[1])
rom.execute_i(line[2])
rom.execute_i(line[3])
rom.execute_i(line[4])
rom.execute_i(line[5])

print(rom.get_reg("01"))
print("********")
print(data[3])
"""